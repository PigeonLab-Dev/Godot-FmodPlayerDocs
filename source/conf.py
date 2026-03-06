# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Godot FmodPlayer'
copyright = '2026, LuYingYiLong'
author = 'LuYingYiLong'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# 多语言配置
languages = ['zh_CN', 'en', 'de', 'ja']
html_context = {
    'languages': languages,
    'current_language': 'zh_CN',
}

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.
