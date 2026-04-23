播放控制
========

Godot-FmodPlayer 提供灵活的播放控制功能，支持通过节点或代码直接控制音频播放。

播放节点
--------

FmodAudioStreamPlayer
~~~~~~~~~~~~~~~~~~~~~

用于播放 ``FmodAudioStream`` 资源的节点，适合背景音乐和长时间音频。

**主要属性：**

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``stream``
     - FmodAudioStream
     - 要播放的音频流
   * - ``playing``
     - bool (readonly)
     - 是否正在播放
   * - ``volume_db``
     - float
     - 音量（分贝）
   * - ``pitch``
     - float
     - 音调（1.0 = 正常）
   * - ``autoplay``
     - bool
     - 场景开始时自动播放
   * - ``bus``
     - String
     - 音频总线名称

**主要方法：**

.. list-table::
   :header-rows: 1

   * - 方法
     - 说明
   * - ``play(from_position=0.0)``
     - 从指定位置开始播放
   * - ``stop()``
     - 停止播放
   * - ``seek(position)``
     - 跳转到指定位置
   * - ``get_playback_position()``
     - 获取当前播放位置

**代码示例：**

.. code-block:: gdscript

    extends Node

    @onready var player = $FmodAudioStreamPlayer

    func _ready():
        var stream = FmodAudioStream.new()
        stream.file_path = "res://music/bgm.mp3"
        player.stream = stream

    func play_music():
        player.play()

    func stop_music():
        player.stop()

    func fade_volume(target_db: float, duration: float):
        var tween = create_tween()
        tween.tween_property(player, "volume_db", target_db, duration)

FmodAudioSampleEmitter
~~~~~~~~~~~~~~~~~~~~~~

用于播放 ``FmodAudioSample`` 资源的节点，适合音效和短音频。

**主要属性：**

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
     - 自动发射（设置 sample 时自动播放）
   * - ``bus``
     - String
     - 音频总线名称

**主要方法：**

.. list-table::
   :header-rows: 1

   * - 方法
     - 说明
   * - ``emit()``
     - 播放一次采样
   * - ``set_sample(sample)``
     - 设置并加载采样

**代码示例：**

.. code-block:: gdscript

    extends Node

    @onready var emitter = $FmodAudioSampleEmitter

    func _ready():
        var sample = FmodAudioSample.new()
        sample.file_path = "res://sfx/shoot.wav"
        emitter.sample = sample

    func play_shoot():
        emitter.emit()

直接代码播放
------------

不通过节点，直接使用 ``FmodSystem`` 播放音频。

基本播放
~~~~~~~~

.. code-block:: gdscript

    func play_sound_simple(path: String):
        var system = FmodServer.main_system
        
        # 创建声音
        var sound = system.create_sound_from_file(path, FmodSystem.MODE_DEFAULT)
        
        # 获取主通道组
        var master = system.get_master_channel_group()
        
        # 播放（paused=false 立即播放）
        var channel = system.play_sound(sound, master, false)
        
        return channel

高级播放控制
~~~~~~~~~~~~

.. code-block:: gdscript

    func play_sound_advanced(path: String):
        var system = FmodServer.main_system
        
        # 创建声音（使用特定模式）
        var mode = FmodSystem.MODE_LOOP_OFF | FmodSystem.MODE_3D
        var sound = system.create_sound_from_file(path, mode)
        
        # 创建通道组
        var sfx_group = system.create_channel_group("SFX")
        
        # 播放并暂停（准备状态）
        var channel = system.play_sound(sound, sfx_group, true)
        
        # 设置参数
        channel.set_volume_db(-6.0)
        channel.set_pitch(1.2)
        
        # 开始播放
        channel.set_paused(false)
        
        return channel

通道控制
--------

``FmodChannel`` 代表一个正在播放的声音实例。

播放状态控制
~~~~~~~~~~~~

.. code-block:: gdscript

    func control_playback(channel: FmodChannel):
        # 暂停/继续
        channel.set_paused(true)
        channel.set_paused(false)
        
        # 停止
        channel.stop()
        
        # 检查播放状态
        if channel.is_playing():
            print("Channel is playing")

音量和音调
~~~~~~~~~~

.. code-block:: gdscript

    func adjust_audio(channel: FmodChannel) -> void:
        # Set volume in decibels
        channel.volume_db = -10.0 # -10 dB
        channel.volume_db = 0.0 # 0 dB (original volume)
        channel.volume_db = 6.0 # +6 dB (approximately double volume)
        
        # Set pitch
        channel.pitch = 1.0 # Normal pitch
        channel.pitch = 0.5 # Half speed (one octave down)
        channel.pitch = 2.0 # Double speed (one octave up)
        
        # Set pan
        channel.set_pan(-1.0) # Left only
        channel.set_pan(0.0) # Center
        channel.set_pan(1.0) # Right only

播放位置
~~~~~~~~

.. code-block:: gdscript

    func control_position(channel: FmodChannel) -> void:
        # Get current position in milliseconds
        var position_ms: int = channel.get_position(FmodChannel.TIMEUNIT_MS)
        
        # Jump to 30 seconds
        channel.set_position(30000, FmodChannel.TIMEUNIT_MS)
        
        # Get total length of the sound
        var sound: FmodSound = channel.get_current_sound()
        var length: float = sound.get_length()
        print("Total length: %.2f seconds" % length)

循环控制
~~~~~~~~

.. code-block:: gdscript

    func setup_looping(channel: FmodChannel) -> void:
        # Set infinite looping (-1 for infinite loops)
        channel.loop_count = -1
        
        # Set loop count (3 times)
        channel.loop_count = 3
        
        # Disable looping
        channel.loop_count = 0

3D 音频
-------

设置 3D 位置和属性
~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    extends Node3D

    @onready var player: FmodAudioStreamPlayer = $FmodAudioStreamPlayer

    func _ready() -> void:
        # Enable 3D mode on the sound
        var system: FmodSystem = FmodServer.main_system
        var sound: FmodSound = system.create_sound_from_file(
            "res://sfx/3d_sound.wav",
            FmodSystem.MODE_3D
        )
        
        # Get the channel and set 3D attributes
        var channel: FmodChannel = system.play_sound(sound, system.get_master_channel_group(), false)
        
        # Set position and velocity for 3D sound
        var pos: Vector3 = Vector3(10, 0, 5)
        channel.set_3d_attributes(pos, Vector3.ZERO)
        
        # Set distance attenuation
        channel.set_3d_min_max_distance(1.0, 100.0)
        channel.set_3d_level(1.0)

3D 监听器
~~~~~~~~~

.. code-block:: gdscript

    extends CharacterBody3D

    func _physics_process(_delta: float) -> void:
        # Update 3D listener attributes based on the player's position and orientation
        var system: FmodSystem = FmodServer.main_system
        system.set_3d_listener_attributes(
            0,
            global_position,
            velocity,
            -global_transform.basis.z,
            global_transform.basis.y
        )

最佳实践
--------

#. **使用节点播放背景音乐** - 便于场景管理
#. **使用 Emitter 播放音效** - 便于复用和批量管理
#. **及时释放资源** - 不再使用的 Channel 会自动释放
#. **合理使用通道组** - 按类型（音乐、音效、语音）分组管理
#. **3D 音频优化** - 设置合适的衰减距离，避免远距离计算

注意事项
--------

- 通道数量受 ``max_channels`` 限制
- 停止播放的通道会自动释放
- 3D 音频需要在创建声音时启用 ``MODE_3D``
- 音调变化会影响播放速度（以及音高）
