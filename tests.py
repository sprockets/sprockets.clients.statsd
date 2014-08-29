"""
Tests for the sprockets.clients.statsd package

"""
import mock
import socket
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from sprockets.clients import statsd


class SendTests(unittest.TestCase):

    def test_socket_sendto_is_invoked(self):
        with mock.patch('socket.socket.sendto') as sendto:
            statsd._send('foo.bar.baz', 'c', 2)
            sendto.assert_called_once_with(b'foo.bar.baz:2|c',
                                           ('localhost', 8125))

    def test_socket_sendto_logs_exception(self):
        with mock.patch('socket.socket.sendto') as sendto:
            with mock.patch('sprockets.clients.statsd.LOGGER') as LOGGER:
                sendto.side_effect = socket.error
                LOGGER.exception = mock.Mock()
                statsd._send('foo.bar.baz', 'c', 2)
                LOGGER.exception.assert_called_once_with(statsd.SOCKET_ERROR)


class AddTimingTests(unittest.TestCase):

    def test_single_delimited_key_invokes_send(self):
        with mock.patch('sprockets.clients.statsd._send') as send:
            statsd.add_timing('foo.bar.baz', value=3.14159)
            send.assert_called_once_with('foo.bar.baz', 3.14159, 'ms')

    def test_invokes_statsd_send_default_value(self):
        with mock.patch('sprockets.clients.statsd._send') as send:
            statsd.add_timing('foo', 'bar', 'baz', 'qux', value=1.123)
            send.assert_called_once_with('foo.bar.baz.qux', 1.123, 'ms')


class IncrTests(unittest.TestCase):

    def test_single_delimited_key_invokes_send(self):
        with mock.patch('sprockets.clients.statsd._send') as send:
            statsd.incr('foo.bar.baz', value=2)
            send.assert_called_once_with('foo.bar.baz', 2, 'c')

    def test_invokes_statsd_send_default_value(self):
        with mock.patch('sprockets.clients.statsd._send') as send:
            statsd.incr('foo', 'bar', 'baz', 'qux')
            send.assert_called_once_with('foo.bar.baz.qux', 1, 'c')


class SetGaugeTests(unittest.TestCase):

    def test_single_delimited_key_invokes_send(self):
        with mock.patch('sprockets.clients.statsd._send') as send:
            statsd.set_gauge('foo.bar.baz', value=20)
            send.assert_called_once_with('foo.bar.baz', 20, 'g')

    def test_invokes_statsd_send_default_value(self):
        with mock.patch('sprockets.clients.statsd._send') as send:
            statsd.set_gauge('foo', 'bar', 'baz', 'qux', value=99)
            send.assert_called_once_with('foo.bar.baz.qux', 99, 'g')
