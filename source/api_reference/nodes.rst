节点 API
========

FmodAudioStreamPlayer
---------------------

继承自：Node

用于播放 ``FmodAudioStream`` 资源的节点，适合背景音乐和长时间音频。

属性
~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``stream``
     - FmodAudioStream
     - 要播放的音频流
   * - ``playing``
     - bool
     - 是否正在播放（只读）
   * - ``volume_db``
     - float
     - 音量（分贝，默认 0.0）
   * - ``pitch``
     - float
     - 音调（默认 1.0）
   * - ``auto_play``
     - bool
     - 自动播放（默认 false）
   * - ``bus``
     - String
     - 音频总线名称（默认 "Master"）
   * - ``stream_paused``
     - bool
     - 流暂停状态

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``play(from_position=0.0)``
     - void
     - 从指定位置开始播放
   * - ``stop()``
     - void
     - 停止播放
   * - ``seek(position)``
     - void
     - 跳转到指定位置（秒）
   * - ``get_playback_position()``
     - float
     - 获取当前播放位置（秒）
   * - ``set_stream(stream)``
     - void
     - 设置音频流
   * - ``get_stream()``
     - FmodAudioStream
     - 获取音频流
   * - ``set_bus(bus)``
     - void
     - 设置音频总线
   * - ``get_bus()``
     - String
     - 获取音频总线
   * - ``set_volume_db(volume_db)``
     - void
     - 设置音量
   * - ``get_volume_db()``
     - float
     - 获取音量
   * - ``set_pitch(pitch)``
     - void
     - 设置音调
   * - ``get_pitch()``
     - float
     - 获取音调

信号
~~~~

.. list-table::
   :header-rows: 1

   * - 信号
     - 说明
   * - ``finished()``
     - 播放完成时发出

示例
~~~~

.. code-block:: gdscript

    extends Node

    @onready var player = $FmodAudioStreamPlayer

    func _ready():
        # 加载并播放（流式模式）
        var stream = FmodAudioStream.load_from_file("res://music/bgm.mp3",
            FmodAudioStream.MODE_STREAM)
        
        player.stream = stream
        player.volume_db = -6.0
        player.play()
        
        # 连接完成信号
        player.finished.connect(_on_playback_finished)

    func _on_playback_finished():
        print("Playback finished!")
        
    func fade_out():
        var tween = create_tween()
        tween.tween_property(player, "volume_db", -80.0, 2.0)
        tween.tween_callback(player.stop)

FmodAudioSampleEmitter
----------------------

继承自：Node

用于播放短音频（音效）的节点，内部使用 ``FmodAudioStream`` 并自动设置 ``MODE_SAMPLE`` 标志。

属性
~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``stream``
     - FmodAudioStream
     - 要播放的音频（自动使用样本模式）
   * - ``auto_emit``
     - bool
     - 自动发射（设置流时自动播放，默认 false）
   * - ``bus``
     - String
     - 音频总线名称（默认 "Master"）

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``emit()``
     - void
     - 播放一次音频
   * - ``set_stream(stream)``
     - void
     - 设置音频流
   * - ``get_stream()``
     - FmodAudioStream
     - 获取音频流
   * - ``set_auto_emit(enable)``
     - void
     - 设置自动发射
   * - ``is_autoemit_enabled()``
     - bool
     - 获取自动发射状态

示例
~~~~

.. code-block:: gdscript

    extends Node

    @onready var emitter = $FmodAudioSampleEmitter
    var shoot_stream: FmodAudioStream

    func _ready():
        # 预加载音效（样本模式）
        shoot_stream = FmodAudioStream.load_from_file("res://sfx/shoot.wav",
            FmodAudioStream.MODE_SAMPLE)
        
        emitter.stream = shoot_stream
        emitter.bus = "SFX"

    func _input(event):
        if event.is_action_pressed("shoot"):
            play_shoot_sound()

    func play_shoot_sound():
        emitter.emit()

    # 自动发射示例
    func setup_auto_emit():
        var stream = FmodAudioStream.load_from_file("res://sfx/heartbeat.wav",
            FmodAudioStream.MODE_SAMPLE)
        
        emitter.stream = stream
        emitter.auto_emit = true  # 设置流时自动播放

属性对比
--------

.. list-table::
   :header-rows: 1

   * - 特性
     - FmodAudioStreamPlayer
     - FmodAudioSampleEmitter
   * - 资源类型
     - FmodAudioStream
     - FmodAudioStream
   * - 播放方式
     - 播放/停止/跳转
     - 发射（一次性）
   * - 适合场景
     - 背景音乐、长音频
     - 音效、短音频
   * - 音量控制
     - ✅
     - ❌（使用总线）
   * - 音调控制
     - ✅
     - ❌
   * - 自动播放
     - auto_play 属性
     - auto_emit 属性
