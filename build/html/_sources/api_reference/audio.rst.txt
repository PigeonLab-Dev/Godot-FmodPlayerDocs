音频资源 API
============

FmodAudioStream
---------------

继承自：Resource

音频流资源类，支持流式加载和内存加载两种模式，通过 ``mode_flags`` 控制加载行为。

枚举
~~~~

CreateMode
^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 枚举值
     - 值
     - 说明
   * - ``MODE_DEFAULT``
     - 0
     - 默认模式
   * - ``MODE_STREAM``
     - 1
     - 流式加载（从内存流式播放，适合大文件）
   * - ``MODE_SAMPLE``
     - 2
     - 样本模式（加载到内存，适合音效）
   * - ``MODE_LOOP``
     - 4
     - 循环播放
   * - ``MODE_LOOP_BIDI``
     - 8
     - 双向循环（ ping-pong 循环）

属性
~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``audio_data``
     - PackedByteArray
     - 音频数据（二进制）
   * - ``mode_flags``
     - int
     - 创建模式标志（组合使用 CreateMode 枚举）
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
   * - ``set_audio_data(data)``
     - void
     - 设置音频数据
   * - ``get_audio_data()``
     - PackedByteArray
     - 获取音频数据
   * - ``set_mode_flags(flags)``
     - void
     - 设置创建模式标志
   * - ``get_mode_flags()``
     - int
     - 获取创建模式标志
   * - ``add_mode_flag(flag)``
     - void
     - 添加单个模式标志
   * - ``remove_mode_flag(flag)``
     - void
     - 移除单个模式标志
   * - ``has_mode_flag(flag)``
     - bool
     - 检查是否包含某个模式标志
   * - ``get_sound()``
     - FmodSound
     - 获取 FMOD 声音对象（延迟创建）
   * - ``get_length()``
     - float
     - 获取音频长度（秒）
   * - ``clear()``
     - void
     - 清理音频数据和声音资源
   * - ``load_from_file(path, flags)`` (静态)
     - FmodAudioStream
     - 从文件加载音频，返回新的流实例

示例
~~~~

**从文件加载（流式模式 - 适合背景音乐）：**

.. code-block:: gdscript

    # 流式加载（默认）
    var stream = FmodAudioStream.load_from_file("res://music/background.mp3")
    stream.mode_flags = FmodAudioStream.MODE_STREAM | FmodAudioStream.MODE_LOOP
    
    var player = $FmodAudioStreamPlayer
    player.stream = stream
    player.play()

**从文件加载（样本模式 - 适合音效）：**

.. code-block:: gdscript

    # 样本模式加载到内存
    var sfx = FmodAudioStream.load_from_file("res://sfx/explosion.wav", 
        FmodAudioStream.MODE_SAMPLE)
    
    var emitter = $FmodAudioSampleEmitter
    emitter.stream = sfx
    emitter.emit()

**从内存加载：**

.. code-block:: gdscript

    var stream = FmodAudioStream.new()
    stream.audio_data = loaded_bytes
    stream.mode_flags = FmodAudioStream.MODE_SAMPLE

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
