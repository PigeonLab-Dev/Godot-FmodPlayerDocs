播放控制 API
============

.. _FmodChannelControl:

FmodChannelControl
------------------

继承自： `RefCounted`_

**Channel 和 ChannelGroup 的通用控制基类**

描述
~~~~

**FmodChannelControl** 封装 FMOD::ChannelControl 的共享能力，为 :ref:`FmodChannel<FmodChannel>` 和 :ref:`FmodChannelGroup<FmodChannelGroup>` 提供播放控制、音量、3D 空间化、声像矩阵、滤波、DSP 链和样本精确调度等功能。

该类主要作为基类使用，通常通过 :ref:`FmodChannel<FmodChannel>` 或 :ref:`FmodChannelGroup<FmodChannelGroup>` 获取实例。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `bool`_
    - pasued
    - false
    - 暂停状态。注意当前绑定名称为 ``pasued``，方法名仍为 :ref:`set_paused()<FmodChannelControl-set_paused>` / :ref:`get_paused()<FmodChannelControl-get_paused>`
  * - `float`_
    - pitch
    - 1.0
    - 相对音高和播放速率
  * - `float`_
    - volume_db
    - 0.0
    - 音量，单位为分贝
  * - `bool`_
    - volume_ramp
    - false
    - 音量变化是否使用平滑斜坡
  * - `bool`_
    - mute
    - false
    - 静音状态
  * - ``PackedVector3Array``
    - 3d_custom_rolloff
    - PackedVector3Array()
    - 自定义 3D 距离衰减曲线
  * - `float`_
    - 3d_doppler_level
    - 1.0
    - 多普勒效果缩放量
  * - `float`_
    - 3d_level
    - 1.0
    - 3D 平移与 2D 平移之间的混合比例
  * - `float`_
    - 3d_min_distance
    - 1.0
    - 3D 距离衰减的最小距离
  * - `float`_
    - 3d_max_distance
    - 10000.0
    - 3D 距离衰减的最大距离
  * - `float`_
    - 3d_spread
    - 0.0
    - 3D 声音在扬声器空间中的扩散角度
  * - `float`_
    - gain
    - 1.0
    - 内置低通/距离滤波使用的干信号增益

信号
~~~~

.. list-table::
  :header-rows: 1

  * - 信号
    - 说明
  * - callback_received(type: `int`_)
    - 当 FMOD ChannelControl 回调触发时发出，``type`` 为回调类型。

方法
~~~~

有效性检查
^^^^^^^^^^

.. _FmodChannelControl-channel_control_is_valid:

`bool`_ channel_control_is_valid() const
++++++++++++++++++++++++++++++++++++++++

如果底层 FMOD::ChannelControl 句柄有效，则返回 ``true``。

.. _FmodChannelControl-channel_control_is_null:

`bool`_ channel_control_is_null() const
+++++++++++++++++++++++++++++++++++++++

如果底层 FMOD::ChannelControl 句柄为空或不可用，则返回 ``true``。

播放控制
^^^^^^^^

.. _FmodChannelControl-is_playing:

`bool`_ is_playing() const
++++++++++++++++++++++++++

返回该 Channel 或 ChannelGroup 当前是否正在播放。

.. _FmodChannelControl-stop:

void stop()
+++++++++++

停止该 Channel 的播放，或停止嵌套在 ChannelGroup 中的所有 Channel。

.. _FmodChannelControl-set_paused:

void set_paused(paused: `bool`_)
++++++++++++++++++++++++++++++++

设置暂停状态。``true`` 会暂停播放，``false`` 会恢复播放。

.. _FmodChannelControl-get_paused:

`bool`_ get_paused() const
++++++++++++++++++++++++++

返回当前暂停状态。

.. _FmodChannelControl-set_mode:

void set_mode(mode: :ref:`FmodMode<FmodMode>`)
++++++++++++++++++++++++++++++++++++++++++++++

设置 FMOD 播放模式标志，用于控制循环、2D/3D、距离衰减等行为。

.. _FmodChannelControl-get_mode:

:ref:`FmodMode<FmodMode>` get_mode() const
++++++++++++++++++++++++++++++++++++++++++

返回当前播放模式标志。

