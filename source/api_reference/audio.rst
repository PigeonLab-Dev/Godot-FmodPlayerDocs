音频资源 API
============

FmodAudioStream
---------------

继承自：Resource

流式音频资源类，适合播放大型音频文件。

属性
~~~~

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
     - 原始音频数据
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
   * - ``set_file_path(path)``
     - void
     - 设置文件路径
   * - ``get_file_path()``
     - String
     - 获取文件路径
   * - ``get_sound()``
     - FmodSound
     - 获取 FMOD 声音对象
   * - ``get_length()``
     - float
     - 获取音频长度（秒）

示例
~~~~

.. code-block:: gdscript

    var stream = FmodAudioStream.new()
    stream.file_path = "res://music/background.mp3"
    
    var length = stream.get_length()
    print("Duration: %.2f seconds" % length)

FmodAudioSample
---------------

继承自：Resource

采样音频资源类，完全加载到内存，适合音效。

属性
~~~~

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
     - 原始音频数据
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
   * - "set_file_path(path)"
     - void
     - 设置文件路径
   * - ``get_file_path()``
     - String
     - 获取文件路径
   * - ``get_sound()``
     - FmodSound
     - 获取 FMOD 声音对象
   * - ``get_length()``
     - float
     - 获取音频长度（秒）

示例
~~~~

.. code-block:: gdscript

    var sample = FmodAudioSample.new()
    sample.file_path = "res://sfx/explosion.wav"
    
    var emitter = $FmodAudioSampleEmitter
    emitter.sample = sample
    emitter.play()

FmodSound
---------

继承自：RefCounted

FMOD::Sound 的包装类，代表加载的音频数据。

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``load_from_file(path, mode)``
     - FmodSound
     - 静态方法，从文件加载
   * - ``get_name()``
     - String
     - 获取声音名称
   * - ``get_format()``
     - Dictionary
     - 获取格式信息
   * - ``get_length()``
     - double
     - 获取长度（秒）
   * - ``get_num_subsounds()``
     - int
     - 获取子声音数量
   * - ``get_subsound(index)``
     - FmodSound
     - 获取子声音
   * - ``release()``
     - void
     - 释放声音资源

示例
~~~~

.. code-block:: gdscript

    var system = FmodServer.main_system
    var sound = system.create_sound_from_file("res://music.mp3")
    
    var format = sound.get_format()
    print("Channels: %d" % format["channels"])
    print("Sample Rate: %d" % format["sample_rate"])
    print("Bits: %d" % format["bits"])

FmodAudioBus
------------

继承自：RefCounted

音频总线类，包装 FmodChannelGroup 提供更友好的接口。

属性
~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``bus_name``
     - String
     - 总线名称
   * - ``volume_db``
     - float
     - 音量（分贝）
   * - ``mute``
     - bool
     - 静音状态
   * - ``solo``
     - bool
     - 独奏状态

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``init_bus(name, parent)``
     - void
     - 初始化总线
   * - ``set_volume_db(volume)``
     - void
     - 设置音量
   * - ``get_volume_db()``
     - float
     - 获取音量
   * - ``set_mute(mute)``
     - void
     - 设置静音
   * - ``set_solo(solo)``
     - void
     - 设置独奏
   * - ``add_effect(effect, index)``
     - void
     - 添加效果器
   * - ``remove_effect(index)``
     - void
     - 移除效果器

FmodAudioBusLayout
------------------

继承自：Resource

音频总线布局类，管理所有音频总线的结构。

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``create_audio_bus(name, parent_name)``
     - FmodAudioBus
     - 创建音频总线
   * - ``get_audio_bus(name)``
     - FmodAudioBus
     - 通过名称获取总线
   * - ``remove_audio_bus(name)``
     - void
     - 移除音频总线
   * - ``sync_from_audio_server()``
     - void
     - 从 Godot AudioServer 同步
   * - ``add_bus_effect(bus_name, effect, index)``
     - void
     - 给总线添加效果

示例
~~~~

.. code-block:: gdscript

    var layout = FmodServer.get_audio_bus_layout()
    
    # 创建新总线
    var ui_bus = layout.create_audio_bus("UI", "Master")
    ui_bus.volume_db = -6.0
    
    # 获取现有总线
    var music_bus = layout.get_audio_bus("Music")
    music_bus.mute = false
