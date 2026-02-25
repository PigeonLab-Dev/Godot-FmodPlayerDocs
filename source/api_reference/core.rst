核心类 API
==========

FmodServer
----------

全局单例，管理 FMOD 系统的生命周期。

静态属性
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``singleton``
     - FmodServer
     - 全局单例实例
   * - ``main_system``
     - FmodSystem
     - 主 FMOD 系统实例

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``get_singleton()``
     - FmodServer
     - 获取单例实例
   * - ``get_main_system()``
     - FmodSystem
     - 获取主系统
   * - ``get_master_channel_group()``
     - FmodChannelGroup
     - 获取主通道组
   * - ``get_audio_bus_layout()``
     - FmodAudioBusLayout
     - 获取音频总线布局

示例
~~~~

.. code-block:: gdscript

    # 获取主系统
    var system = FmodServer.get_main_system()
    
    # 或者通过单例
    var server = FmodServer.get_singleton()
    var system = server.get_main_system()

FmodSystem
----------

FMOD::System 的包装类，负责创建声音、通道、DSP 等。

方法
~~~~

系统管理
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``init(max_channels, flags)``
     - bool
     - 初始化系统
   * - ``update()``
     - void
     - 更新系统（每帧自动调用）
   * - ``release()``
     - void
     - 释放系统资源
   * - "set_advanced_settings(settings)"
     - void
     - 设置高级参数

声音创建
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``create_sound_from_file(path, mode)``
     - FmodSound
     - 从文件创建声音
   * - ``create_sound_from_memory(data, mode)``
     - FmodSound
     - 从内存创建声音
   * - ``create_stream_from_file(path, mode)``
     - FmodSound
     - 创建流式声音

通道和组
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``play_sound(sound, group, paused)``
     - FmodChannel
     - 播放声音
   * - ``create_channel_group(name)``
     - FmodChannelGroup
     - 创建通道组
   * - ``get_master_channel_group()``
     - FmodChannelGroup
     - 获取主通道组
   * - ``get_channel_group_by_name(name)``
     - FmodChannelGroup
     - 通过名称获取通道组

DSP 创建
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``create_dsp_by_type(type)``
     - FmodDSP
     - 通过类型创建 DSP
   * - ``create_dsp_by_index(index)``
     - FmodDSP
     - 通过索引创建 DSP

状态查询
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``get_cpu_usage()``
     - Dictionary
     - 获取 CPU 使用率
   * - "get_channels_playing()"
     - Dictionary
     - 获取播放中的通道数
   * - ``get_memory_info()``
     - Dictionary
     - 获取内存使用信息

3D 音频
^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - "set_3d_listener_attributes(index, pos, vel, forward, up)"
     - void
     - 设置 3D 监听器属性
   * - ``set_3d_settings(doppler, distance, rolloff)``
     - void
     - 设置 3D 全局设置

常量
~~~~

加载模式
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 常量
     - 值
     - 说明
   * - ``MODE_DEFAULT``
     - 0x00000000
     - 默认模式
   * - "MODE_LOOP_OFF"
     - 0x00000001
     - 不循环
   * - ``MODE_LOOP_NORMAL``
     - 0x00000002
     - 正常循环
   * - ``MODE_3D``
     - 0x00000010
     - 3D 声音
   * - ``MODE_CREATESAMPLE``
     - 0x00000100
     - 创建采样
   * - ``MODE_CREATESTREAM``
     - 0x00000200
     - 创建流
   * - ``MODE_NONBLOCKING``
     - 0x00010000
     - 非阻塞加载

示例
~~~~

.. code-block:: gdscript

    var system = FmodServer.main_system
    
    # 创建声音
    var sound = system.create_sound_from_file(
        "res://music.mp3",
        FmodSystem.MODE_LOOP_NORMAL | FmodSystem.MODE_CREATESTREAM
    )
    
    # 播放
    var channel = system.play_sound(sound, null, false)
    
    # 获取性能信息
    var cpu = system.get_cpu_usage()
    print("DSP: %.2f%%" % cpu["dsp"])
