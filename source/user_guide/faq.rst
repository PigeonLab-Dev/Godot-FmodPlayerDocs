.. _faq:

常见问题
========

本章节整理使用 Godot-FmodPlayer 时经常遇到的问题。若问题与 FMOD 授权、平台发布或商业项目有关，请以 FMOD 官方文档与实际项目合同为准。

.. _faq-plugin-license:

使用 Godot-FmodPlayer 插件有哪些许可条款？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Godot-FmodPlayer 插件本身使用 `MIT 许可证 <https://opensource.org/license/MIT>`_。
这意味着你可以自由使用、修改和分发本插件，但需要保留原始版权与许可证声明。

需要注意的是，Godot-FmodPlayer 依赖 **FMOD Engine**。FMOD 是 Firelight
Technologies Pty Ltd 的专有音频引擎，并不随本插件一起变成开源软件。
如果你的项目会发布、商业化或在特定平台上分发，请阅读
`FMOD Licensing <https://www.fmod.com/licensing>`_ 与
`FMOD Legal Information <https://www.fmod.com/legal>`_，并根据你的项目情况
注册项目或获取相应授权。

.. _faq-fmod-studio-bank:

Godot-FmodPlayer 支持 FMOD Studio Event 或 Bank 吗？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

目前 Godot-FmodPlayer 主要面向 **FMOD Core API**，重点是音频文件播放、
通道控制、混音、DSP 效果与 3D 音频等底层功能。

它不等同于 FMOD Studio 集成，也不提供完整的 Studio Event 工作流。如果你的项目
依赖 FMOD Studio 的事件、参数、Bank 构建与音频设计师工作流，可以考虑使用
`fmod-gdextension <https://github.com/utopia-rise/fmod-gdextension>`_。

.. _faq-module-no-found:

为什么导入 Godot-FmodPlayer 插件后 Godot 报错找不到指定模块？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

请检查是否手动将 FMOD 运行库（如 Windows 的 ``fmod.dll``）放在 ``res://addons/fmod_player/`` 目录之下。如果没有下载 FMOD 运行库请从 `FMOD <https://www.fmod.com>`_ 下载。

因为根据 `FMOD EULA <https://www.fmod.com/legal>`_，Godot-FmodPlayer 无权二次分发 FMOD 运行库。

.. _faq-no-sound:

为什么播放时没有声音？
~~~~~~~~~~~~~~~~~~~~~~

可以按以下顺序检查：

#. 确认场景中使用的是 ``FmodAudioStreamPlayer`` 或对应的 FMOD 播放节点。
#. 确认 ``stream`` 已正确设置，并且音频路径存在。
#. 确认播放器的 ``playing`` 状态、音量、暂停状态没有被脚本覆盖。
#. 确认主通道组或目标通道组没有被静音，音量没有被设置为 0。
#. 查看 Godot 输出面板中是否有 FMOD 初始化、文件加载或解码相关错误。

如果使用代码加载音频，建议先用一个简单的 ``res://`` 路径测试，排除路径、
导入设置和打包路径带来的影响。

.. _faq-stream-vs-sample:

背景音乐和短音效应该分别使用哪种加载模式？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

一般建议：

- 背景音乐、语音、环境音等较长音频使用 ``MODE_STREAM``。
- 点击音、攻击音效、爆炸声等短音效使用 ``MODE_SAMPLE``。

``MODE_STREAM`` 会按需读取音频数据，适合较长文件，可以降低内存占用。
``MODE_SAMPLE`` 会把音频加载到内存中，播放延迟更低，适合频繁触发的短音效。

.. _faq-export-audio-missing:

为什么导出后音频无法播放？
~~~~~~~~~~~~~~~~~~~~~~~~~~

导出后无法播放通常与路径、资源打包或动态库有关：

#. 确认音频文件被包含在 Godot 导出包中。
#. 优先使用 ``res://`` 路径引用项目内资源，避免依赖开发机上的绝对路径。
#. 确认目标平台包含对应架构的 FMOD 运行时库与 GDExtension 文件。
#. 检查导出模板、平台架构和插件提供的二进制文件是否匹配。
#. 在导出版本中打开日志输出，查看是否有文件找不到或动态库加载失败的错误。

如果开发环境可以播放但导出后失败，优先检查导出预设中的资源过滤规则和插件二进制文件。

.. _faq-native-audio-mix:

可以把 Godot 原生 AudioStreamPlayer 和 FmodAudioStreamPlayer 混用吗？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

可以混用，但两者属于不同的音频系统。Godot 原生 ``AudioStreamPlayer`` 走
Godot 的音频服务器， ``FmodAudioStreamPlayer`` 走 FMOD 系统。

如果同一个项目中同时使用两套系统，需要分别管理它们的音量、暂停、总线和生命周期。
对于需要 FMOD DSP、通道组或 3D 音频控制的声音，建议统一使用 FMOD 播放节点，
避免混音逻辑分散。

.. _faq-release-audio-resources:

什么时候需要手动释放音频资源？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

大多数 Godot 资源会随着引用释放而自动清理，但在以下场景中建议主动管理：

- 运行时动态加载了大量音频文件。
- 使用 ``MODE_SAMPLE`` 预加载了大量短音效。
- 关卡切换时需要释放当前关卡专用的音频资源。
- 创建了临时播放器、发射器、DSP 或通道组。

对于不再使用的节点可以调用 ``queue_free()``。对于音频资源，如果文档或 API
提供了 ``clear()`` 等清理方法，可以在确认没有播放器继续使用它之后再调用。

.. _faq-dsp-not-working:

DSP 效果没有生效怎么办？
~~~~~~~~~~~~~~~~~~~~~~~~

先确认 DSP 被添加到了正确的位置。DSP 可以挂在主通道组、指定通道组，或某个正在播放的
通道上；如果加到了错误的通道组，目标声音就不会经过这个效果器。

还需要检查：

#. DSP 是否成功创建。
#. 参数索引和参数类型是否正确。
#. DSP 是否被 bypass。
#. 目标声音是否正在通过该通道或通道组播放。
#. DSP 的添加顺序是否符合预期。

调试时可以先把 DSP 加到主通道组上确认效果本身可用，再移动到更具体的通道组。

.. _faq-mobile-platforms:

移动平台上使用时需要注意什么？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

移动平台更容易受到内存、CPU 和文件读取速度的影响。建议：

- 背景音乐使用 ``MODE_STREAM``。
- 高频短音效使用 ``MODE_SAMPLE`` 并提前加载。
- 避免同时创建过多 DSP，尤其是混响、卷积、复杂滤波等较重效果。
- 控制同时播放的通道数量。
- 在真机上测试延迟、性能和导出包内容。

模拟器和编辑器中的表现不能完全代表真机，发布前应以目标设备测试结果为准。

.. _faq-crash-debugging:

遇到崩溃或 FMOD 错误时应该如何定位？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

建议先收集以下信息：

#. Godot 版本、插件版本和目标平台。
#. 触发问题的最小复现场景。
#. Godot 输出面板中的完整错误信息。
#. 使用的音频格式、加载模式和播放方式。
#. 是否只在导出版本或特定设备上出现。

如果问题可以稳定复现，尽量创建一个只包含必要场景和音频文件的最小项目。这样更容易判断是
路径、导入、平台二进制、FMOD 初始化，还是具体 API 调用导致的问题。

如果无法解决问题，可以在 `Github issue <https://github.com/LuYingYiLong/Godot-FmodPlayer/issues>`_ 提出问题或寻求解决方法。
