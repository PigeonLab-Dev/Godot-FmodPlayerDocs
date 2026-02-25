# Godot-FmodPlayer 文档项目

## 项目概述

本项目是 **Godot-FmodPlayer** 的文档站点，使用 Sphinx 文档生成器构建，采用 reStructuredText 格式编写文档内容。

- **项目名称**: Godot-FmodPlayer
- **项目版本**: 1.0.0
- **作者**: LuYingYiLong
- **版权**: 2026, LuYingYiLong
- **语言**: 简体中文 (zh_CN)
- **GitHub 仓库**: https://github.com/LuYingYiLong/Godot-FmodPlayerDocs

## 技术栈

- **Python**: 3.13.3
- **Sphinx**: 9.1.0 (文档生成工具)
- **主题**: sphinx_rtd_theme 3.1.0 (Read the Docs 主题)
- **文档格式**: reStructuredText (.rst)
- **构建工具**: Make (跨平台: Makefile + make.bat)

### 依赖的 Sphinx 扩展

| 包名 | 版本 | 用途 |
|------|------|------|
| Sphinx | 9.1.0 | 核心文档生成器 |
| sphinx_rtd_theme | 3.1.0 | HTML 主题 |
| sphinxcontrib-applehelp | 2.0.0 | Apple Help 输出支持 |
| sphinxcontrib-devhelp | 2.0.0 | DevHelp 输出支持 |
| sphinxcontrib-htmlhelp | 2.1.0 | HTML Help 输出支持 |
| sphinxcontrib-jquery | 4.1 | jQuery 支持 |
| sphinxcontrib-jsmath | 1.0.1 | JavaScript 数学支持 |
| sphinxcontrib-qthelp | 2.0.0 | Qt Help 输出支持 |
| sphinxcontrib-serializinghtml | 2.0.0 | 序列化 HTML 支持 |

## 项目结构

```
.
├── Makefile              # Unix/Linux/macOS 构建脚本
├── make.bat              # Windows 构建脚本
├── README.md             # 项目简介
├── AGENTS.md             # 本文件 - AI 代理指南
├── source/               # 文档源文件目录
│   ├── conf.py           # Sphinx 配置文件
│   ├── index.rst         # 文档首页/主入口
│   ├── usage.rst         # 使用指南页面
│   ├── export.rst        # 导出说明页面 (待完善)
│   ├── _static/          # 静态资源文件 (图片、CSS、JS 等)
│   └── _templates/       # 自定义 HTML 模板
└── build/                # 构建输出目录
    ├── doctrees/         # 文档树缓存
    └── html/             # HTML 输出文件
```

## 构建命令

### 显示帮助信息

```bash
# Linux/macOS
make help

# Windows
make.bat help
```

### 构建 HTML 文档

```bash
# Linux/macOS
make html

# Windows
make.bat html
```

构建后的 HTML 文件将位于 `build/html/` 目录，可直接在浏览器中打开 `build/html/index.html` 查看。

### 其他输出格式

Sphinx 支持多种输出格式，可通过以下命令构建：

```bash
make <format>
```

支持的格式包括：
- `html` - 独立 HTML 文件
- `dirhtml` - 每个文档一个目录的 HTML
- `singlehtml` - 单页 HTML
- `epub` - EPUB 电子书
- `latex` - LaTeX 源文件
- `man` - Unix Manpage
- `text` - 纯文本
- `xml` - Docutils XML
- `json` - JSON 文件

### 清理构建缓存

```bash
make clean
```

## 文档编写规范

### 文件格式

- 使用 **reStructuredText** (.rst) 格式编写文档
- 文件编码: UTF-8
- 缩进: 使用空格，避免 Tab

### 目录结构组织

- `index.rst` - 文档主入口，包含 toctree 导航
- 每个主要功能或主题创建独立的 `.rst` 文件
- 在 `index.rst` 的 toctree 中添加新页面以纳入导航

### reStructuredText 常用语法

```rst
标题
====

子标题
------

.. _引用标签:

章节标题
~~~~~~~~

**粗体文本** 和 *斜体文本*

代码块::

    这里是代码块内容

行内代码 ``code``

链接:
- 外部链接: `链接文本 <https://example.com>`_
- 内部引用: :doc:`页面名称` 或 :ref:`引用标签`

列表:
- 项目 1
- 项目 2
  - 子项目

1. 有序项目 1
2. 有序项目 2

表格:

====== ======
表头1  表头2
====== ======
内容1  内容2
内容3  内容4
====== ======
```

### 中文排版建议

- 中文与英文/数字之间保留空格
- 使用全角标点符号
- 避免英文标点与中文混用

## 配置说明

Sphinx 配置文件位于 `source/conf.py`，主要配置项：

| 配置项 | 当前值 | 说明 |
|--------|--------|------|
| `project` | 'Godot-FmodPlayer' | 项目名称 |
| `author` | 'LuYingYiLong' | 作者名 |
| `release` | '1.0.0' | 版本号 |
| `language` | 'zh_CN' | 文档语言 |
| `html_theme` | 'sphinx_rtd_theme' | HTML 主题 |
| `extensions` | ["sphinx_rtd_theme"] | 启用的扩展 |
| `templates_path` | ['_templates'] | 模板路径 |
| `html_static_path` | ['_static'] | 静态文件路径 |

## 开发工作流

### 添加新文档页面

1. 在 `source/` 目录下创建新的 `.rst` 文件
2. 在 `source/index.rst` 的 toctree 中添加新页面引用
3. 运行 `make html` 构建并验证

### 添加静态资源

1. 将图片、CSS、JS 等文件放入 `source/_static/` 目录
2. 在文档中使用相对路径引用，例如：
   ```rst
   .. image:: _static/screenshot.png
   ```

### 自定义模板

1. 将自定义模板放入 `source/_templates/` 目录
2. 在 `conf.py` 中配置模板路径（已默认配置）

## 部署

构建后的 `build/html/` 目录包含完整的静态网站文件，可部署到任何静态网站托管服务：

- **GitHub Pages**: 将 `build/html` 内容推送到 `gh-pages` 分支
- **Read the Docs**: 关联 GitHub 仓库自动构建
- **Netlify/Vercel**: 配置构建命令为 `make html`，发布目录为 `build/html`

## 注意事项

1. **不要直接修改 `build/` 目录下的文件**，这些是由 Sphinx 自动生成的
2. 提交代码时，通常不需要提交 `build/` 目录（可添加到 `.gitignore`）
3. 编辑 `.rst` 文件后需要重新运行构建命令才能看到更新
4. 当前文档内容仍在初始阶段，大部分页面为模板内容，需要根据实际项目补充

## 参考资源

- [Sphinx 官方文档](https://www.sphinx-doc.org/en/master/)
- [reStructuredText 语法参考](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)
- [sphinx_rtd_theme 文档](https://sphinx-rtd-theme.readthedocs.io/)
