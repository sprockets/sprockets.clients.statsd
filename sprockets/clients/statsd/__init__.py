"""
StatsD API
==========
The default statsd server that is used is localhost:8125. The ``STATSD``
environment variable can be used to set the statsd server connection
parameters. Note that the socket for communicating with statsd is
created once upon module import and will not change until the application is
restarted or the module is reloaded.

"""
import logging
import os
import socket
import time
import types
try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse

__version__ = '1.2.1'

LOGGER = logging.getLogger(__name__)

STATSD_ADDR = None
SOCKET_ERROR = 'Error sending statsd metric'
STATSD_SOCKET = socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM,
                              socket.IPPROTO_UDP)
STATSD_PREFIX = os.getenv('STATSD_PREFIX', 'sprockets')


def set_address():
    """Set the (host, port) to connect to from the environment.

    If the environment is updated, a call to this function will update the
    address this client connects to.

    This function will prefer to use the ``STATSD`` connection string
    environment variable, but will fall back to using the ``STATSD_HOST``
    and ``STATSD_PORT``.

    """
    global STATSD_ADDR
    connection_string = os.getenv('STATSD')
    if connection_string:
        url = urlparse.urlparse(connection_string)
        STATSD_ADDR = (url.hostname, url.port)
    else:
        STATSD_ADDR = (os.getenv('STATSD_HOST', 'localhost'),
                       int(os.getenv('STATSD_PORT', 8125)))


def set_prefix(prefix_value):
    """Set a statsd prefix that is included when using the statsd functions

    :param str prefix_value: prefix value

    """
    global STATSD_PREFIX
    STATSD_PREFIX = prefix_value


set_address()


def execution_timer(value):
    """The ``execution_timer`` decorator allows for easy instrumentation of
    the duration of function calls, using the method name in the key.

    The following example would add duration timing with the key ``my_function``

    .. code: python

        @statsd.execution_timer
        def my_function(foo):
            pass


    You can also have include a string argument value passed to your method as
    part of the key. Pass the index offset of the arguments to specify the
    argument number to use. In the following example, the key would be
    ``my_function.baz``:

    .. code:python

        @statsd.execution_timer(2)
        def my_function(foo, bar, 'baz'):
            pass

    """
    def _invoke(method, key_arg_position, *args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        duration = time.time() - start_time

        key = [method.func_name]
        if key_arg_position is not None:
            key.append(args[key_arg_position])
        add_timing('.'.join(key), value=duration)
        return result

    if type(value) is types.FunctionType:
        def wrapper(*args, **kwargs):
            return _invoke(value, None, *args, **kwargs)
        return wrapper
    else:
        def duration_decorator(func):
            def wrapper(*args, **kwargs):
                return _invoke(func, value, *args, **kwargs)
            return wrapper
        return duration_decorator


def add_timing(*args, **kwargs):
    """Add a timer value to statsd.  The key is specified as one or more
    strings that will be joined together with period delimiters. The value
    must be specified as a keyword argument. The following example will add a
     timing to the statsd key ``foo.bar.baz`` of ``3.14159``.

     .. code:: python

        add_timing('foo', 'bar', 'baz', value=3.14159)

    :param list parts: The key parts to append to the base key
    :param int|float value: The time value

    """
    _send('.'.join(args), kwargs.get('value', 0), 'ms')


def incr(*args, **kwargs):
    """Increment a statsd counter by the specified value. If you intend to
    increment the value by anything other than one, you must specify the value
    as a keyword argument. In the following example, the statsd key
    ``foo.bar.baz`` will be incremented by ``2``.

    .. code:: python

        incr('foo', 'bar', 'baz', value=2)

    :param list args: Metric name parts to increment
    :param int|float value: The value to increment by

    """
    _send('.'.join(args), kwargs.get('value', 1), 'c')


def set_gauge(*args, **kwargs):
    """Set a gauge value in statsd. The key is specified as one or more
    strings that will be joined together with period delimiters. The value
    must be specified as a keyword argument. The following example will set
    the statsd key ``foo.bar.baz`` to ``3``.

    .. code:: python

        set_gauge('foo', 'bar', 'baz', 3)

    :param list args: The gauge metric name to set
    :param int|float value: The gauge value

    """
    _send('.'.join(args), kwargs.get('value', 0), 'g')


def _send(key, value, metric_type):
    """Send the specified value to the statsd daemon via UDP without a
    direct socket connection.

    :param str value: The properly formatted statsd counter value

    """
    if STATSD_PREFIX:
        key = '.'.join([STATSD_PREFIX, key])
    try:
        STATSD_SOCKET.sendto('{0}:{1}|{2}'.format(key,
                                                  value,
                                                  metric_type).encode(),
                             STATSD_ADDR)
    except socket.error:
        LOGGER.exception(SOCKET_ERROR)
