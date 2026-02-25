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
   * - ``autoplay``
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
        # 加载并播放
        var stream = FmodAudioStream.new()
        stream.file_path = "res://music/bgm.mp3"
        
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

用于播放 ``FmodAudioSample`` 资源的节点，适合音效和短音频。

属性
~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``sample``
     - FmodAudioSample
     - 要播放的采样
   * - ``auto_emit``
     - bool
     - 自动发射（默认 false）
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
     - 播放一次采样
   * - ``set_sample(sample)``
     - void
     - 设置采样
   * - ``get_sample()``
     - FmodAudioSample
     - 获取采样
   * - ``set_bus(bus)``
     - void
     - 设置音频总线
   * - ``get_bus()``
     - String
     - 获取音频总线

示例
~~~~

.. code-block:: gdscript

    extends Node

    @onready var emitter = $FmodAudioSampleEmitter
    var shoot_sample: FmodAudioSample

    func _ready():
        # 预加载采样
        shoot_sample = FmodAudioSample.new()
        shoot_sample.file_path = "res://sfx/shoot.wav"
        
        emitter.sample = shoot_sample
        emitter.bus = "SFX"

    func _input(event):
        if event.is_action_pressed("shoot"):
            play_shoot_sound()

    func play_shoot_sound():
        # 添加随机音调变化
        emitter.emit()

    # 自动发射示例
    func setup_auto_emit():
        var sample = FmodAudioSample.new()
        sample.file_path = "res://sfx/heartbeat.wav"
        
        emitter.sample = sample
        emitter.auto_emit = true  # 设置 sample 时自动播放

属性对比
--------

.. list-table::
   :header-rows: 1

   * - 特性
     - FmodAudioStreamPlayer
     - FmodAudioSampleEmitter
   * - 资源类型
     - FmodAudioStream
     - FmodAudioSample
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
     - autoplay 属性
     - auto_emit 属性
