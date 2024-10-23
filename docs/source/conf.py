# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ET Engine Python SDK (Core)'
copyright = '2024, Exploration Technologies, Inc.'
author = 'Exploration Technologies, Inc.'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
]

autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'show-inheritance': False,
    'show-source': False,
    'private-members': False,
    'no-special-members': True
}

autosummary_generate = True

autosummary_imported_members = True
add_module_names = False
modindex_common_prefix = ['et_engine.']


html_show_sourcelink = False
html_copy_source = False
html_show_sphinx = False

templates_path = ['_templates']
exclude_patterns = []

autodoc_member_order = 'groupwise'
autosummary_depth = 2

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'

html_static_path = ['_static']
html_css_files = ['custom.css']
