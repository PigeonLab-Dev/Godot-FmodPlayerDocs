安装指南
========

系统要求
--------

- **Godot 版本**: 4.1 或更高版本
- **操作系统**: Windows 10/11, Android
- **编译器** (如需从源码构建):
  - Windows: MSVC v145+ (Visual Studio 2022)
  - Android: Android NDK

.. important::
   
   **FMOD 运行库需要手动下载**
   
   由于 FMOD 的许可协议不允许二次分发，你需要自行从 
   `FMOD 官网 <https://www.fmod.com/download>`_ 下载 FMOD Core API。
   
   - 注册/登录 FMOD 账户
   - 下载对应平台的 FMOD Core API
   - 将运行库文件（如 Windows 的 ``fmod.dll``）放置到插件目录

安装方式
--------

方式一：预编译二进制文件（推荐）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 从 `GitHub Releases <https://github.com/LuYingYiLong/Godot-FmodPlayer/releases>`_ 下载最新版本

2. 解压下载的文件，将 ``addons/fmod_player`` 文件夹复制到你的 Godot 项目的 ``res://addons/`` 目录下

3. 从 FMOD 官网下载 FMOD Core API，将运行库文件放入插件目录::

    res://
    └── addons/
        └── fmod_player/
            ├── bin/
            │   ├── fmod_player.gdextension      # GDExtension 配置
            │   ├── fmod.dll                     # Windows FMOD 运行库（需自行下载）
            │   ├── libfmod.so                   # Android FMOD 运行库（需自行下载）
            │   ├── fmod_player.windows.*.dll    # 插件 DLL
            │   └── ...
            └── ...

4. 在 Godot 编辑器中，进入 **项目 > 项目设置 > 插件**，启用 "FmodPlayer"

方式二：从源码构建
~~~~~~~~~~~~~~~~~~~~

前置要求
^^^^^^^^

- Python 3.8+
- SCons 4.0+
- C++ 编译器 (MSVC v145+ 或 Android NDK)
- Git

获取源码
^^^^^^^^

.. code-block:: bash

    git clone --recursive https://github.com/LuYingYiLong/Godot-FmodPlayer.git
    cd Godot-FmodPlayer

.. note::
   
   使用 ``--recursive`` 参数确保 ``godot-cpp`` 子模块被正确克隆。

Windows 构建
^^^^^^^^^^^^

.. code-block:: bash

    # 调试版本
    scons platform=windows target=template_debug arch=x86_64

    # 发布版本
    scons platform=windows target=template_release arch=x86_64

    # 编辑器版本
    scons platform=windows target=editor arch=x86_64

Android 构建
^^^^^^^^^^^^

.. code-block:: bash

    # ARM64 调试版本
    scons platform=android target=template_debug arch=arm64

    # ARM64 发布版本
    scons platform=android target=template_release arch=arm64

构建选项说明
^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 选项
     - 可选值
     - 说明
   * - ``platform``
     - ``windows``, ``android``
     - 目标平台
   * - ``target``
     - ``template_debug``, ``template_release``, ``editor``
     - 构建目标类型
   * - ``arch``
     - ``x86_64``, ``arm64``, ``arm32``, ``x86_32``
     - 目标架构

输出位置
^^^^^^^^

构建完成后，二进制文件位于::

    addons/bin/
    ├── fmod_player.windows.{target}.{arch}.dll    # Windows
    ├── libfmod_player.android.{target}.{arch}.so  # Android
    └── ...

FMOD 运行库获取
----------------

由于 FMOD 的许可协议不允许二次分发，你需要自行下载 FMOD Core API 运行库。

下载步骤
~~~~~~~~

1. 访问 `FMOD 官网下载页面 <https://www.fmod.com/download>`_
2. 注册或登录 FMOD 账户
3. 下载 **FMOD Engine** （选择对应你的开发平台的版本）
4. 解压下载的文件

获取运行库文件
~~~~~~~~~~~~~~

根据你的目标平台，从下载的 FMOD Engine 中找到对应的运行库文件：

**Windows:**

- 文件: ``fmod.dll`` （发布版）或 ``fmodL.dll`` （调试版）
- 位置: ``api/core/lib/x64/``
- 放置到: ``addons/fmod_player/bin/``

**Android:**

- 文件: ``libfmod.so`` （发布版）或 ``libfmodL.so`` （调试版）
- 位置: ``api/core/lib/android/`` （按架构选择子目录）
- 放置到: 需要打包到 APK 的库目录

许可证说明
~~~~~~~~~~

- FMOD 允许免费用于非商业项目
- **商业项目需要获取 FMOD 许可证**
- 详见 `FMOD 许可页面 <https://www.fmod.com/licensing>`_

验证安装
--------

1. 打开 Godot 编辑器
2. 创建一个新场景
3. 在节点面板中搜索 "Fmod"，应该能看到以下节点：

   - ``FmodAudioStreamPlayer`` - 流式音频播放器
   - ``FmodAudioSampleEmitter`` - 采样音频发射器

4. 在资源面板中创建新资源，应该能看到：

   - ``FmodAudioStream`` - 流式音频资源
   - ``FmodAudioSample`` - 采样音频资源
   - ``FmodAudioBusLayout`` - 音频总线布局

常见问题
--------

插件未显示在节点列表中
~~~~~~~~~~~~~~~~~~~~~~

- 检查 ``addons/bin/fmod_player.gdextension`` 文件是否存在
- 检查对应平台的 DLL/SO 文件是否存在
- 查看 Godot 编辑器的 **输出** 面板是否有加载错误
- 确认 Godot 版本 >= 4.1

FMOD 初始化失败
~~~~~~~~~~~~~~~

- 检查 ``fmod.dll`` (Windows) 或 ``libfmod.so`` (Android) 是否在正确位置
- 检查音频设备是否正常工作
- 查看 Godot 控制台输出获取详细错误信息

Android 构建失败
~~~~~~~~~~~~~~~~

- 确保 Android NDK 已正确安装并设置环境变量
- 确认 ``godot-cpp`` 子模块已初始化::

    git submodule update --init --recursive

下一步
------

安装完成后，请阅读 :doc:`quick_start` 了解如何使用本插件。
