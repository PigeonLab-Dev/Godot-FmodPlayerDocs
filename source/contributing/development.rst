.. _contributing-development:

开发 FmodPlayer
===============

我们假设你已经了解 `C++ (godot-cpp) <https://docs.godotengine.org/zh-cn/4.x/tutorials/scripting/cpp/index.html>`_ 并克隆了 `FmodPlayer <https://github.com/LuYingYiLong/Godot-FmodPlayer>`_ 仓库了。

你可以使用任何文本编辑器和通过在命令行上调用 ``scons`` 来轻松开发 FmodPlayer，但是如果你要使用IDE，我们推荐您使用 `Visual Studio <https://visualstudio.microsoft.com/>`_。

配置 Visual Stduio
------------------

`Visual Studio Community <https://visualstudio.microsoft.com>`_ 是 `Microsoft <https://www.microsoft.com>`_ 的一个只面向 Windows 的 IDE，个人或者组织内的非商业使用是免费的。它有很多有用的功能，如内存视图、性能视图、源码控制等。

导入项目
~~~~~~~~

你可以通过双击项目根目录下的 ``Godot-FmodPlayer.slnx`` 或使用 Visual Studio **打开项目或解决方案** 选项来打开项目

.. warning::
    Visual Studio 必须配置 C++ 包。可以在安装程序中选择：

    .. image:: ../_static/contributing/vs_install_cpp_package.png
        :align: center

补齐 FMOD 运行库
----------------

由于受 FMOD 许可证约束，FmodPlayer 并没有包含 FMOD 运行库，请前往 `FMOD 下载页面 <https://www.fmod.com/download>`_ 下载 FMOD Engine。

准备好后，以 Windows 默认安装路径为例，找到 ``C:\Program Files (x86)\FMOD SoundSystem\FMOD Studio API Windows\api\core\lib``，复制 ``lib`` 粘贴到 FmodPlayer 的 ``src/thirdparty/fmod/`` 下。然后找到 ``C:\Program Files (x86)\FMOD SoundSystem\FMOD Studio API Windows\api\core\inc``，复制 ``inc`` 粘贴到 FmodPlayer 的 ``src/thirdparty/fmod/`` 下。

你的 ``src/thirdparty`` 目录结构应该是：

.. code-block:: text
    
    thirdparty
    └───fmod
        ├───inc
        │       fmod.cs
        │       fmod.h
        │       fmod.hpp
        │       fmod_codec.h
        │       fmod_common.h
        │       fmod_dsp.cs
        │       fmod_dsp.h
        │       fmod_dsp_effects.h
        │       fmod_errors.cs
        │       fmod_errors.h
        │       fmod_output.h
        │
        └───lib
            ├───arm64
            │       fmod.dll
            │       fmodL.dll
            │       fmodL_vc.lib
            │       fmod_vc.lib
            │
            ├───x64
            │       fmod.dll
            │       fmodL.dll
            │       fmodL_vc.lib
            │       fmod_vc.lib
            │
            └───x86
                    fmod.dll
                    fmodL.dll
                    fmodL_vc.lib
                    fmod_vc.lib
                    libfmod.a
                    libfmodL.a

代码风格
--------

我们采用 ``K&R`` 风格，并且指针/引号左对齐，K&R 风格是一种以C语言创始人 Brian Kernighan 和 Dennis Ritchie 命名的代码书写风格，其特点是左花括号紧跟在语句末尾，代码紧凑且易于阅读。
