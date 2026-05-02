.. _contributing-translation:

翻译 Godot-FmodPlayer
=====================

Godot-FmodPlayer 的文档和插件界面都需要稳定的翻译维护。翻译贡献不只是把中文逐句替换成英文，更重要的是保持术语、API 名称、示例代码和页面结构一致。

在线文档翻译
------------

在线文档使用 `Sphinx <https://www.sphinx-doc.org/en/master/>`_ 构建，源文件位于 ``source/``，格式为 reStructuredText。

英文文档通过 gettext / PO 文件维护。请不要直接复制一份英文 ``.rst`` 来翻译，否则后续中文源文档更新时很难同步。

常用流程如下：

.. code-block:: bash

    sphinx-build -b gettext source build/gettext
    sphinx-intl update -p build/gettext -l en

翻译文件位于：

.. code-block:: text

    locales/en/LC_MESSAGES/

修改 ``.po`` 后，编译并构建英文 HTML：

.. code-block:: bash

    sphinx-intl build -l en
    sphinx-build -b html -D language=en source build/html_en

翻译时请注意：

- ``msgid`` 保持不变，只修改 ``msgstr``。
- API 类名、方法名、属性名和枚举名不要翻译。
- ``:ref:``、``:doc:``、```code```、链接和 GDScript 示例要保持可构建。
- 中文术语请优先参考 :doc:`../glossary`。
- 如果源文档改了标题或标记，记得重新生成 gettext 模板并更新 PO。

离线文档翻译
------------

离线类参考文档使用 XML 风格的类描述。它更接近 Godot 官方类参考格式，适合编辑器内提示、类说明和属性描述。

.. seealso::

    `Godot class reference primer <https://docs.godotengine.org/en/4.x/engine_details/class_reference/index.html#doc-class-reference-primer>`_

维护离线文档时，请保持 API 名称与 GDExtension 绑定一致。新增类、属性、方法或枚举后，应同步检查在线文档与离线文档是否都已更新。

属性本地化
----------

插件属性本地化用于编辑器检查器中的显示名称、分组和提示文本。它与在线文档翻译不是同一套文件。

如果你修改了导出的属性名、分类或提示文本，请同时检查：

- GDExtension 绑定中的属性名称。
- 编辑器中实际显示的本地化文本。
- 在线 API 文档中的属性说明。

翻译检查
--------

提交翻译前建议至少检查：

- 英文 HTML 能否成功构建。
- 页面中是否残留明显中文。
- 是否存在 ``msgstr "."``、``#, fuzzy`` 或明显机器翻译残留。
- 代码块、内部引用和表格是否渲染正常。

如果不确定某个术语怎么翻译，可以先保留 API 原名，并在 PR 中说明疑问。术语一致性比单句看起来华丽更重要。
