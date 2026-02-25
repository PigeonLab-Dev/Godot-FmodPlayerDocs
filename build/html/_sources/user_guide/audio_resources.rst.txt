音频资源
========

Godot-FmodPlayer 提供两种音频资源类型，适用于不同的使用场景。

音频资源类型
------------

FmodAudioStream（流式音频）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

适合播放大型音频文件，如背景音乐、环境音效等。音频数据按需从磁盘流式读取，内存占用低。

**特点：**

- 内存效率高（只缓存少量数据）
- 适合长时间播放
- 支持无缝循环
- 可实时跳转播放位置

**创建方式：**

.. code-block:: gdscript

    var stream = FmodAudioStream.new()
    stream.file_path = "res://music/background.mp3"

FmodAudioSample（采样音频）
~~~~~~~~~~~~~~~~~~~~~~~~~~~

适合播放短音效，如按钮点击、爆炸声等。音频数据完全加载到内存，播放延迟低。

**特点：**

- 播放延迟极低
- 适合频繁触发
- 支持多实例同时播放
- 内存占用与文件大小成正比

**创建方式：**

.. code-block:: gdscript

    var sample = FmodAudioSample.new()
    sample.file_path = "res://sfx/explosion.wav"

加载模式对比
------------

.. list-table::
   :header-rows: 1

   * - 特性
     - FmodAudioStream
     - FmodAudioSample
   * - 内存占用
     - 低
     - 高（完整文件）
   * - 播放延迟
     - 较高
     - 极低
   * - 适用场景
     - 背景音乐、长音频
     - 音效、短音频
   * - 支持格式
     - 所有 FMOD 格式
     - 所有 FMOD 格式
   * - 循环支持
     - 是
     - 是

支持的音频格式
--------------

.. list-table::
   :header-rows: 1

   * - 格式
     - 扩展名
     - Stream
     - Sample
   * - MP3
     - .mp3
     - ✅
     - ✅
   * - WAV
     - .wav
     - ✅
     - ✅
   * - OGG Vorbis
     - .ogg
     - ✅
     - ✅
   * - FLAC
     - .flac
     - ✅
     - ✅
   * - MOD
     - .mod
     - ✅
     - ✅
   * - XM
     - .xm
     - ✅
     - ✅
   * - S3M
     - .s3m
     - ✅
     - ✅
   * - IT
     - .it
     - ✅
     - ✅
   * - MIDI
     - .mid
     - ✅
     - ✅
   * - AIFF
     - .aiff
     - ✅
     - ✅

资源加载方式
------------

从文件系统加载
~~~~~~~~~~~~~~

.. code-block:: gdscript

    # 使用 Godot 资源路径
    stream.file_path = "res://music/song.mp3"
    
    # 使用用户数据路径
    stream.file_path = "user://recordings/voice.wav"
    
    # 使用绝对路径（不推荐）
    stream.file_path = "C:/Music/song.mp3"

从内存加载
~~~~~~~~~~

.. code-block:: gdscript

    # 从 PackedByteArray 加载
    var audio_data: PackedByteArray = load_audio_from somewhere()
    sample.data = audio_data

资源属性
--------

公共属性
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``file_path``
     - String
     - 音频文件路径
   * - ``data``
     - PackedByteArray
     - 原始音频数据（内存加载）
   * - ``data_loaded``
     - bool
     - 数据是否已加载

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``get_sound()``
     - FmodSound
     - 获取 FMOD 声音对象
   * - ``get_length()``
     - float
     - 获取音频长度（秒）

使用示例
--------

背景音乐的流式播放
~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    extends Node

    @onready var bgm_player = $BGMPlayer
    var bgm_tracks: Array[FmodAudioStream] = []
    var current_track: int = 0

    func _ready():
        # 加载播放列表
        for i in range(3):
            var stream = FmodAudioStream.new()
            stream.file_path = "res://music/track_%d.mp3" % i
            bgm_tracks.append(stream)
        
        play_track(0)

    func play_track(index: int):
        current_track = index
        bgm_player.stream = bgm_tracks[index]
        bgm_player.play()
        
        # 监听播放结束
        # 注意：需要在 FmodAudioStreamPlayer 中设置 loop = false

音效池管理
~~~~~~~~~~

.. code-block:: gdscript

    extends Node

    var sfx_cache: Dictionary = {}

    func preload_sfx(sfx_name: String, path: String):
        var sample = FmodAudioSample.new()
        sample.file_path = path
        sfx_cache[sfx_name] = sample

    func play_sfx(sfx_name: String, bus: String = "SFX"):
        if not sfx_cache.has(sfx_name):
            push_error("SFX not found: " + sfx_name)
            return
        
        # 使用 emitter 播放
        var emitter = FmodAudioSampleEmitter.new()
        add_child(emitter)
        
        emitter.sample = sfx_cache[sfx_name]
        emitter.bus = bus
        emitter.play()
        
        # 播放完成后自动释放
        await get_tree().create_timer(5.0).timeout
        emitter.queue_free()

动态加载大文件
~~~~~~~~~~~~~~

.. code-block:: gdscript

    extends Node

    @onready var player = $FmodAudioStreamPlayer

    func load_and_play_large_file(path: String):
        # 创建加载线程避免卡顿
        var thread = Thread.new()
        thread.start(func():
            var stream = FmodAudioStream.new()
            stream.file_path = path
            
            # 返回主线程更新 UI
            call_deferred("_on_stream_loaded", stream)
        )

    func _on_stream_loaded(stream: FmodAudioStream):
        player.stream = stream
        player.play()

最佳实践
--------

#. **背景音乐使用 Stream** - 降低内存占用，支持大文件
#. **音效使用 Sample** - 确保低延迟播放
#. **预加载常用资源** - 在游戏启动时加载常用音效
#. **使用资源路径** - 优先使用 ``res://`` 路径，便于打包
#. **注意文件格式** - OGG 适合音乐，WAV 适合短音效

注意事项
--------

- 流式音频在播放期间文件必须保持可访问
- 采样音频会占用与文件大小相等的内存
- 某些格式（如 MIDI）可能需要额外配置
- 移动设备上注意流式音频的磁盘 I/O 消耗
