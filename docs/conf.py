# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re

from importlib import import_module
from types import ModuleType

sys.path.insert(0, os.path.abspath('./..'))
sys.path.append(os.path.abspath('localexts'))


# -- Project information -----------------------------------------------------

project = 'fortnitepy'
copyright = '2019-2020, Terbau'
author = 'Terbau'

version = ''
with open('../fortnitepy/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

# The full version, including alpha/beta/rc tags.
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.coverage', 
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinxcontrib_trio',
    # 'sphinx.ext.viewcode',
    'viewcode'
]


autodoc_member_order = 'bysource'
autodoc_typehints = 'none'

# Links used for cross-referencing stuff in other documentation
intersphinx_mapping = {
  'py': ('https://docs.python.org/3', None),
  'aiohttp': ('https://aiohttp.readthedocs.io/en/stable/', None),
  'requests': ('http://docs.python-requests.org/en/latest/', 'requests.inv'),
  'aioxmpp': ('https://docs.zombofant.net/aioxmpp/devel/', None)
}

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# def viewcode_find_source(app, modname):
#     print('viewcode-find-source EVENT', repr(modname))


# def _findsub(module, attribute):
#     for submod in module.__dict__:
#         if not isinstance(submod, ModuleType):
#             continue

#         new = getattr(module, attribute, None)
#         if new is not None:
#             return new


# def _find(module, attribute):
#     try:
#         value = module
#         for attr in attribute.split('.'):
#             if attr:
#                 value = getattr(value, attr, None)
#                 if value is None:
#                     bases = getattr(value, '__bases__', None)
#                     if bases is None:
#                         return None
#                     if len(bases) == 1 and bases[0] is object:
#                         return None

#                     for base in bases:
#                         new = _findsub(base, attribute)
#                         if new is not None:
#                             value = new

#         return getattr(value, '__module__', None)
#     except AttributeError:
#         # sphinx.ext.viewcode can't follow class instance attribute
#         # then AttributeError logging output only verbose mode.
#         return None
#     except Exception:
#         # sphinx.ext.viewcode follow python domain directives.
#         # because of that, if there are no real modules exists that specified
#         # by py:function or other directives, viewcode emits a lot of warnings.
#         # It should be displayed only verbose mode.
#         return None


# def viewcode_follow_imported(app, modname, attribute):
#     print('viewcode-follow-imported EVENT', repr(modname), repr(attribute))

#     if modname is None:
#         return None

#     module = import_module(modname)
#     new = _find(module, attribute)

#     print('NEW FOUND', new)
#     return new


def setup(app):
    app.add_stylesheet('style.css')
    app.add_javascript('custom.js')
    # app.connect('viewcode-find-source', viewcode_find_source)
    # app.connect('viewcode-follow-imported', viewcode_follow_imported)
