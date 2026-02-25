快速开始
========

本指南将帮助你在几分钟内开始使用 Godot-FmodPlayer。

基本概念
--------

在使用插件之前，了解以下核心概念会很有帮助：

.. glossary::

    FmodServer
        全局单例，管理 FMOD 系统的生命周期。所有 FMOD 功能都通过它访问。

    FmodSystem
        FMOD 核心系统的包装类，用于创建声音、通道、DSP 等。

    FmodAudioStream
        流式音频资源，适合播放大型音乐文件（如背景音乐）。

    FmodAudioSample
        采样音频资源，完全加载到内存，适合播放音效。

    FmodChannel
        代表一个正在播放的声音实例，可以控制播放状态、音量、音调等。

    FmodChannelGroup
        通道组，用于将多个通道组织在一起进行统一控制（混音总线）。

    FmodDSP
        数字信号处理器，用于添加音频效果（混响、EQ 等）。

第一个项目
----------

步骤 1：创建场景
~~~~~~~~~~~~~~~~

1. 创建一个新的 Godot 场景
2. 添加一个 ``Node`` 作为根节点
3. 将场景保存为 ``main.tscn``

步骤 2：添加流式播放器
~~~~~~~~~~~~~~~~~~~~~~

1. 在场景中添加 ``FmodAudioStreamPlayer`` 节点
2. 将其命名为 ``MusicPlayer``
3. 在 Inspector 中设置以下属性：

   - **Bus**: ``Master``
   - **Volume Db**: ``0.0``
   - **Pitch**: ``1.0``

步骤 3：创建音频资源
~~~~~~~~~~~~~~~~~~~~

1. 在文件系统面板中，右键点击 ``res://`` 文件夹
2. 选择 **新建资源...**
3. 搜索并选择 ``FmodAudioStream``
4. 将资源保存为 ``res://music_stream.tres``
5. 在 Inspector 中设置 **File Path** 为你的音乐文件路径（例如 ``res://assets/music/background.mp3``）

步骤 4：播放音乐
~~~~~~~~~~~~~~~~

1. 选择 ``MusicPlayer`` 节点
2. 在 Inspector 中将 ``music_stream.tres`` 拖到 **Stream** 属性上
3. 勾选 **Autoplay** 选项

运行场景，你应该能听到音乐播放了！

代码示例
--------

除了使用编辑器，你也可以通过代码控制音频播放。

基本流式播放
~~~~~~~~~~~~

.. code-block:: gdscript

    extends Node

    @onready var player = $FmodAudioStreamPlayer

    func _ready():
        # 创建流式音频资源
        var stream = FmodAudioStream.new()
        stream.file_path = "res://music/background.mp3"
        
        # 设置播放器
        player.stream = stream
        player.volume_db = -6.0  # 稍微降低音量
        player.play()

播放采样音效
~~~~~~~~~~~~

.. code-block:: gdscript

    extends Node

    @onready var sfx_emitter = $FmodAudioSampleEmitter

    func play_jump_sound():
        var sample = FmodAudioSample.new()
        sample.file_path = "res://sfx/jump.wav"
        
        sfx_emitter.sample = sample
        sfx_emitter.bus = "SFX"
        sfx_emitter.play()

使用代码播放（不通过节点）
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func play_sound_directly():
        # 获取 FMOD 系统
        var system = FmodServer.main_system
        
        # 从文件创建声音
        var sound = system.create_sound_from_file(
            "res://sfx/explosion.wav",
            FmodSystem.MODE_DEFAULT
        )
        
        # 获取主通道组
        var master_group = system.get_master_channel_group()
        
        # 播放声音
        var channel = system.play_sound(sound, master_group, false)

添加音效
~~~~~~~~

.. code-block:: gdscript

    func add_reverb_effect():
        var system = FmodServer.main_system
        
        # 创建混响 DSP
        var reverb = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        
        # 设置混响参数
        reverb.set_parameter_float(0, 0.5)   # Decay time
        reverb.set_parameter_float(1, 0.3)   # Early delay
        reverb.set_parameter_float(2, 0.8)   # Late delay
        reverb.set_parameter_float(3, 0.5)   # HF decay ratio
        
        # 添加到主通道组
        var master = system.get_master_channel_group()
        master.add_dsp(0, reverb)

控制播放
~~~~~~~~

.. code-block:: gdscript

    extends Node

    @onready var player = $FmodAudioStreamPlayer

    func _input(event):
        if event.is_action_pressed("ui_accept"):
            if player.playing:
                player.stop()
            else:
                player.play()
        
        if event.is_action_pressed("ui_up"):
            # 增加音量
            player.volume_db += 3.0
        
        if event.is_action_pressed("ui_down"):
            # 降低音量
            player.volume_db -= 3.0

性能监控
~~~~~~~~

.. code-block:: gdscript

    extends Node

    func _process(delta):
        var system = FmodServer.main_system
        
        # 获取 CPU 使用率
        var cpu_usage = system.get_cpu_usage()
        print("DSP CPU: %.2f%%" % cpu_usage["dsp"])
        
        # 获取正在播放的通道数
        var channels = system.get_channels_playing()
        print("Active channels: %d" % channels["real"])

学习路径
--------

- 继续阅读 :doc:`../user_guide/audio_resources` 深入了解音频资源
- 学习 :doc:`../user_guide/playback` 掌握播放控制
- 探索 :doc:`../user_guide/mixer` 了解混音系统
- 查看 :doc:`../user_guide/dsp_effects` 使用 DSP 效果器

示例项目
--------

你可以在 `GitHub 仓库 <https://github.com/LuYingYiLong/Godot-FmodPlayer>`_ 的 ``examples/`` 目录中找到完整的示例项目：

- **BasicPlayback** - 基础播放示例
- **DSPDemo** - DSP 效果器演示
- **MixerExample** - 混音系统示例
