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

FmodAudioStreamPlayer3D
-----------------------

继承自：Node3D

用于在 3D 空间中播放音频的节点，支持距离衰减、多普勒效应和定向发射。适合环境音效、NPC 语音等需要空间定位的音频。

属性
~~~~

基础属性
^^^^^^^^

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
   * - ``stream_paused``
     - bool
     - 流暂停状态
   * - ``volume_db``
     - float
     - 音量（分贝，默认 0.0，范围 -80~24）
   * - ``pitch``
     - float
     - 音调（默认 1.0，范围 0.01~4.0）
   * - ``auto_play``
     - bool
     - 自动播放（默认 false）
   * - ``bus``
     - StringName
     - 音频总线名称（默认 "Master"）

3D 属性
^^^^^^^

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``max_distance``
     - float
     - 最大距离（米，默认 10.0）
   * - ``unit_size``
     - float
     - 单位大小（米，默认 1.0，控制衰减起点）
   * - ``attenuation_model``
     - int
     - 衰减模型（见下方常量）
   * - ``area_mask``
     - int
     - 区域遮罩（用于 Area 过滤）

发射角度
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``emission_angle_enabled``
     - bool
     - 启用发射角度限制（默认 false）
   * - ``emission_angle``
     - float
     - 发射角度（度，默认 45，范围 0~90）
   * - ``emission_angle_filter_attenuation_db``
     - float
     - 超出角度时的衰减（dB，默认 -12）

距离滤波器
^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``attenuation_filter_cutoff_hz``
     - float
     - 距离滤波器截止频率（Hz，默认 5000）
   * - ``attenuation_filter_db``
     - float
     - 距离滤波器衰减（dB，默认 0，范围 -80~0）

多普勒效应
^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``doppler_tracking``
     - int
     - 多普勒追踪模式（见下方常量）

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``play(from_position=0.0)``
     - void
     - 从指定位置开始播放（秒）
   * - ``seek(position)``
     - void
     - 跳转到指定位置（秒）
   * - ``stop()``
     - void
     - 停止播放
   * - ``is_playing()``
     - bool
     - 是否正在播放
   * - ``get_playback_position()``
     - float
     - 获取当前播放位置（秒）
   * - ``get_stream()``
     - FmodAudioStream
     - 获取音频流
   * - ``set_stream(stream)``
     - void
     - 设置音频流
   * - ``get_channel()``
     - FmodChannel
     - 获取内部通道（用于高级控制）

常量
~~~~

衰减模型
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 常量
     - 值
     - 说明
   * - ``ATTENUATION_INVERSE_DISTANCE``
     - 0
     - 反距离衰减
   * - ``ATTENUATION_INVERSE_SQUARE_DISTANCE``
     - 1
     - 反距离平方衰减
   * - ``ATTENUATION_LOGARITHMIC``
     - 2
     - 对数衰减（线性到最大距离）
   * - ``ATTENUATION_DISABLED``
     - 3
     - 禁用衰减

多普勒追踪
^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 常量
     - 值
     - 说明
   * - ``DOPPLER_TRACKING_DISABLED``
     - 0
     - 禁用多普勒效应
   * - ``DOPPLER_TRACKING_IDLE_STEP``
     - 1
     - 在 _process 中追踪
   * - ``DOPPLER_TRACKING_PHYSICS_STEP``
     - 2
     - 在 _physics_process 中追踪

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

基础 3D 音频
^^^^^^^^^^^^

.. code-block:: gdscript

    extends Node3D

    @onready var player_3d = $FmodAudioStreamPlayer3D

    func _ready():
        # 加载 3D 音频流
        var stream = FmodAudioStream.load_from_file(
            "res://audio/ambience_cave.wav",
            FmodAudioStream.MODE_STREAM
        )
        
        player_3d.stream = stream
        player_3d.volume_db = -6.0
        player_3d.max_distance = 20.0
        player_3d.unit_size = 2.0
        player_3d.auto_play = true

带发射角度的音频
^^^^^^^^^^^^^^^^

.. code-block:: gdscript

    extends Node3D

    @onready var speaker = $FmodAudioStreamPlayer3D

    func _ready():
        var stream = FmodAudioStream.load_from_file(
            "res://audio/announcement.wav",
            FmodAudioStream.MODE_STREAM
        )
        
        speaker.stream = stream
        
        # 启用定向发射（类似喇叭）
        speaker.emission_angle_enabled = true
        speaker.emission_angle = 30.0  # 30度内为清晰区域
        speaker.emission_angle_filter_attenuation_db = -20.0
        
        # 让发射方向跟随节点旋转
        speaker.rotation.y = PI / 4  # 指向特定方向

动态控制 3D 音频
^^^^^^^^^^^^^^^^

.. code-block:: gdscript

    extends CharacterBody3D

    @onready var engine_sound = $FmodAudioStreamPlayer3D

    func _ready():
        var stream = FmodAudioStream.load_from_file(
            "res://audio/engine.wav",
            FmodAudioStream.MODE_STREAM
        )
        
        engine_sound.stream = stream
        engine_sound.doppler_tracking = FmodAudioStreamPlayer3D.DOPPLER_TRACKING_PHYSICS_STEP
        engine_sound.attenuation_model = FmodAudioStreamPlayer3D.ATTENUATION_INVERSE_SQUARE_DISTANCE
        engine_sound.max_distance = 50.0
        engine_sound.play()

    func _physics_process(delta):
        # 根据速度调整音调
        var speed = velocity.length()
        engine_sound.pitch = 1.0 + (speed / 100.0)

切换音频总线
^^^^^^^^^^^^

.. code-block:: gdscript

    extends Area3D

    # 当进入水下区域时切换音频总线
    func _on_body_entered(body):
        if body.has_node("FmodAudioStreamPlayer3D"):
            var player = body.get_node("FmodAudioStreamPlayer3D")
            player.bus = "Underwater"  # 使用带低通滤波器的总线

属性对比
--------

.. list-table::
   :header-rows: 1

   * - 特性
     - FmodAudioStreamPlayer
     - FmodAudioSampleEmitter
     - FmodAudioStreamPlayer3D
   * - 继承自
     - Node
     - Node
     - Node3D
   * - 资源类型
     - FmodAudioStream
     - FmodAudioStream
     - FmodAudioStream
   * - 播放方式
     - 播放/停止/跳转
     - 发射（一次性）
     - 播放/停止/跳转（3D）
   * - 适合场景
     - 背景音乐、长音频
     - 音效、短音频
     - 3D 空间音频
   * - 3D 支持
     - ❌
     - ❌
     - ✅
   * - 距离衰减
     - ❌
     - ❌
     - ✅
   * - 多普勒效应
     - ❌
     - ❌
     - ✅
   * - 定向发射
     - ❌
     - ❌
     - ✅
   * - 音量控制
     - ✅
     - ❌（使用总线）
     - ✅
   * - 音调控制
     - ✅
     - ❌
     - ✅
   * - 自动播放
     - auto_play 属性
     - auto_emit 属性
     - auto_play 属性
