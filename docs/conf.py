# -*- coding: utf-8 -*-
#
# documentation build configuration file for the 'capturer' package. This
# file is execfile()d with the current directory set to its containing dir.

import sys, os

# Add the 'capturer' source distribution's root directory to the module path.
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration -----------------------------------------------------

# Sphinx extension module names.
extensions = ['sphinx.ext.doctest', 'sphinx.ext.autodoc', 'sphinx.ext.intersphinx']

# Paths that contain templates, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'capturer'
copyright = u'2015, Peter Odding'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# Find the package version and make it the release.
from capturer import __version__ as capturer_version

# The short X.Y version.
version = '.'.join(capturer_version.split('.')[:2])

# The full version, including alpha/beta/rc tags.
release = capturer_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Refer to the Python standard library.
# From: http://twistedmatrix.com/trac/ticket/4582.
intersphinx_mapping = {
    'python': ('http://docs.python.org', None),
}

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Output file base name for HTML help builder.
htmlhelp_basename = 'capturerdoc'

def setup(app):
    # Based on http://stackoverflow.com/a/5599712/788200.
    app.connect('autodoc-skip-member', (lambda app, what, name, obj, skip, options:
                                        False if name == '__init__' and obj.__doc__ else skip))
