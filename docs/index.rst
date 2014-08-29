sprockets.clients.statsd
========================
The ``sprockets.clients.statsd`` package implements a simple statsd client that
is used by the ``sprockets.mixins.statsd`` package. It can be used in your
applications for sending metric values to statsd.

|Version| |Downloads| |Status| |Coverage| |License|

Installation
------------
``sprockets.clients.statsd`` is available on the
`Python Package Index <https://pypi.python.org/pypi/sprockets.clients.statsd>`_
and can be installed via ``pip`` or ``easy_install``:

.. code:: bash

  pip install sprockets.clients.statsd

Configuration
-------------
The default statsd server that is used is ``localhost:8125``. The ``STATSD_HOST``
and ``STATSD_PORT`` environment variables can be used to set the statsd server
connection parameters. Note that the socket for communicating with statsd is
created once upon module import and will not change until the application is
restarted or the module is reloaded.

API Documentation
-----------------
.. toctree::
   :maxdepth: 2

   api
   examples

Version History
---------------
See :doc:`history`

Issues
------
Please report any issues to the Github project at `https://github.com/sprockets/sprockets.clients.statsd/issues <https://github.com/sprockets/sprockets.clients.statsd/issues>`_

Source
------
sprockets.clients.statsd source is available on Github at `https://github.com/sprockets/sprockets.clients.statsd <https://github.com/sprockets/sprockets.clients.statsd>`_

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. |Version| image:: https://badge.fury.io/py/sprockets.clients.statsd.svg?
   :target: http://badge.fury.io/py/sprockets.clients.statsd

.. |Status| image:: https://travis-ci.org/sprockets/sprockets.clients.statsd.svg?branch=master
   :target: https://travis-ci.org/sprockets/sprockets.clients.statsd

.. |Coverage| image:: https://img.shields.io/coveralls/sprockets/sprockets.clients.statsd.svg?
   :target: https://coveralls.io/r/sprockets/sprockets.clients.statsd

.. |Downloads| image:: https://pypip.in/d/sprockets.clients.statsd/badge.svg?
   :target: https://pypi.python.org/pypi/sprockets.clients.statsd

.. |License| image:: https://pypip.in/license/sprockets.clients.statsd/badge.svg?
   :target: https://sprockets.clients.statsd.readthedocs.org