.. _FmodChannelControl-set_pitch:

void set_pitch(pitch: `float`_)
+++++++++++++++++++++++++++++++

设置相对音高和播放速率。``1.0`` 为原始音高，``2.0`` 为两倍速，``0.5`` 为半速。

.. _FmodChannelControl-get_pitch:

`float`_ get_pitch() const
++++++++++++++++++++++++++

返回当前相对音高和播放速率。

音量控制
^^^^^^^^

.. _FmodChannelControl-get_audibility:

`float`_ get_audibility() const
+++++++++++++++++++++++++++++++

返回综合音量、静音、3D 衰减和父级混音后的最终可听度。

.. _FmodChannelControl-set_volume_db:

void set_volume_db(volume: `float`_)
++++++++++++++++++++++++++++++++++++

设置音量，单位为分贝。

.. _FmodChannelControl-get_volume_db:

`float`_ get_volume_db() const
++++++++++++++++++++++++++++++

返回当前音量，单位为分贝。

.. _FmodChannelControl-set_volume_ramp:

void set_volume_ramp(ramp: `bool`_)
+++++++++++++++++++++++++++++++++++

设置音量变化是否使用 FMOD 的平滑斜坡。启用后可减少突然变更音量时的爆音。

.. _FmodChannelControl-get_volume_ramp:

`bool`_ get_volume_ramp() const
+++++++++++++++++++++++++++++++

返回音量变化是否使用平滑斜坡。

.. _FmodChannelControl-set_mute:

void set_mute(mute: `bool`_)
++++++++++++++++++++++++++++

设置静音状态。

.. _FmodChannelControl-get_mute:

`bool`_ get_mute() const
++++++++++++++++++++++++

返回当前静音状态。

空间化
^^^^^^

.. _FmodChannelControl-set_3d_attributes:

