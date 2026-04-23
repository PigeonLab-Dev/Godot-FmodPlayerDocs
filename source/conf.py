# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# 将 _extensions 目录加入 Python 路径，以便加载本地 Sphinx 扩展
sys.path.insert(0, os.path.abspath('_extensions'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Godot FmodPlayer'
copyright = '2026, LuYingYiLong'
author = 'LuYingYiLong'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'gdscript',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# 添加自定义 CSS 文件
html_css_files = [
    'custom.css',
]

# 全局可用的外部链接别名（所有 .rst 文件均可使用）
rst_epilog = """
.. _int: https://docs.godotengine.org/zh-cn/4.x/classes/class_int.html
.. _float: https://docs.godotengine.org/zh-cn/4.x/classes/class_float.html
.. _bool: https://docs.godotengine.org/zh-cn/4.x/classes/class_bool.html
.. _String: https://docs.godotengine.org/zh-cn/4.x/classes/class_string.html
.. _Dictionary: https://docs.godotengine.org/zh-cn/4.x/classes/class_dictionary.html
.. _Array: https://docs.godotengine.org/zh-cn/4.x/classes/class_array.html
.. _Vector3: https://docs.godotengine.org/zh-cn/4.x/classes/class_vector3.html
.. _Transform3D: https://docs.godotengine.org/zh-cn/4.x/classes/class_transform3d.html
.. _Node: https://docs.godotengine.org/zh-cn/4.x/classes/class_node.html
.. _Node3D: https://docs.godotengine.org/zh-cn/4.x/classes/class_node3d.html
.. _PackedByteArray: https://docs.godotengine.org/zh-cn/4.x/classes/class_packedbytearray.html
.. _RefCounted: https://docs.godotengine.org/zh-cn/4.x/classes/class_refcounted.html
.. _Resource: https://docs.godotengine.org/zh-cn/4.x/classes/class_resource.html
.. _Callable: https://docs.godotengine.org/zh-cn/4.x/classes/class_callable.html
"""

# multi-language docs
# 检测 Read the Docs 的语言设置，默认为中文
language = os.getenv('READTHEDOCS_LANGUAGE', 'zh_CN')

locale_dirs = ['../locales/']                   # 翻译文件存放目录
gettext_compact = False                         # 为每个源文件生成独立的 .po 文件
gettext_uuid = True                             # 为翻译字符串添加唯一标识符
gettext_additional_targets = ['literal-block']  # 允许翻译代码块
