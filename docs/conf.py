#!/usr/bin/env python
from sprockets.clients.statsd import __version__

needs_sphinx = '1.0'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain',
]

release = __version__
version = '.'.join(release.split('.')[0:1])

templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = 'sprockets.clients.statsd'
copyright = '2014, AWeber Communications'
pygments_style = 'sphinx'
intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'requests': ('https://requests.readthedocs.org/en/latest/', None),
    'sprockets': ('https://sprockets.readthedocs.org/en/latest/', None),
}