void set_3d_attributes(pos: `Vector3`_, vel: `Vector3`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置 3D 位置和速度，用于平移、距离衰减和多普勒计算。

.. _FmodChannelControl-get_3d_attributes:

`Dictionary`_ get_3d_attributes() const
+++++++++++++++++++++++++++++++++++++++

返回 3D 属性字典，包含 ``pos`` 和 ``vel``。

.. _FmodChannelControl-set_3d_cone_orientation:

void set_3d_cone_orientation(orientation: `Vector3`_)
+++++++++++++++++++++++++++++++++++++++++++++++++++++

设置 3D 声音锥体方向，用于方向性遮挡和衰减。

.. _FmodChannelControl-get_3d_cone_orientation:

`Vector3`_ get_3d_cone_orientation() const
++++++++++++++++++++++++++++++++++++++++++

返回当前 3D 声音锥体方向。

.. _FmodChannelControl-set_3d_cone_settings:

void set_3d_cone_settings(inside_cone_angle: `float`_, outside_cone_angle: `float`_, outside_volume_db: `float`_)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置方向性 3D 声音锥体的内角、外角和外部音量衰减。

.. _FmodChannelControl-get_3d_cone_settings:

`Dictionary`_ get_3d_cone_settings() const
++++++++++++++++++++++++++++++++++++++++++

返回锥体设置字典，包含 ``inside_cone_angle``、``outside_cone_angle`` 和 ``outside_volume_db``。

.. _FmodChannelControl-set_3d_custom_rolloff:

void set_3d_custom_rolloff(points: ``PackedVector3Array``)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置自定义 3D 距离衰减曲线。通常需要配合 ``FMOD_MODE_3D_CUSTOMROLLOFF`` 使用。

.. _FmodChannelControl-get_3d_custom_rolloff:

``PackedVector3Array`` get_3d_custom_rolloff() const
++++++++++++++++++++++++++++++++++++++++++++++++++++

返回当前自定义 3D 距离衰减曲线。

.. _FmodChannelControl-set_3d_distance_filter:

void set_3d_distance_filter(custom: `bool`_, custom_level: `float`_, center_freq: `float`_)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置 3D 距离滤波器覆盖值，用于随距离改变低通/高通滤波表现。

.. _FmodChannelControl-get_3d_distance_filter:

`Dictionary`_ get_3d_distance_filter() const
++++++++++++++++++++++++++++++++++++++++++++

返回距离滤波器设置字典，包含 ``custom``、``custom_level`` 和 ``center_freq``。

.. _FmodChannelControl-set_3d_doppler_level:

void set_3d_doppler_level(level: `float`_)
++++++++++++++++++++++++++++++++++++++++++

设置多普勒效果缩放量。该功能主要用于 Channel。

.. _FmodChannelControl-get_3d_doppler_level:

`float`_ get_3d_doppler_level() const
+++++++++++++++++++++++++++++++++++++

返回多普勒效果缩放量。

.. _FmodChannelControl-set_3d_level:

void set_3d_level(level: `float`_)
++++++++++++++++++++++++++++++++++

设置 3D 平移与 2D 平移之间的混合比例。

.. _FmodChannelControl-get_3d_level:

`float`_ get_3d_level() const
+++++++++++++++++++++++++++++

返回 3D 平移与 2D 平移之间的混合比例。

.. _FmodChannelControl-set_3d_min_distance:

void set_3d_min_distance(min: `float`_)
+++++++++++++++++++++++++++++++++++++++

设置 3D 距离衰减开始前的最小距离。

.. _FmodChannelControl-get_3d_min_distance:

`float`_ get_3d_min_distance() const
++++++++++++++++++++++++++++++++++++

返回 3D 距离衰减的最小距离。

.. _FmodChannelControl-set_3d_max_distance:

void set_3d_max_distance(max: `float`_)
+++++++++++++++++++++++++++++++++++++++

设置 3D 距离衰减的最大距离。

.. _FmodChannelControl-get_3d_max_distance:

`float`_ get_3d_max_distance() const
++++++++++++++++++++++++++++++++++++

返回 3D 距离衰减的最大距离。

.. _FmodChannelControl-set_3d_occlusion:

void set_3d_occlusion(direct_occlusion: `float`_, reverb_occlusion: `float`_)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置直接声和混响路径的遮挡衰减因子，范围通常为 ``0.0`` 到 ``1.0``。

.. _FmodChannelControl-get_3d_occlusion:

`Dictionary`_ get_3d_occlusion() const
++++++++++++++++++++++++++++++++++++++

返回遮挡字典，包含 ``direct_occlusion`` 和 ``reverb_occlusion``。

.. _FmodChannelControl-set_3d_spread:

void set_3d_spread(angle: `float`_)
+++++++++++++++++++++++++++++++++++

设置 3D 声音在扬声器空间中的扩散角度。

.. _FmodChannelControl-get_3d_spread:

`float`_ get_3d_spread() const
++++++++++++++++++++++++++++++

返回 3D 声音扩散角度。

声像与电平
^^^^^^^^^^

.. _FmodChannelControl-set_pan:

void set_pan(pan: `float`_)
+++++++++++++++++++++++++++

设置左右声像。``-1.0`` 为左，``0.0`` 为中间，``1.0`` 为右。

.. _FmodChannelControl-set_mix_levels_input:

void set_mix_levels_input(levels: ``PackedFloat32Array``)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

为多声道输入信号的每个输入通道设置电平。该功能主要用于 Channel。

.. _FmodChannelControl-set_mix_levels_output:

void set_mix_levels_output(front_left: `float`_, front_right: `float`_, center: `float`_, lfe: `float`_, surround_left: `float`_, surround_right: `float`_, back_left: `float`_, back_right: `float`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

为每个输出扬声器设置音量电平。

.. _FmodChannelControl-set_mix_matrix:

void set_mix_matrix(matrix: ``PackedFloat32Array``, outchannels: `int`_, inchannels: `int`_, inchannel_hop: `int`_ = 0)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置二维声像矩阵，将输入通道列映射到输出扬声器行。``matrix`` 的长度应至少覆盖 ``outchannels * inchannel_hop``，当 ``inchannel_hop`` 为 ``0`` 时使用 ``inchannels``。

.. _FmodChannelControl-get_mix_matrix:

`Dictionary`_ get_mix_matrix() const
++++++++++++++++++++++++++++++++++++

返回当前混音矩阵信息，包含矩阵数据、输出通道数、输入通道数和输入通道步长。

过滤
^^^^

.. _FmodChannelControl-set_reverb_properties:

void set_reverb_properties(instance: `int`_, wet: `float`_)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置指定全局混响实例的发送电平。

.. _FmodChannelControl-get_reverb_properties:

`float`_ get_reverb_properties(instance: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回指定全局混响实例的发送电平。

.. _FmodChannelControl-set_low_pass_gain:

void set_low_pass_gain(gain: `float`_)
++++++++++++++++++++++++++++++++++++++

设置内置低通/距离滤波应用时干信号的增益。

.. _FmodChannelControl-get_low_pass_gain:

`float`_ get_low_pass_gain() const
++++++++++++++++++++++++++++++++++

返回内置低通/距离滤波应用时干信号的增益。

DSP 链配置
^^^^^^^^^^

.. _FmodChannelControl-add_dsp:

void add_dsp(index: `int`_, dsp: :ref:`FmodDSP<FmodDSP>`)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

在 DSP 链指定索引处插入一个 DSP 单元。

.. _FmodChannelControl-remove_dsp:

void remove_dsp(dsp: :ref:`FmodDSP<FmodDSP>`)
+++++++++++++++++++++++++++++++++++++++++++++

从 DSP 链中移除指定 DSP 单元。

.. _FmodChannelControl-get_num_dsps:

`int`_ get_num_dsps() const
+++++++++++++++++++++++++++

返回 DSP 链中的 DSP 单元数量。

.. _FmodChannelControl-get_dsp:

:ref:`FmodDSP<FmodDSP>` get_dsp(index: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++

返回 DSP 链中指定索引处的 DSP 单元。

.. _FmodChannelControl-set_dsp_index:

void set_dsp_index(dsp: :ref:`FmodDSP<FmodDSP>`, index: `int`_)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置指定 DSP 单元在 DSP 链中的索引。

.. _FmodChannelControl-get_dsp_index:

`int`_ get_dsp_index(dsp: :ref:`FmodDSP<FmodDSP>`) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回指定 DSP 单元在 DSP 链中的索引。

样本精准排程
^^^^^^^^^^^^

.. _FmodChannelControl-get_dsp_clock:

`Dictionary`_ get_dsp_clock() const
+++++++++++++++++++++++++++++++++++

返回当前 DSP 时钟信息，通常包含当前时钟和父级时钟。

.. _FmodChannelControl-set_delay:

void set_delay(start: `int`_, end: `int`_, stopchannels: `bool`_ = true)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置相对于父 ChannelGroup DSP 时钟的样本精确开始和停止时间。

.. _FmodChannelControl-get_delay:

`Dictionary`_ get_delay() const
+++++++++++++++++++++++++++++++

返回样本精确延迟设置，包含开始、结束时钟和停止行为。

.. _FmodChannelControl-add_fade_point:

void add_fade_point(dspclock: `int`_, volume: `float`_)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

在指定 DSP 时钟处添加一个音量淡变点。

.. _FmodChannelControl-set_fade_point_ramp:

void set_fade_point_ramp(dspclock: `int`_, volume: `float`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

添加从当前音量到指定 DSP 时钟音量的淡变斜坡。

.. _FmodChannelControl-remove_fade_points:

void remove_fade_points(start: `int`_, end: `int`_)
+++++++++++++++++++++++++++++++++++++++++++++++++++

移除两个 DSP 时钟值之间的所有淡变点。

.. _FmodChannelControl-get_fade_points:

`Dictionary`_ get_fade_points() const
+++++++++++++++++++++++++++++++++++++

返回当前存储的淡变点信息。

回调
^^^^

.. _FmodChannelControl-set_callback:

void set_callback()
+++++++++++++++++++

设置 ChannelControl 级别的 FMOD 回调，并通过 ``callback_received`` 信号转发回 Godot。

.. _FmodChannelControl-clear_callback:

void clear_callback()
+++++++++++++++++++++

清除 ChannelControl 回调。

.. _FmodChannelControl-_on_callback:

void _on_callback(controltype: `int`_, callbacktype: `int`_, commanddata1: `int`_, commanddata2: `int`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

C++ 子类可重写的回调处理函数。GDScript 通常使用 ``callback_received`` 信号，而不是直接调用该方法。

.. _FmodChannel:

FmodChannel
-----------

继承自： :ref:`FmodChannelControl<FmodChannelControl>`

**单个播放通道的控制对象**

描述
~~~~

**FmodChannel** 表示 FMOD 中一次实际或虚拟的声音播放实例。它继承 :ref:`FmodChannelControl<FmodChannelControl>` 的通用控制能力，并额外提供播放频率、优先级、播放位置、循环点、所属 ChannelGroup、当前声音和通道索引等接口。

方法
~~~~

内部设置
^^^^^^^^

.. _FmodChannel-setup:

void setup(channel: `int`_)
+++++++++++++++++++++++++++

绑定底层 FMOD::Channel 指针。该方法主要供扩展内部使用。

有效性检查
^^^^^^^^^^

.. _FmodChannel-channel_is_valid:

`bool`_ channel_is_valid() const
++++++++++++++++++++++++++++++++

如果底层 FMOD::Channel 句柄有效，则返回 ``true``。

.. _FmodChannel-channel_is_null:

`bool`_ channel_is_null() const
+++++++++++++++++++++++++++++++

如果底层 FMOD::Channel 句柄为空或不可用，则返回 ``true``。

播放参数
^^^^^^^^

.. _FmodChannel-set_frequency:

void set_frequency(frequency: `float`_)
+++++++++++++++++++++++++++++++++++++++

设置播放频率，单位为赫兹。改变频率会影响播放速度和音高。

.. _FmodChannel-get_frequency:

`float`_ get_frequency() const
++++++++++++++++++++++++++++++

返回当前播放频率，单位为赫兹。

.. _FmodChannel-set_priority:

void set_priority(priority: `int`_)
+++++++++++++++++++++++++++++++++++

设置虚拟语音排序优先级。数值越低优先级越高。

.. _FmodChannel-get_priority:

`int`_ get_priority() const
+++++++++++++++++++++++++++

返回当前虚拟语音排序优先级。

.. _FmodChannel-set_position:

void set_position(position: `int`_, timeunit: :ref:`FmodTimeUnit<FmodTimeUnit>` = FMOD_TIME_UNIT_MS)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置当前播放位置。默认使用毫秒时间单位。

.. _FmodChannel-get_position:

`int`_ get_position(timeunit: :ref:`FmodTimeUnit<FmodTimeUnit>` = FMOD_TIME_UNIT_MS) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回当前播放位置。默认使用毫秒时间单位。

.. _FmodChannel-set_channel_group:

void set_channel_group(channel_group: :ref:`FmodChannelGroup<FmodChannelGroup>`)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置该 Channel 输出到的 ChannelGroup。

.. _FmodChannel-get_channel_group:

:ref:`FmodChannelGroup<FmodChannelGroup>` get_channel_group() const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回该 Channel 当前输出到的 ChannelGroup。

.. _FmodChannel-set_loop_count:

void set_loop_count(loop_count: `int`_)
+++++++++++++++++++++++++++++++++++++++

设置停止前的循环次数。``-1`` 通常表示无限循环。

.. _FmodChannel-get_loop_count:

`int`_ get_loop_count() const
+++++++++++++++++++++++++++++

返回停止前的循环次数。

.. _FmodChannel-set_loop_points:

void set_loop_points(start: `int`_, end: `int`_, timeunit: :ref:`FmodTimeUnit<FmodTimeUnit>` = FMOD_TIME_UNIT_MS)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置循环起点和终点。

.. _FmodChannel-get_loop_points:

`Dictionary`_ get_loop_points(timeunit: :ref:`FmodTimeUnit<FmodTimeUnit>` = FMOD_TIME_UNIT_MS) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回循环点字典，包含 ``start`` 和 ``end``。

状态与信息
^^^^^^^^^^

.. _FmodChannel-is_virtual:

`bool`_ is_virtual() const
++++++++++++++++++++++++++

返回该 Channel 是否当前由 FMOD 虚拟语音系统模拟。

.. _FmodChannel-get_current_sound:

:ref:`FmodSound<FmodSound>` get_current_sound() const
+++++++++++++++++++++++++++++++++++++++++++++++++++++

返回该 Channel 当前播放的声音。

.. _FmodChannel-get_index:

`int`_ get_index() const
++++++++++++++++++++++++

返回该 Channel 在 FMOD 系统通道池中的索引。

.. _FmodChannel-_on_callback:

void _on_callback(controltype: `int`_, callbacktype: `int`_, commanddata1: `int`_, commanddata2: `int`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

处理 Channel 级别 FMOD 回调的 C++ 重写函数。

.. _FmodChannelGroup:

FmodChannelGroup
----------------

继承自： :ref:`FmodChannelControl<FmodChannelControl>`

**用于组织和混合多个 Channel 的通道组**

描述
~~~~

**FmodChannelGroup** 表示 FMOD 的 ChannelGroup，可作为多个 Channel 或子 ChannelGroup 的输入目标。它继承通用的播放、音量、DSP 和调度控制能力，适合用于分组混音、总线式控制和批量停止声音。

方法
~~~~

内部设置
^^^^^^^^

.. _FmodChannelGroup-setup:

void setup(channel_group: `int`_)
+++++++++++++++++++++++++++++++++

绑定底层 FMOD::ChannelGroup 指针。该方法主要供扩展内部使用。

有效性检查
^^^^^^^^^^

.. _FmodChannelGroup-channel_group_is_valid:

`bool`_ channel_group_is_valid() const
++++++++++++++++++++++++++++++++++++++

如果底层 FMOD::ChannelGroup 句柄有效，则返回 ``true``。

.. _FmodChannelGroup-channel_group_is_null:

`bool`_ channel_group_is_null() const
+++++++++++++++++++++++++++++++++++++

如果底层 FMOD::ChannelGroup 句柄为空或不可用，则返回 ``true``。

Channel 管理
^^^^^^^^^^^^

.. _FmodChannelGroup-get_num_channels:

`int`_ get_num_channels() const
+++++++++++++++++++++++++++++++

返回汇入该组的 Channel 数量。

.. _FmodChannelGroup-get_channel:

:ref:`FmodChannel<FmodChannel>` get_channel(index: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回指定索引处的 Channel。

ChannelGroup 管理
^^^^^^^^^^^^^^^^^

.. _FmodChannelGroup-add_group:

void add_group(channel_group: :ref:`FmodChannelGroup<FmodChannelGroup>`, propagatedspclock: `bool`_ = true)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

将另一个 ChannelGroup 添加为当前组的输入。``propagatedspclock`` 控制是否传播 DSP 时钟。

.. _FmodChannelGroup-get_num_groups:

`int`_ get_num_groups() const
+++++++++++++++++++++++++++++

返回汇入该组的子 ChannelGroup 数量。

.. _FmodChannelGroup-get_group:

:ref:`FmodChannelGroup<FmodChannelGroup>` get_group(index: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回组输入列表中指定索引处的 ChannelGroup。

.. _FmodChannelGroup-get_parent_group:

:ref:`FmodChannelGroup<FmodChannelGroup>` get_parent_group() const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回当前 ChannelGroup 输出到的父 ChannelGroup。

概述
^^^^

.. _FmodChannelGroup-get_name:

`String`_ get_name() const
++++++++++++++++++++++++++

返回创建该 ChannelGroup 时使用的名称。

.. _FmodChannelGroup-release:

void release()
++++++++++++++

释放 ChannelGroup。释放后底层句柄不应继续使用。

.. _FmodSoundGroup:

FmodSoundGroup
--------------

继承自： `RefCounted`_

**用于限制和管理一组 FmodSound 播放行为的对象**

描述
~~~~

**FmodSoundGroup** 封装 FMOD::SoundGroup，可为一组声音设置最大同时可听数量、超出限制时的处理策略、静音淡出速度和整体音量。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `int`_
    - max_audible
    - -1
    - 同时可听到的最大播放数量
  * - :ref:`Behavior<FmodSoundGroup-Behavior>`
    - max_audible_behavior
    - BEHAVIOR_FAIL
    - 超过最大可听数量时的处理方式
  * - `float`_
    - mute_fade_speed
    - 0.0
    - 静音淡入淡出速度
  * - `float`_
    - volume_db
    - 0.0
    - SoundGroup 音量，单位为分贝

方法
~~~~

有效性检查
^^^^^^^^^^

.. _FmodSoundGroup-sound_group_is_valid:

`bool`_ sound_group_is_valid() const
++++++++++++++++++++++++++++++++++++

如果底层 FMOD::SoundGroup 句柄有效，则返回 ``true``。

.. _FmodSoundGroup-sound_group_is_null:

`bool`_ sound_group_is_null() const
+++++++++++++++++++++++++++++++++++

如果底层 FMOD::SoundGroup 句柄为空或不可用，则返回 ``true``。

内部设置
^^^^^^^^

.. _FmodSoundGroup-setup:

void setup(sound_group: `int`_)
+++++++++++++++++++++++++++++++

绑定底层 FMOD::SoundGroup 指针。该方法主要供扩展内部使用。

基础功能
^^^^^^^^

.. _FmodSoundGroup-set_max_audible:

void set_max_audible(max_audible: `int`_)
+++++++++++++++++++++++++++++++++++++++++

设置 SoundGroup 中同时可听到的最大播放数量。

.. _FmodSoundGroup-get_max_audible:

`int`_ get_max_audible() const
++++++++++++++++++++++++++++++

返回 SoundGroup 中同时可听到的最大播放数量。

.. _FmodSoundGroup-set_max_audible_behavior:

void set_max_audible_behavior(behavior: :ref:`Behavior<FmodSoundGroup-Behavior>`)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置超过最大可听数量时的处理方式。

.. _FmodSoundGroup-get_max_audible_behavior:

:ref:`Behavior<FmodSoundGroup-Behavior>` get_max_audible_behavior() const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回超过最大可听数量时的处理方式。

.. _FmodSoundGroup-set_mute_fade_speed:

void set_mute_fade_speed(speed: `float`_)
+++++++++++++++++++++++++++++++++++++++++

设置因最大可听数量限制而静音或恢复时的淡变速度。

.. _FmodSoundGroup-get_mute_fade_speed:

`float`_ get_mute_fade_speed() const
++++++++++++++++++++++++++++++++++++

返回静音淡变速度。

.. _FmodSoundGroup-set_volume_db:

void set_volume_db(volume_db: `float`_)
+++++++++++++++++++++++++++++++++++++++

设置 SoundGroup 音量，单位为分贝。

.. _FmodSoundGroup-get_volume_db:

`float`_ get_volume_db() const
++++++++++++++++++++++++++++++

返回 SoundGroup 音量，单位为分贝。

音效功能
^^^^^^^^

.. _FmodSoundGroup-get_num_sounds:

`int`_ get_num_sounds() const
+++++++++++++++++++++++++++++

返回 SoundGroup 中包含的 FmodSound 数量。

.. _FmodSoundGroup-get_sound:

:ref:`FmodSound<FmodSound>` get_sound(index: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回 SoundGroup 中指定索引处的 FmodSound。

.. _FmodSoundGroup-get_num_playing:

`int`_ get_num_playing() const
++++++++++++++++++++++++++++++

返回 SoundGroup 当前正在播放的 Channel 数量。

.. _FmodSoundGroup-stop:

void stop()
+++++++++++

停止 SoundGroup 中所有正在播放的声音。

概述
^^^^

.. _FmodSoundGroup-get_name:

`String`_ get_name() const
++++++++++++++++++++++++++

返回 SoundGroup 的名称。

.. _FmodSoundGroup-release:

void release()
++++++++++++++

释放 SoundGroup，并将其中的声音返回主 SoundGroup。

枚举
~~~~

.. _FmodSoundGroup-Behavior:

Behavior
^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - BEHAVIOR_FAIL
    - 0
    - 调用播放接口时，如果超过最大可听数量则播放失败
  * - BEHAVIOR_MUTE
    - 1
    - 超出的声音从静音开始，直到有足够声音停止后再变得可听
  * - BEHAVIOR_STEAL_LOWEST
    - 2
    - 超出限制时抢占当前最安静的声音
  * - BEHAVIOR_MAX
    - 3
    - 行为枚举数量