sprockets.clients.statsd
========================
The ``sprockets.clients.statsd`` package implements a simple statsd client that
is used by the ``sprockets.mixins.statsd`` package. It can be used in your
applications for sending metric values to statsd.

The default statsd server that is used is ``localhost:8125``. The ``STATSD``
environment variable can be used to set the statsd server connection parameters.
This should take the form of a URL, such as ``udp://statsd.service:8675``.
Note that the socket for communicating with statsd is created once upon module
import and will not change until the application is restarted or the module is
reloaded.

|Version| |Downloads| |Status| |Coverage| |License|

Installation
------------
``sprockets.clients.statsd`` is available on the
`Python Package Index <https://pypi.python.org/pypi/sprockets.clients.statsd>`_
and can be installed via ``pip`` or ``easy_install``:

.. code:: bash

  pip install sprockets.clients.statsd

Documentation
-------------
https://sprocketsclientsstatsd.readthedocs.org

Example
-------
The following example demonstrates how to use ``sprockets.clients.statsd`` by
incrementing a counter, setting a gauge value, and adding a timing value:

.. code:: python

    from sprockets.clients import statsd

    # Increment foo.bar.baz by 1
    statsd.incr('foo', 'bar', 'baz')

    # Set a gauge value
    statsd.set_gauge('foo', 'bar', 'baz', value=10)

    # Add a timing value
    statsd.add_timing('foo', 'bar', 'baz', value=3.14159)

Documentation is available at https://sprocketsclientsstatsd.readthedocs.org

Version History
---------------
Available at https://sprocketsclientsstatsd.readthedocs.org/en/latest/history.html

.. |Version| image:: https://badge.fury.io/py/sprockets.clients.statsd.svg?
   :target: http://badge.fury.io/py/sprockets.clients.statsd

.. |Status| image:: https://travis-ci.org/sprockets/sprockets.clients.statsd.svg?branch=master
   :target: https://travis-ci.org/sprockets/sprockets.clients.statsd

.. |Coverage| image:: https://img.shields.io/coveralls/sprockets/sprockets.clients.statsd.svg?
   :target: https://coveralls.io/r/sprockets/sprockets.clients.statsd

.. |Downloads| image:: https://pypip.in/d/sprockets.clients.statsd/badge.svg?
   :target: https://pypi.python.org/pypi/sprockets.clients.statsd

.. |License| image:: https://pypip.in/license/sprockets.clients.statsd/badge.svg?
   :target: https://sprocketsclientsstatsd.readthedocs.org
