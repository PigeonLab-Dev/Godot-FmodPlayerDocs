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

# multi-language docs
language = 'zh_CN'
locale_dirs = ['../locales/']   # 翻译文件存放目录
gettext_compact = False         # 为每个源文件生成独立的 .po 文件
gettext_uuid = True             # 为翻译字符串添加唯一标识符
gettext_additional_targets = ['literal-block']  # 允许翻译代码块
