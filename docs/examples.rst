Examples
========
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
