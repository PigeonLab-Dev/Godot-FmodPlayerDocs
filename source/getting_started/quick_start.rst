快速开始
========

本指南会带你完成一次最小可用的播放流程：创建播放器、加载音频、播放、暂停和调整音量。
开始前请先完成 :doc:`installation`。

你需要知道的三个概念
--------------------

.. list-table::
   :header-rows: 1

   * - 名称
     - 作用
   * - ``FmodAudioStreamPlayer``
     - 场景中的播放节点，适合播放背景音乐、环境音和普通 2D 声音。
   * - ``FmodAudioStream``
     - FMOD 音频资源，保存音频数据和加载模式。
   * - ``FmodServer``
     - 全局 FMOD 系统入口，用于访问主系统、主通道组和性能数据。

.. tip::

   如果只是播放一段音乐，通常只需要 ``FmodAudioStreamPlayer`` 和
   ``FmodAudioStream``。``FmodSystem``、``FmodChannel``、``FmodDSP`` 等底层对象
   可以等到需要混音、DSP 或更细控制时再学习。

在编辑器中播放第一段音频
~~~~~~~~~~~~~~~~~~~~~~~~

创建场景
~~~~~~~~

#. 新建一个 Godot 场景。
#. 添加一个 ``Node`` 作为根节点。
#. 添加一个 ``FmodAudioStreamPlayer`` 子节点。
#. 保存场景，例如 ``main.tscn``。

导入音频
~~~~~~~~

#. 将音频文件放入项目目录，例如 ``res://music/background.mp3``。
#. 在 Godot 的 **导入** 面板中，将导入类型设置为 **FMOD Audio**。
#. 根据用途选择导入预设：

   - **Stream (Low memory)**：适合背景音乐和较长音频。
   - **Sample (High quality)**：适合短音效和需要低延迟的声音。
   - **Loop Sample**：适合需要循环播放的短音效。

#. 点击 **重新导入**。

播放音频
~~~~~~~~

#. 选中 ``FmodAudioStreamPlayer`` 节点。
#. 在 Inspector 中，将导入后的 ``FmodAudioStream`` 资源设置到 ``Stream`` 属性。
#. 勾选 ``Playing``，或启用 ``Auto Play`` 让它进入场景树时自动播放。

如果听不到声音，请先确认 FMOD 运行库已放入插件目录，并查看 Godot 输出面板是否有
GDExtension 或 FMOD 初始化错误。

用代码加载并播放
----------------

如果不想通过导入器创建资源，也可以直接从路径加载音频文件。

.. code-block:: gdscript

   extends Node

   @onready var player: FmodAudioStreamPlayer = $FmodAudioStreamPlayer

   func _ready() -> void:
       var stream := FmodAudioStream.load_from_file(
           "res://music/background.mp3",
           FmodAudioStream.MODE_STREAM | FmodAudioStream.MODE_LOOP
       )

       if stream == null:
           push_error("Failed to load audio file")
           return

       player.stream = stream
       player.play()

``MODE_STREAM`` 适合长音频；``MODE_LOOP`` 会让音频循环播放。短音效通常更适合使用
``MODE_SAMPLE``，可以降低频繁触发时的播放延迟。

控制播放
--------

下面的示例使用键盘控制播放、暂停和音量。你可以把脚本挂到场景根节点上。

.. code-block:: gdscript

   extends Node

   @onready var player: FmodAudioStreamPlayer = $FmodAudioStreamPlayer

   func _unhandled_input(event: InputEvent) -> void:
       if event.is_action_pressed("ui_accept"):
           player.playing = not player.playing

       if event.is_action_pressed("ui_cancel"):
           player.stream_paused = not player.stream_paused

       if event.is_action_pressed("ui_up"):
           player.volume_db += 3.0

       if event.is_action_pressed("ui_down"):
           player.volume_db -= 3.0

常用属性
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 说明
   * - ``stream``
     - 要播放的 ``FmodAudioStream``。
   * - ``playing``
     - 开始或停止播放。
   * - ``stream_paused``
     - 暂停或恢复，不重置播放位置。
   * - ``volume_db``
     - 播放音量，单位为 dB。
   * - ``pitch``
     - 播放速度和音高，``1.0`` 为原始音高。
   * - ``bus``
     - 输出到指定音频总线，默认是 ``Master``。

播放一次性音效
--------------

如果只是播放一个短音效，也可以直接通过 ``FmodSystem`` 创建声音并播放。

.. code-block:: gdscript

   func play_click_sound() -> void:
       var system: FmodSystem = FmodServer.get_main_system()
       var sound: FmodSound = system.create_sound_from_file(
           "res://sfx/click.wav",
           FmodSystem.FMOD_MODE_CREATESAMPLE
       )

       if sound == null:
           push_error("Failed to load sound")
           return

       var master: FmodChannelGroup = system.get_master_channel_group()
       system.play_sound(sound, master, false)

需要频繁播放同一个音效时，建议提前加载并复用 ``FmodAudioStream`` 或 ``FmodSound``，
不要每次按键都重新从文件读取。

添加一个简单 DSP 效果
---------------------

下面的示例把混响添加到主通道组。这样所有经过主输出的声音都会带有混响。

.. code-block:: gdscript

   func add_reverb_to_master() -> void:
       var system: FmodSystem = FmodServer.get_main_system()
       var reverb: FmodDSP = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)

       if reverb == null:
           push_error("Failed to create reverb DSP")
           return

       var master: FmodChannelGroup = system.get_master_channel_group()
       master.add_dsp(-1, reverb)

.. note::

   ``-1`` 表示把 DSP 添加到链末尾。实际项目中更推荐把效果添加到具体总线或通道组，
   避免影响所有声音。

查看性能数据
------------

Godot-FmodPlayer 会把 FMOD 性能数据注册到 Godot 的性能监视器中。运行项目后，
可以在 **调试器 > 监视器** 中查看 ``FmodCPUUsage`` 和 ``FmodFileUsage`` 相关指标。

也可以在代码中读取：

.. code-block:: gdscript

   func _process(_delta: float) -> void:
       var system: FmodSystem = FmodServer.get_main_system()
       var cpu_usage: Dictionary = system.get_cpu_usage()
       var channels: Dictionary = system.get_channels_playing()

       print("DSP CPU: %.2f%%" % cpu_usage["dsp"])
       print("Real channels: %d" % channels["real_channels"])

下一步
------

- 阅读 :doc:`../user_guide/audio_resources`，了解 ``MODE_STREAM`` 和 ``MODE_SAMPLE`` 的选择。
- 阅读 :doc:`../user_guide/playback`，学习播放、暂停、跳转和通道控制。
- 阅读 :doc:`../user_guide/mixer`，了解总线和混音系统。
- 阅读 :doc:`../user_guide/dsp_effects`，学习使用 DSP 效果。
- 遇到问题时查看 :doc:`../user_guide/faq`。
