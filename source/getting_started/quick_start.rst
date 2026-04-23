快速开始
========

本指南将帮助你在几分钟内开始使用 Godot-FmodPlayer。

基本概念
--------

在使用插件之前，了解以下核心概念会很有帮助：

.. glossary::

    FmodServer
        全局单例，管理 FMOD 系统的生命周期。所有 FMOD 功能都通过它访问

    FmodSystem
        FMOD 核心系统的包装类，用于创建声音、通道、DSP 等

    FmodAudioStream
        FMOD 可识别的音频资源类，有流式、样本、循环，双向循环四种创建标志

    FmodChannel
        代表一个正在播放的声音实例，可以控制播放状态、音量、音调等

    FmodChannelGroup
        通道组，用于将多个通道组织在一起进行统一控制（混音总线）

    FmodSound
        声音对象，包含音频数据和播放属性，可以通过 **FmodSystem** 创建

    FmodSoundGroup
        声音组，用于管理声音资源的内存和加载行为

    FmodDSP
        数字信号处理器，用于添加音频效果（混响、EQ 等）

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

步骤 3：导入音频资源
~~~~~~~~~~~~~~~~~~~~

1. 将你的音乐文件（例如 ``background.mp3``）导入到项目中
2. 在 Improter 设置中选择 **FMOD Audio** 作为导入类型并重新导入

步骤 4：播放音乐
~~~~~~~~~~~~~~~~

1. 在 ``FmodAudioStreamPlayer`` 节点的 Inspector 中点击 **Stream** 选择刚才导入的音频资源，或者在 Inspector 中将 ``music_stream.tres`` 拖到 **Stream** 属性上
2. 勾选 **Playing** 启动播放

代码示例
--------

除了使用编辑器，你也可以通过代码控制音频播放。

基本流式播放
~~~~~~~~~~~~

.. code-block:: gdscript

    extends Node

    @onready var player: FmodAudioStreamPlayer = $FmodAudioStreamPlayer

    func _ready() -> void:
        var stream = FmodAudioStream.new()
        stream.load_from_file("res://music/background.mp3")
        player.stream = stream
        player.play()

使用代码播放（不通过节点）
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func play_sound_directly() -> void:
        var system: FmodSystem = FmodServer.get_main_system()
        var sound: FmodSound = system.create_sound_from_file(
            "res://sfx/explosion.wav",
            FmodSystem.MODE_DEFAULT
        )
        var master_group: FmodChannelGroup = system.get_master_channel_group()
        var channel: FmodChannel = system.play_sound(sound, master_group, false)

添加 DSP 效果
~~~~~~~~

.. code-block:: gdscript

    func add_reverb_effect() -> void:
        var system: FmodSystem = FmodServer.get_main_system()
        var reverb: FmodDSP = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        
        reverb.set_parameter_float(0, 0.5)
        reverb.set_parameter_float(1, 0.3)
        reverb.set_parameter_float(2, 0.8)
        reverb.set_parameter_float(3, 0.5)
        
        var master: FmodChannelGroup = system.get_master_channel_group()
        master.add_dsp(0, reverb)

控制播放
~~~~~~~~

.. code-block:: gdscript

    extends Node

    @onready var player: FmodAudioStreamPlayer = $FmodAudioStreamPlayer

    func _unhandled_input(event: InputEvent) -> void:
        if event.is_action_just_pressed(&"ui_accept"):
            if player.playing:
                player.stop()
            else:
                player.play()
        
        if event.is_action_just_pressed(&"ui_up"):
            player.volume_db += 3.0
        
        if event.is_action_just_pressed(&"ui_down"):
            player.volume_db -= 3.0

性能监控
~~~~~~~~

.. code-block:: gdscript

    extends Node

    func _process(_delta: float) -> void:
        var system: FmodSystem = FmodServer.main_system
        
        var cpu_usage: Dictionary = system.get_cpu_usage()
        print("DSP CPU: %.2f%%" % cpu_usage["dsp"])
        
        var channels: Dictionary = system.get_channels_playing()
        print("Active channels: %d" % channels["real"])

学习路径
--------

- 继续阅读 :doc:`../user_guide/audio_resources` 深入了解音频资源
- 学习 :doc:`../user_guide/playback` 掌握播放控制
- 探索 :doc:`../user_guide/mixer` 了解混音系统
- 查看 :doc:`../user_guide/dsp_effects` 使用 DSP 效果器

