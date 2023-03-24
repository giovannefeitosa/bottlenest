import sphinx_rtd_theme
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BottleNest'
copyright = '2023, Giovanne Feitosa Afonso <giovanneafonso@gmail.com>'
author = 'Giovanne Feitosa Afonso <giovanneafonso@gmail.com>'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
]

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']

# The master toctree document.
# master_doc = '/mnt/c/Users/Giovanne/dev/experiments/bottlenest/docs/source/index'
