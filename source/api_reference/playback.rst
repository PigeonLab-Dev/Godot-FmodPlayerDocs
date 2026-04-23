播放控制 API
============

.. _FmodChannelControl:

FmodChannelControl
------------------

继承自：RefCounted

通道控制的抽象基类，``FmodChannel`` 和 ``FmodChannelGroup`` 都继承自此类。

方法
~~~~

播放控制
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``is_playing()``
     - bool
     - 是否正在播放
   * - ``stop()``
     - void
     - 停止播放
   * - ``set_paused(paused)``
     - void
     - 设置暂停状态
   * - ``get_paused()``
     - bool
     - 获取暂停状态

音量控制
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_volume(volume)``
     - void
     - 设置音量（线性 0.0-1.0）
   * - ``get_volume()``
     - float
     - 获取音量（线性）
   * - ``set_volume_db(volume_db)``
     - void
     - 设置音量（分贝）
   * - ``get_volume_db()``
     - float
     - 获取音量（分贝）
   * - ``set_mute(mute)``
     - void
     - 设置静音
   * - ``get_mute()``
     - bool
     - 获取静音状态

音调和声像
^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_pitch(pitch)``
     - void
     - 设置音调（1.0 = 正常）
   * - ``get_pitch()``
     - float
     - 获取音调
   * - ``set_pan(pan)``
     - void
     - 设置声像（-1.0 ~ 1.0）
   * - ``get_pan()``
     - float
     - 获取声像

DSP 效果
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``add_dsp(index, dsp)``
     - void
     - 添加 DSP 效果器
   * - ``remove_dsp(dsp)``
     - void
     - 移除 DSP 效果器
   * - ``get_dsp(index)``
     - FmodDSP
     - 获取指定索引的 DSP
   * - ``get_num_dsps()``
     - int
     - 获取 DSP 数量

3D 属性
^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_3d_attributes(pos, vel)``
     - void
     - 设置 3D 位置和速度
   * - ``get_3d_attributes()``
     - Dictionary
     - 获取 3D 属性
   * - ``set_3d_min_max_distance(min, max)``
     - void
     - 设置 3D 最小/最大距离
   * - ``set_3d_level(level)``
     - void
     - 设置 3D 级别

.. _FmodChannel:

FmodChannel
-----------

继承自：FmodChannelControl

代表一个正在播放的声音实例。

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``setup(channel)``
     - void
     - 设置内部 FMOD 通道
   * - ``set_position(position, timeunit)``
     - void
     - 设置播放位置
   * - ``get_position(timeunit)``
     - int
     - 获取播放位置
   * - ``get_current_sound()``
     - FmodSound
     - 获取当前播放的声音
   * - ``set_loop_count(loopcount)``
     - void
     - 设置循环次数（-1=无限）
   * - ``get_loop_count()``
     - int
     - 获取循环次数
   * - ``set_channel_group(group)``
     - void
     - 设置所属通道组
   * - ``get_channel_group()``
     - FmodChannelGroup
     - 获取所属通道组

常量
~~~~

时间单位
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 常量
     - 值
     - 说明
   * - ``TIMEUNIT_MS``
     - 1
     - 毫秒
   * - ``TIMEUNIT_PCM``
     - 2
     - PCM 采样
   * - ``TIMEUNIT_PCMBYTES``
     - 4
     - PCM 字节

示例
~~~~

.. code-block:: gdscript

    var channel = system.play_sound(sound, null, false)
    
    # 设置音量和音调
    channel.set_volume_db(-6.0)
    channel.set_pitch(1.2)
    
    # 跳转到 30 秒处
    channel.set_position(30000, FmodChannel.TIMEUNIT_MS)
    
    # 设置无限循环
    channel.set_loop_count(-1)

.. _FmodChannelGroup:

FmodChannelGroup
----------------

继承自：FmodChannelControl

通道组，用于将多个通道组织在一起进行混音控制。

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - "setup(channel_group)"
     - void
     - 设置内部 FMOD 通道组
   * - ``add_group(group, propagatedspclock)``
     - void
     - 添加子组
   * - ``get_num_groups()``
     - int
     - 获取子组数量
   * - ``get_group(index)``
     - FmodChannelGroup
     - 获取指定子组
   * - ``get_num_channels()``
     - int
     - 获取通道数量
   * - ``get_channel(index)``
     - FmodChannel
     - 获取指定通道
   * - ``get_name()``
     - String
     - 获取组名称
   * - ``release()``
     - void
     - 释放通道组

示例
~~~~

.. code-block:: gdscript

    # 创建 SFX 组
    var sfx_group = system.create_channel_group("SFX")
    var master = system.get_master_channel_group()
    master.add_group(sfx_group)
    
    # 播放到 SFX 组
    var channel = system.play_sound(sound, sfx_group, false)
    
    # 控制整个组
    sfx_group.set_volume_db(-12.0)
    sfx_group.set_mute(true)
