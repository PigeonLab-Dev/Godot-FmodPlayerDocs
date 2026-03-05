音频资源
========

Godot-FmodPlayer 使用统一的 ``FmodAudioStream`` 资源类来管理音频数据，通过不同的 **创建模式标志（CreateMode）** 来适应不同的使用场景。

音频资源类型
------------

FmodAudioStream
~~~~~~~~~~~~~~~

统一的音频资源类，支持流式和样本两种加载模式。

**创建模式标志：**

.. list-table::
   :header-rows: 1

   * - 标志
     - 说明
     - 适用场景
   * - ``MODE_STREAM``
     - 流式加载，数据按需从内存流式读取
     - 背景音乐、长音频、环境音效
   * - ``MODE_SAMPLE``
     - 样本模式，数据完全加载到内存
     - 音效、短音频、需要低延迟播放
   * - ``MODE_LOOP``
     - 循环播放标志
     - 需要循环的音频
   * - ``MODE_LOOP_BIDI``
     - 双向循环（乒乓循环）
     - 特殊循环效果

**流式模式（MODE_STREAM）特点：**

- 内存效率高（只缓存少量数据）
- 适合长时间播放
- 支持无缝循环
- 可实时跳转播放位置

**样本模式（MODE_SAMPLE）特点：**

- 播放延迟极低
- 适合频繁触发
- 支持多实例同时播放
- 内存占用与文件大小成正比

加载模式对比
------------

.. list-table::
   :header-rows: 1

   * - 特性
     - MODE_STREAM
     - MODE_SAMPLE
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
     - 支持情况
   * - MP3
     - .mp3
     - ✅
   * - WAV
     - .wav
     - ✅
   * - OGG Vorbis
     - .ogg
     - ✅
   * - FLAC
     - .flac
     - ✅
   * - MOD
     - .mod
     - ✅
   * - XM
     - .xm
     - ✅
   * - S3M
     - .s3m
     - ✅
   * - IT
     - .it
     - ✅
   * - MIDI
     - .mid
     - ✅
   * - AIFF
     - .aiff
     - ✅

资源加载方式
------------

从文件加载（推荐）
~~~~~~~~~~~~~~~~~~

使用静态方法 ``load_from_file()`` 从文件系统加载音频：

.. code-block:: gdscript

    # 流式加载 - 适合背景音乐（默认）
    var bgm_stream = FmodAudioStream.load_from_file("res://music/background.mp3")
    bgm_stream.mode_flags = FmodAudioStream.MODE_STREAM | FmodAudioStream.MODE_LOOP
    
    # 样本加载 - 适合音效
    var sfx_stream = FmodAudioStream.load_from_file("res://sfx/explosion.wav",
        FmodAudioStream.MODE_SAMPLE)

从内存加载
~~~~~~~~~~

.. code-block:: gdscript

    # 从 PackedByteArray 加载
    var audio_data: PackedByteArray = load_audio_from_somewhere()
    
    var stream = FmodAudioStream.new()
    stream.audio_data = audio_data
    stream.mode_flags = FmodAudioStream.MODE_SAMPLE

资源属性
--------

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``audio_data``
     - PackedByteArray
     - 原始音频数据（二进制）
   * - ``mode_flags``
     - int
     - 创建模式标志组合
   * - ``data_loaded``
     - bool
     - 数据是否已加载（只读）

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``get_sound()``
     - FmodSound
     - 获取 FMOD 声音对象（延迟创建）
   * - ``get_length()``
     - float
     - 获取音频长度（秒）
   * - ``clear()``
     - void
     - 清理音频数据和声音资源

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
        # 加载播放列表（流式模式）
        for i in range(3):
            var stream = FmodAudioStream.load_from_file(
                "res://music/track_%d.mp3" % i,
                FmodAudioStream.MODE_STREAM)
            bgm_tracks.append(stream)
        
        play_track(0)

    func play_track(index: int):
        current_track = index
        bgm_player.stream = bgm_tracks[index]
        bgm_player.play()

音效池管理
~~~~~~~~~~

.. code-block:: gdscript

    extends Node

    var sfx_cache: Dictionary = {}

    func preload_sfx(sfx_name: String, path: String):
        # 使用样本模式加载音效
        var stream = FmodAudioStream.load_from_file(path, 
            FmodAudioStream.MODE_SAMPLE)
        sfx_cache[sfx_name] = stream

    func play_sfx(sfx_name: String, bus: String = "SFX"):
        if not sfx_cache.has(sfx_name):
            push_error("SFX not found: " + sfx_name)
            return
        
        # 使用 emitter 播放
        var emitter = FmodAudioSampleEmitter.new()
        add_child(emitter)
        
        emitter.stream = sfx_cache[sfx_name]
        emitter.bus = bus
        emitter.emit()
        
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
            var stream = FmodAudioStream.load_from_file(path,
                FmodAudioStream.MODE_STREAM)
            
            # 返回主线程更新
            call_deferred("_on_stream_loaded", stream)
        )

    func _on_stream_loaded(stream: FmodAudioStream):
        player.stream = stream
        player.play()

循环播放设置
~~~~~~~~~~~~

.. code-block:: gdscript

    extends Node

    func setup_looping_music():
        var stream = FmodAudioStream.load_from_file("res://music/loop.mp3")
        
        # 设置循环模式
        stream.mode_flags = FmodAudioStream.MODE_STREAM | FmodAudioStream.MODE_LOOP
        
        # 或使用双向循环
        # stream.mode_flags = FmodAudioStream.MODE_STREAM | FmodAudioStream.MODE_LOOP_BIDI
        
        $MusicPlayer.stream = stream
        $MusicPlayer.play()

最佳实践
--------

#. **背景音乐使用 MODE_STREAM** - 降低内存占用，支持大文件
#. **音效使用 MODE_SAMPLE** - 确保低延迟播放
#. **预加载常用资源** - 在游戏启动时加载常用音效
#. **使用资源路径** - 优先使用 ``res://`` 路径，便于打包
#. **注意文件格式** - OGG 适合音乐，WAV 适合短音效
#. **及时清理资源** - 不再使用的音频调用 ``clear()`` 释放内存

注意事项
--------

- 流式音频在播放期间音频数据必须保持有效
- 样本音频会占用与文件大小相等的内存
- 某些格式（如 MIDI）可能需要额外配置
- 移动设备上注意流式音频的内存占用
