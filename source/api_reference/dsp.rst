DSP 效果器 API
==============

.. _FmodDSP:

FmodDSP
-------

继承自： `RefCounted`_

**FMOD::DSP 的低层级封装，用于数字信号处理和效果链连接**

描述
~~~~

**FmodDSP** 表示 FMOD DSP 单元。它既可以是 FMOD 内置效果，也可以由 :ref:`FmodAudioEffect<FmodAudioEffect>` 创建并挂到总线或 ChannelControl 的 DSP 链中。通过该类可以控制 DSP 激活状态、旁路状态、参数、输入输出连接、计量信息以及自定义回调。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `bool`_
    - active
    - false
    - DSP 是否处于激活状态
  * - `bool`_
    - bypass
    - false
    - DSP 是否被旁路

方法
~~~~

连接路由
^^^^^^^^

.. _FmodDSP-add_input:

:ref:`FmodDSPConnection<FmodDSPConnection>` add_input(target_dsp: :ref:`FmodDSP<FmodDSP>`, type: :ref:`FmodDSPConnectionType<FmodDSPConnectionType>` = DSPCONNECTION_TYPE_STANDARD)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

将 ``target_dsp`` 作为输入连接到当前 DSP，并返回连接对象。

.. _FmodDSP-get_input:

`Dictionary`_ get_input(index: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++

返回指定输入连接信息，通常包含输入 DSP 和连接对象。

.. _FmodDSP-get_output:

`Dictionary`_ get_output(index: `int`_) const
+++++++++++++++++++++++++++++++++++++++++++++

返回指定输出连接信息，通常包含输出 DSP 和连接对象。

.. _FmodDSP-get_num_inputs:

`int`_ get_num_inputs() const
+++++++++++++++++++++++++++++

返回输入连接数量。

.. _FmodDSP-get_num_outputs:

`int`_ get_num_outputs() const
++++++++++++++++++++++++++++++

返回输出连接数量。

.. _FmodDSP-disconnect_from:

void disconnect_from(target: :ref:`FmodDSP<FmodDSP>`, connection: :ref:`FmodDSPConnection<FmodDSPConnection>` = null)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

断开到指定 DSP 的连接。传入连接对象时只断开该连接。

.. _FmodDSP-disconnect_all:

void disconnect_all(inputs: `bool`_, outputs: `bool`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++

批量断开输入和/或输出连接。

通道格式与计量
^^^^^^^^^^^^^^

.. _FmodDSP-set_channel_format:

void set_channel_format(numchannels: `int`_, speakermode: `int`_)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置 DSP 输出通道数和扬声器模式。

.. _FmodDSP-get_channel_format:

`Dictionary`_ get_channel_format() const
++++++++++++++++++++++++++++++++++++++++

返回 DSP 当前通道格式信息。

.. _FmodDSP-get_output_channel_format:

`Dictionary`_ get_output_channel_format(inchannels: `int`_, inspeakermode: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

根据输入通道格式查询该 DSP 预计输出的通道格式。

.. _FmodDSP-set_metering_enabled:

void set_metering_enabled(input_enabled: `bool`_, output_enabled: `bool`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

启用或禁用 DSP 输入/输出电平计量。

.. _FmodDSP-get_metering_enabled:

`Dictionary`_ get_metering_enabled() const
++++++++++++++++++++++++++++++++++++++++++

返回输入和输出计量是否启用。

.. _FmodDSP-get_metering_info:

`Dictionary`_ get_metering_info() const
+++++++++++++++++++++++++++++++++++++++

返回电平计量信息，适合做音量表或频谱显示。

参数控制
^^^^^^^^

.. _FmodDSP-get_num_parameters:

`int`_ get_num_parameters() const
+++++++++++++++++++++++++++++++++

返回 DSP 暴露的参数数量。

.. _FmodDSP-get_parameter_info:

`Dictionary`_ get_parameter_info(index: `int`_) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++

返回指定参数的名称、标签、描述、类型、范围和默认值等信息。

.. _FmodDSP-get_data_parameter_index:

`int`_ get_data_parameter_index(data_type: :ref:`FmodDSPParameterDataType<FmodDSPParameterDataType>`) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

按 FMOD 数据参数类型查找参数索引。

.. list-table::
  :header-rows: 1

  * - 方法
    - 说明
  * - ``set_parameter_float(index, value)`` / ``get_parameter_float(index)``
    - 设置或获取浮点参数
  * - ``set_parameter_int(index, value)`` / ``get_parameter_int(index)``
    - 设置或获取整数参数
  * - ``set_parameter_bool(index, value)`` / ``get_parameter_bool(index)``
    - 设置或获取布尔参数
  * - ``set_parameter_data(index, data)`` / ``get_parameter_data(index)``
    - 设置或获取字节数据参数

状态与信息
^^^^^^^^^^

.. _FmodDSP-set_active:

void set_active(active: `bool`_)
++++++++++++++++++++++++++++++++

设置 DSP 激活状态。

.. _FmodDSP-get_active:

`bool`_ get_active() const
++++++++++++++++++++++++++

返回 DSP 是否激活。

.. _FmodDSP-set_bypass:

void set_bypass(bypass: `bool`_)
++++++++++++++++++++++++++++++++

设置 DSP 旁路状态。

.. _FmodDSP-get_bypass:

`bool`_ get_bypass() const
++++++++++++++++++++++++++

返回 DSP 是否被旁路。

.. _FmodDSP-set_wet_dry_mix:

void set_wet_dry_mix(prewet: `float`_, postwet: `float`_, dry: `float`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置 DSP 的湿/干混合比例。

.. _FmodDSP-get_wet_dry_mix:

`Dictionary`_ get_wet_dry_mix() const
+++++++++++++++++++++++++++++++++++++

返回湿/干混合设置。

.. _FmodDSP-get_idle:

`bool`_ get_idle() const
++++++++++++++++++++++++

如果 DSP 当前处于空闲状态，则返回 ``true``。

.. _FmodDSP-reset:

void reset()
++++++++++++

重置 DSP 内部状态。

.. _FmodDSP-release:

void release()
++++++++++++++

释放底层 DSP 资源。

.. _FmodDSP-get_type:

:ref:`FmodDSPType<FmodDSPType>` get_type() const
++++++++++++++++++++++++++++++++++++++++++++++++

返回 DSP 类型。

.. _FmodDSP-get_info:

`Dictionary`_ get_info() const
++++++++++++++++++++++++++++++

返回 DSP 概述信息，通常包括名称、版本、通道数和配置宽度等。

.. _FmodDSP-get_cpu_usage:

`Dictionary`_ get_cpu_usage() const
+++++++++++++++++++++++++++++++++++

返回 DSP 的 CPU 使用信息。

.. _FmodDSP-get_system_object:

:ref:`FmodSystem<FmodSystem>` get_system_object() const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回创建或拥有该 DSP 的 FMOD 系统对象。

回调
^^^^

自定义 DSP 可以通过 Callable 接收 FMOD 生命周期、处理和参数访问回调。每个回调都有对应的 ``set_*_callback(callback)`` 与 ``get_*_callback()`` 方法。

.. list-table::
  :header-rows: 1

  * - 回调组
    - 方法
    - 说明
  * - 生命周期
    - ``create``、``release``、``reset``
    - DSP 创建、释放和重置时调用
  * - 处理
    - ``read``、``process``、``shouldiprocess``、``setposition``
    - 音频读取、块处理、是否处理和播放位置变化
  * - 参数设置
    - ``setparam_float``、``setparam_int``、``setparam_bool``、``setparam_data``
    - 外部写入 DSP 参数时调用
  * - 参数读取
    - ``getparam_float``、``getparam_int``、``getparam_bool``、``getparam_data``
    - 外部读取 DSP 参数时调用

枚举
~~~~

.. _FmodDSPType:

FmodDSPType
^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - DSP_TYPE_UNKNOWN
    - 0
    - 通过非 FMOD 插件创建，类型未知
  * - DSP_TYPE_MIXER
    - 1
    - 不处理信号，仅用于混合输入
  * - DSP_TYPE_OSCILLATOR
    - 2
    - 振荡器，可生成正弦、方波、锯齿波、三角波或噪声
  * - DSP_TYPE_LOWPASS
    - 3
    - 共振低通滤波器，已弃用
  * - DSP_TYPE_ITLOWPASS
    - 4
    - Impulse Tracker 风格低通滤波器
  * - DSP_TYPE_HIGHPASS
    - 5
    - 共振高通滤波器，已弃用
  * - DSP_TYPE_ECHO
    - 6
    - 回声效果
  * - DSP_TYPE_FADER
    - 7
    - 音量缩放和声像控制
  * - DSP_TYPE_FLANGE
    - 8
    - 法兰效果
  * - DSP_TYPE_DISTORTION
    - 9
    - 失真效果
  * - DSP_TYPE_NORMALIZE
    - 10
    - 归一化或放大声音到指定水平
  * - DSP_TYPE_LIMITER
    - 11
    - 限制声音电平
  * - DSP_TYPE_PARAMEQ
    - 12
    - 参数均衡器，已弃用
  * - DSP_TYPE_PITCHSHIFT
    - 13
    - 在不改变速度的情况下调整音高
  * - DSP_TYPE_CHORUS
    - 14
    - 合唱效果
  * - DSP_TYPE_ITECHO
    - 15
    - Impulse Tracker 风格回声
  * - DSP_TYPE_COMPRESSOR
    - 16
    - 动态压缩器
  * - DSP_TYPE_SFXREVERB
    - 17
    - SFX 混响效果
  * - DSP_TYPE_LOWPASS_SIMPLE
    - 18
    - 简单低通滤波器
  * - DSP_TYPE_DELAY
    - 19
    - 多通道延迟效果
  * - DSP_TYPE_TREMOLO
    - 20
    - 颤音效果
  * - DSP_TYPE_SEND
    - 21
    - 将信号发送到返回 DSP
  * - DSP_TYPE_RETURN
    - 22
    - 接收多个发送 DSP 的信号
  * - DSP_TYPE_HIGHPASS_SIMPLE
    - 23
    - 简单高通滤波器
  * - DSP_TYPE_PAN
    - 24
    - 2D / 3D 声像与通道混合
  * - DSP_TYPE_THREE_EQ
    - 25
    - 三段均衡器
  * - DSP_TYPE_FFT
    - 26
    - FFT 频谱分析
  * - DSP_TYPE_LOUDNESS_METER
    - 27
    - 响度和真实峰值分析
  * - DSP_TYPE_CONVOLUTIONREVERB
    - 28
    - 卷积混响
  * - DSP_TYPE_CHANNELMIX
    - 29
    - 通道增益、通道分组与扬声器格式转换
  * - DSP_TYPE_TRANSCEIVER
    - 30
    - 全局槽位式发送和接收
  * - DSP_TYPE_OBJECTPAN
    - 31
    - 对象声像空间化
  * - DSP_TYPE_MULTIBAND_EQ
    - 32
    - 五段参数均衡器
  * - DSP_TYPE_MULTIBAND_DYNAMICS
    - 33
    - 多段动态处理，已弃用
  * - DSP_TYPE_MAX
    - 34
    - DSP 类型边界值
  * - DSP_TYPE_FORCEINT
    - 65536
    - 强制枚举以整型大小存储

.. _FmodDSPParameterDataType:

FmodDSPParameterDataType
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - DSP_PARAMETER_DATA_TYPE_USER
    - 0
    - 用户数据
  * - DSP_PARAMETER_DATA_TYPE_OVERALLGAIN
    - -1
    - 整体增益
  * - DSP_PARAMETER_DATA_TYPE_3DATTRIBUTES
    - -2
    - 单个 3D 属性结构
  * - DSP_PARAMETER_DATA_TYPE_SIDECHAIN
    - -3
    - 侧链数据
  * - DSP_PARAMETER_DATA_TYPE_FFT
    - -4
    - FFT 频谱数据
  * - DSP_PARAMETER_DATA_TYPE_3DATTRIBUTES_MULTI
    - -5
    - 多个 3D 属性结构
  * - DSP_PARAMETER_DATA_TYPE_ATTENUATION_RANGE
    - -6
    - 衰减范围
  * - DSP_PARAMETER_DATA_TYPE_DYNAMIC_RESPONSE
    - -7
    - 动态响应
  * - DSP_PARAMETER_DATA_TYPE_FINITE_LENGTH
    - -8
    - 有限长度信息

.. _FmodDSPConnection:

FmodDSPConnection
-----------------

继承自： `RefCounted`_

**DSP 节点之间的连接对象**

描述
~~~~

**FmodDSPConnection** 表示两个 :ref:`FmodDSP<FmodDSP>` 之间的一条连接。可以通过它调整连接混合电平、混音矩阵，并查询输入输出 DSP。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - mix
    - 0.0
    - 连接混合电平，单位为分贝

方法
~~~~

.. _FmodDSPConnection-set_mix:

void set_mix(volume_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置连接混合电平。

.. _FmodDSPConnection-get_mix:

`float`_ get_mix() const
^^^^^^^^^^^^^^^^^^^^^^^^

返回连接混合电平。

.. _FmodDSPConnection-set_mix_matrix:

void set_mix_matrix(matrix: `PackedFloat32Array`_, outchannels: `int`_, inchannels: `int`_, inchannel_hop: `int`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置连接的混音矩阵，用于自定义输入通道到输出通道的映射。

.. _FmodDSPConnection-get_mix_matrix:

`PackedFloat32Array`_ get_mix_matrix(outchannels: `int`_, inchannels: `int`_, inchannel_hop: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回连接的混音矩阵。

.. _FmodDSPConnection-get_input:

:ref:`FmodDSP<FmodDSP>` get_input() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回连接的输入 DSP。

.. _FmodDSPConnection-get_output:

:ref:`FmodDSP<FmodDSP>` get_output() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回连接的输出 DSP。

.. _FmodDSPConnection-get_type:

:ref:`FmodDSPConnectionType<FmodDSPConnectionType>` get_type() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回连接类型。

枚举
^^^^

.. _FmodDSPConnectionType:

FmodDSPConnectionType
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - DSPCONNECTION_TYPE_STANDARD
    - 0
    - 标准 DSP 连接
  * - DSPCONNECTION_TYPE_SIDECHAIN
    - 1
    - 侧链连接
  * - DSPCONNECTION_TYPE_SEND
    - 2
    - 发送连接
  * - DSPCONNECTION_TYPE_SEND_SIDECHAIN
    - 3
    - 侧链发送连接

.. _FmodAudioEffect:

FmodAudioEffect
---------------

继承自： `Resource`_

**可挂到 FmodAudioBus 的音频效果资源基类**

描述
~~~~

**FmodAudioEffect** 是所有 FMOD 音频效果资源的基类。它负责把效果创建出的 DSP 应用到 :ref:`FmodChannelGroup<FmodChannelGroup>`，并保存当前所属总线和 DSP 链。

方法
~~~~

.. _FmodAudioEffect-apply_to:

void apply_to(bus: :ref:`FmodChannelGroup<FmodChannelGroup>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

将效果应用到指定通道组。

.. _FmodAudioEffect-remove_from_bus:

void remove_from_bus(bus: :ref:`FmodChannelGroup<FmodChannelGroup>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从指定通道组移除此效果。

.. _FmodAudioEffect-get_bus:

:ref:`FmodChannelGroup<FmodChannelGroup>` get_bus() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前应用到的通道组。

.. _FmodAudioEffectAmplify:

FmodAudioEffectAmplify
----------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**简单增益效果，用于放大或衰减信号。**

描述
~~~~

**FmodAudioEffectAmplify** 会在总线效果链中创建一个增益 DSP。它适合做总线音量微调、临时放大或衰减，也可以在运行时用 ``volume_db`` 或 ``volume_linear`` 做平滑的强度控制。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - volume_db
    - 0.0
    - 增益，单位为分贝
  * - `float`_
    - volume_linear
    - 1.0
    - 线性增益；该属性隐藏在 Inspector 中，但可以从脚本访问

方法
~~~~

.. _FmodAudioEffectAmplify-set_volume_db:

void set_volume_db(volume_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置分贝增益。

.. _FmodAudioEffectAmplify-get_volume_db:

`float`_ get_volume_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回分贝增益。

.. _FmodAudioEffectAmplify-set_volume_linear:

void set_volume_linear(volume_linear: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置线性增益。

.. _FmodAudioEffectAmplify-get_volume_linear:

`float`_ get_volume_linear() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回线性增益。

.. _FmodAudioEffectFilter:

FmodAudioEffectFilter
---------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**滤波器效果，用于按截止频率、斜率、增益和共振塑造频率响应。**

描述
~~~~

**FmodAudioEffectFilter** 提供基础滤波控制，可通过 ``cutoff_hz`` 设置截止频率，通过 ``db`` 选择截止曲线斜率，并用 ``gain`` 与 ``resonance`` 调整滤波后的信号强度和共振感。它适合制作低通、高通、遮挡、远近感或菜单过渡等效果。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - cutoff_hz
    - 2000.0
    - 截止频率，单位为 Hz
  * - :ref:`FilterDB<FmodAudioEffectFilter-FilterDB>`
    - db
    - FILTER_6DB
    - 截止曲线斜率
  * - `float`_
    - gain
    - 1.0
    - 滤波后频率的线性增益
  * - `float`_
    - resonance
    - 0.5
    - 截止频率附近的共振提升

方法
~~~~

.. _FmodAudioEffectFilter-set_cutoff_hz:

void set_cutoff_hz(cutoff_hz: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置截止频率。

.. _FmodAudioEffectFilter-get_cutoff_hz:

`float`_ get_cutoff_hz() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回截止频率。

.. _FmodAudioEffectFilter-set_db:

void set_db(db: :ref:`FilterDB<FmodAudioEffectFilter-FilterDB>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置滤波器斜率。

.. _FmodAudioEffectFilter-get_db:

:ref:`FilterDB<FmodAudioEffectFilter-FilterDB>` get_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回滤波器斜率。

.. _FmodAudioEffectFilter-set_gain:

void set_gain(gain: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置线性增益。

.. _FmodAudioEffectFilter-get_gain:

`float`_ get_gain() const
^^^^^^^^^^^^^^^^^^^^^^^^^

返回线性增益。

.. _FmodAudioEffectFilter-set_resonance:

void set_resonance(resonance: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置共振量。

.. _FmodAudioEffectFilter-get_resonance:

`float`_ get_resonance() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回共振量。

枚举
~~~~

.. _FmodAudioEffectFilter-FilterDB:

FilterDB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FILTER_6DB
    - 0
    - 每倍频程 6 dB 的斜率
  * - FILTER_12DB
    - 1
    - 每倍频程 12 dB 的斜率
  * - FILTER_18DB
    - 2
    - 每倍频程 18 dB 的斜率
  * - FILTER_24DB
    - 3
    - 每倍频程 24 dB 的斜率

.. _FmodAudioEffectEQ:

FmodAudioEffectEQ
-----------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**多段均衡器基类，使用 FMOD MULTIBAND_EQ DSP 组成 6、10 或 21 段 EQ。**

描述
~~~~

**FmodAudioEffectEQ** 使用一个或多个 FMOD ``MULTIBAND_EQ`` DSP 组成多段均衡器。它可以按预设创建 6、10 或 21 个频段，也可以逐频段修改增益、中心频率、Q 值和滤波器类型。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - :ref:`Preset<FmodAudioEffectEQ-Preset>`
    - preset
    - PRESET_6_BANDS
    - 均衡器频段预设
  * - `float`_
    - band_0_gain 到 band_n_gain
    - 0.0
    - 对应频段增益，单位为分贝
  * - `float`_
    - band_0_frequency 到 band_n_frequency
    - 按预设决定
    - 对应频段中心频率，单位为 Hz
  * - `float`_
    - band_0_q 到 band_n_q
    - 0.707
    - 对应频段 Q 值
  * - :ref:`FilterType<FmodAudioEffectEQ-FilterType>`
    - band_0_filter_type 到 band_n_filter_type
    - FILTER_PEAKING
    - 对应频段滤波器类型

方法
~~~~

.. _FmodAudioEffectEQ-set_preset:

void set_preset(preset: :ref:`Preset<FmodAudioEffectEQ-Preset>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置均衡器频段预设，并重建频段列表。

.. _FmodAudioEffectEQ-get_preset:

:ref:`Preset<FmodAudioEffectEQ-Preset>` get_preset() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前频段预设。

.. _FmodAudioEffectEQ-get_band_count:

`int`_ get_band_count() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前均衡器的频段数量。

.. _FmodAudioEffectEQ-set_band_gain_db:

void set_band_gain_db(band_idx: `int`_, gain_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的增益，单位为分贝。

.. _FmodAudioEffectEQ-get_band_gain_db:

`float`_ get_band_gain_db(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的增益，单位为分贝。

.. _FmodAudioEffectEQ-set_band_frequency:

void set_band_frequency(band_idx: `int`_, frequency: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的中心频率。

.. _FmodAudioEffectEQ-get_band_frequency:

`float`_ get_band_frequency(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的中心频率。

.. _FmodAudioEffectEQ-set_band_filter_type:

void set_band_filter_type(band_idx: `int`_, filter_type: :ref:`FilterType<FmodAudioEffectEQ-FilterType>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的滤波器类型。

.. _FmodAudioEffectEQ-get_band_filter_type:

:ref:`FilterType<FmodAudioEffectEQ-FilterType>` get_band_filter_type(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的滤波器类型。

.. _FmodAudioEffectEQ-set_band_q:

void set_band_q(band_idx: `int`_, q: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的 Q 值。

.. _FmodAudioEffectEQ-get_band_q:

`float`_ get_band_q(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的 Q 值。

枚举
~~~~

.. _FmodAudioEffectEQ-Preset:

Preset
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - PRESET_6_BANDS
    - 0
    - 6 段均衡器
  * - PRESET_10_BANDS
    - 1
    - 10 段均衡器
  * - PRESET_21_BANDS
    - 2
    - 21 段均衡器

.. _FmodAudioEffectEQ-FilterType:

FilterType
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FILTER_DISABLED
    - 0
    - 禁用该频段
  * - FILTER_LOWPASS_12DB
    - 1
    - 12 dB 低通
  * - FILTER_LOWPASS_24DB
    - 2
    - 24 dB 低通
  * - FILTER_LOWPASS_48DB
    - 3
    - 48 dB 低通
  * - FILTER_HIGHPASS_12DB
    - 4
    - 12 dB 高通
  * - FILTER_HIGHPASS_24DB
    - 5
    - 24 dB 高通
  * - FILTER_HIGHPASS_48DB
    - 6
    - 48 dB 高通
  * - FILTER_LOWSHELF
    - 7
    - 低频搁架
  * - FILTER_HIGHSHELF
    - 8
    - 高频搁架
  * - FILTER_PEAKING
    - 9
    - 峰值滤波
  * - FILTER_BANDPASS
    - 10
    - 带通滤波
  * - FILTER_NOTCH
    - 11
    - 陷波滤波
  * - FILTER_ALLPASS
    - 12
    - 全通滤波
  * - FILTER_LOWPASS_6DB
    - 13
    - 6 dB 低通
  * - FILTER_HIGHPASS_6DB
    - 14
    - 6 dB 高通

.. _FmodAudioEffectEQ6:

FmodAudioEffectEQ6
------------------

继承自： :ref:`FmodAudioEffectEQ<FmodAudioEffectEQ>`

**6 段均衡器预设。**

描述
~~~~

**FmodAudioEffectEQ6** 是 :ref:`FmodAudioEffectEQ<FmodAudioEffectEQ>` 的 6 频段预设版本。默认频段为 ``32``、``100``、``320``、``1000``、``3200``、``10000`` Hz。它继承 :ref:`FmodAudioEffectEQ<FmodAudioEffectEQ>` 的全部属性和方法。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - band_0_gain 到 band_n_gain
    - 0.0
    - 对应频段增益，单位为分贝
  * - `float`_
    - band_0_frequency 到 band_n_frequency
    - 按预设决定
    - 对应频段中心频率，单位为 Hz
  * - `float`_
    - band_0_q 到 band_n_q
    - 0.707
    - 对应频段 Q 值
  * - :ref:`FilterType<FmodAudioEffectEQ-FilterType>`
    - band_0_filter_type 到 band_n_filter_type
    - FILTER_PEAKING
    - 对应频段滤波器类型

方法
~~~~

.. _FmodAudioEffectEQ6-set_preset:

void set_preset(preset: :ref:`Preset<FmodAudioEffectEQ-Preset>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置均衡器频段预设，并重建频段列表。

.. _FmodAudioEffectEQ6-get_preset:

:ref:`Preset<FmodAudioEffectEQ-Preset>` get_preset() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前频段预设。

.. _FmodAudioEffectEQ6-get_band_count:

`int`_ get_band_count() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前均衡器的频段数量。

.. _FmodAudioEffectEQ6-set_band_gain_db:

void set_band_gain_db(band_idx: `int`_, gain_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的增益，单位为分贝。

.. _FmodAudioEffectEQ6-get_band_gain_db:

`float`_ get_band_gain_db(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的增益，单位为分贝。

.. _FmodAudioEffectEQ6-set_band_frequency:

void set_band_frequency(band_idx: `int`_, frequency: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的中心频率。

.. _FmodAudioEffectEQ6-get_band_frequency:

`float`_ get_band_frequency(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的中心频率。

.. _FmodAudioEffectEQ6-set_band_filter_type:

void set_band_filter_type(band_idx: `int`_, filter_type: :ref:`FilterType<FmodAudioEffectEQ-FilterType>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的滤波器类型。

.. _FmodAudioEffectEQ6-get_band_filter_type:

:ref:`FilterType<FmodAudioEffectEQ-FilterType>` get_band_filter_type(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的滤波器类型。

.. _FmodAudioEffectEQ6-set_band_q:

void set_band_q(band_idx: `int`_, q: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的 Q 值。

.. _FmodAudioEffectEQ6-get_band_q:

`float`_ get_band_q(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的 Q 值。

.. _FmodAudioEffectEQ10:

FmodAudioEffectEQ10
-------------------

继承自： :ref:`FmodAudioEffectEQ<FmodAudioEffectEQ>`

**10 段均衡器预设。**

描述
~~~~

**FmodAudioEffectEQ10** 是 :ref:`FmodAudioEffectEQ<FmodAudioEffectEQ>` 的 10 频段预设版本。默认频段为 ``31.25``、``62.5``、``125``、``250``、``500``、``1000``、``2000``、``4000``、``8000``、``16000`` Hz。它继承 :ref:`FmodAudioEffectEQ<FmodAudioEffectEQ>` 的全部属性和方法。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - band_0_gain 到 band_n_gain
    - 0.0
    - 对应频段增益，单位为分贝
  * - `float`_
    - band_0_frequency 到 band_n_frequency
    - 按预设决定
    - 对应频段中心频率，单位为 Hz
  * - `float`_
    - band_0_q 到 band_n_q
    - 0.707
    - 对应频段 Q 值
  * - :ref:`FilterType<FmodAudioEffectEQ-FilterType>`
    - band_0_filter_type 到 band_n_filter_type
    - FILTER_PEAKING
    - 对应频段滤波器类型

方法
~~~~

.. _FmodAudioEffectEQ10-set_preset:

void set_preset(preset: :ref:`Preset<FmodAudioEffectEQ-Preset>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置均衡器频段预设，并重建频段列表。

.. _FmodAudioEffectEQ10-get_preset:

:ref:`Preset<FmodAudioEffectEQ-Preset>` get_preset() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前频段预设。

.. _FmodAudioEffectEQ10-get_band_count:

`int`_ get_band_count() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前均衡器的频段数量。

.. _FmodAudioEffectEQ10-set_band_gain_db:

void set_band_gain_db(band_idx: `int`_, gain_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的增益，单位为分贝。

.. _FmodAudioEffectEQ10-get_band_gain_db:

`float`_ get_band_gain_db(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的增益，单位为分贝。

.. _FmodAudioEffectEQ10-set_band_frequency:

void set_band_frequency(band_idx: `int`_, frequency: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的中心频率。

.. _FmodAudioEffectEQ10-get_band_frequency:

`float`_ get_band_frequency(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的中心频率。

.. _FmodAudioEffectEQ10-set_band_filter_type:

void set_band_filter_type(band_idx: `int`_, filter_type: :ref:`FilterType<FmodAudioEffectEQ-FilterType>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的滤波器类型。

.. _FmodAudioEffectEQ10-get_band_filter_type:

:ref:`FilterType<FmodAudioEffectEQ-FilterType>` get_band_filter_type(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的滤波器类型。

.. _FmodAudioEffectEQ10-set_band_q:

void set_band_q(band_idx: `int`_, q: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的 Q 值。

.. _FmodAudioEffectEQ10-get_band_q:

`float`_ get_band_q(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的 Q 值。

.. _FmodAudioEffectEQ21:

FmodAudioEffectEQ21
-------------------

继承自： :ref:`FmodAudioEffectEQ<FmodAudioEffectEQ>`

**21 段均衡器预设。**

描述
~~~~

**FmodAudioEffectEQ21** 是 :ref:`FmodAudioEffectEQ<FmodAudioEffectEQ>` 的 21 频段预设版本。默认频段从 ``22`` Hz 延伸到 ``22000`` Hz。它继承 :ref:`FmodAudioEffectEQ<FmodAudioEffectEQ>` 的全部属性和方法。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - band_0_gain 到 band_n_gain
    - 0.0
    - 对应频段增益，单位为分贝
  * - `float`_
    - band_0_frequency 到 band_n_frequency
    - 按预设决定
    - 对应频段中心频率，单位为 Hz
  * - `float`_
    - band_0_q 到 band_n_q
    - 0.707
    - 对应频段 Q 值
  * - :ref:`FilterType<FmodAudioEffectEQ-FilterType>`
    - band_0_filter_type 到 band_n_filter_type
    - FILTER_PEAKING
    - 对应频段滤波器类型

方法
~~~~

.. _FmodAudioEffectEQ21-set_preset:

void set_preset(preset: :ref:`Preset<FmodAudioEffectEQ-Preset>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置均衡器频段预设，并重建频段列表。

.. _FmodAudioEffectEQ21-get_preset:

:ref:`Preset<FmodAudioEffectEQ-Preset>` get_preset() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前频段预设。

.. _FmodAudioEffectEQ21-get_band_count:

`int`_ get_band_count() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前均衡器的频段数量。

.. _FmodAudioEffectEQ21-set_band_gain_db:

void set_band_gain_db(band_idx: `int`_, gain_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的增益，单位为分贝。

.. _FmodAudioEffectEQ21-get_band_gain_db:

`float`_ get_band_gain_db(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的增益，单位为分贝。

.. _FmodAudioEffectEQ21-set_band_frequency:

void set_band_frequency(band_idx: `int`_, frequency: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的中心频率。

.. _FmodAudioEffectEQ21-get_band_frequency:

`float`_ get_band_frequency(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的中心频率。

.. _FmodAudioEffectEQ21-set_band_filter_type:

void set_band_filter_type(band_idx: `int`_, filter_type: :ref:`FilterType<FmodAudioEffectEQ-FilterType>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的滤波器类型。

.. _FmodAudioEffectEQ21-get_band_filter_type:

:ref:`FilterType<FmodAudioEffectEQ-FilterType>` get_band_filter_type(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的滤波器类型。

.. _FmodAudioEffectEQ21-set_band_q:

void set_band_q(band_idx: `int`_, q: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定频段的 Q 值。

.. _FmodAudioEffectEQ21-get_band_q:

`float`_ get_band_q(band_idx: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频段的 Q 值。

.. _FmodAudioEffectDelay:

FmodAudioEffectDelay
--------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**双 Tap 延迟与反馈延迟效果。**

描述
~~~~

**FmodAudioEffectDelay** 提供两个独立 Tap 和一个可选反馈回路。每个 Tap 都可以设置延迟时间、电平和声像，反馈回路则可以设置延迟、电平和低通截止频率。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - dry
    - 1.0
    - 原始信号电平
  * - `bool`_
    - tap1_active
    - true
    - 是否启用第一个延迟 Tap
  * - `float`_
    - tap1_delay_ms
    - 250.0
    - 第一个 Tap 的延迟时间
  * - `float`_
    - tap1_level_db
    - -6.0
    - 第一个 Tap 的电平
  * - `float`_
    - tap1_pan
    - 0.2
    - 第一个 Tap 的声像
  * - `bool`_
    - tap2_active
    - true
    - 是否启用第二个延迟 Tap
  * - `float`_
    - tap2_delay_ms
    - 500.0
    - 第二个 Tap 的延迟时间
  * - `float`_
    - tap2_level_db
    - -12.0
    - 第二个 Tap 的电平
  * - `float`_
    - tap2_pan
    - -0.4
    - 第二个 Tap 的声像
  * - `bool`_
    - feedback_active
    - false
    - 是否启用反馈延迟
  * - `float`_
    - feedback_delay_ms
    - 340.0
    - 反馈延迟时间
  * - `float`_
    - feedback_level_db
    - -6.0
    - 反馈电平
  * - `float`_
    - feedback_lowpass
    - 16000.0
    - 反馈低通截止频率

方法
~~~~

.. _FmodAudioEffectDelay-set_dry:

void set_dry(dry: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置原始信号电平。

.. _FmodAudioEffectDelay-get_dry:

`float`_ get_dry()
^^^^^^^^^^^^^^^^^^

返回原始信号电平。

.. _FmodAudioEffectDelay-set_tap1_active:

void set_tap1_active(active: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

启用或禁用第一个 Tap。

.. _FmodAudioEffectDelay-is_tap1_active:

`bool`_ is_tap1_active() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回第一个 Tap 是否启用。

.. _FmodAudioEffectDelay-set_tap1_delay_ms:

void set_tap1_delay_ms(delay_ms: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置第一个 Tap 的延迟时间。

.. _FmodAudioEffectDelay-get_tap1_delay_ms:

`float`_ get_tap1_delay_ms() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回第一个 Tap 的延迟时间。

.. _FmodAudioEffectDelay-set_tap1_level_db:

void set_tap1_level_db(level_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置第一个 Tap 的电平。

.. _FmodAudioEffectDelay-get_tap1_level_db:

`float`_ get_tap1_level_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回第一个 Tap 的电平。

.. _FmodAudioEffectDelay-set_tap1_pan:

void set_tap1_pan(pan: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置第一个 Tap 的声像。

.. _FmodAudioEffectDelay-get_tap1_pan:

`float`_ get_tap1_pan() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回第一个 Tap 的声像。

.. _FmodAudioEffectDelay-set_tap2_active:

void set_tap2_active(active: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

启用或禁用第二个 Tap。

.. _FmodAudioEffectDelay-is_tap2_active:

`bool`_ is_tap2_active() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回第二个 Tap 是否启用。

.. _FmodAudioEffectDelay-set_tap2_delay_ms:

void set_tap2_delay_ms(delay_ms: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置第二个 Tap 的延迟时间。

.. _FmodAudioEffectDelay-get_tap2_delay_ms:

`float`_ get_tap2_delay_ms() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回第二个 Tap 的延迟时间。

.. _FmodAudioEffectDelay-set_tap2_level_db:

void set_tap2_level_db(level_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置第二个 Tap 的电平。

.. _FmodAudioEffectDelay-get_tap2_level_db:

`float`_ get_tap2_level_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回第二个 Tap 的电平。

.. _FmodAudioEffectDelay-set_tap2_pan:

void set_tap2_pan(pan: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置第二个 Tap 的声像。

.. _FmodAudioEffectDelay-get_tap2_pan:

`float`_ get_tap2_pan() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回第二个 Tap 的声像。

.. _FmodAudioEffectDelay-set_feedback_active:

void set_feedback_active(active: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

启用或禁用反馈延迟。

.. _FmodAudioEffectDelay-is_feedback_active:

`bool`_ is_feedback_active() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回反馈延迟是否启用。

.. _FmodAudioEffectDelay-set_feedback_delay_ms:

void set_feedback_delay_ms(delay_ms: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置反馈延迟时间。

.. _FmodAudioEffectDelay-get_feedback_delay_ms:

`float`_ get_feedback_delay_ms() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回反馈延迟时间。

.. _FmodAudioEffectDelay-set_feedback_level_db:

void set_feedback_level_db(level_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置反馈电平。

.. _FmodAudioEffectDelay-get_feedback_level_db:

`float`_ get_feedback_level_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回反馈电平。

.. _FmodAudioEffectDelay-set_feedback_lowpass:

void set_feedback_lowpass(lowpass: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置反馈低通截止频率。

.. _FmodAudioEffectDelay-get_feedback_lowpass:

`float`_ get_feedback_lowpass() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回反馈低通截止频率。

.. _FmodAudioEffectChorus:

FmodAudioEffectChorus
---------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**合唱效果，支持多个 voice 的延迟、速率、深度、电平、截止频率和声像控制。**

描述
~~~~

**FmodAudioEffectChorus** 通过多个轻微延迟并调制的 voice 叠加出合唱感。你可以控制整体干湿比例，也可以逐 voice 调整延迟、调制速率、深度、电平、截止频率和声像。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `int`_
    - voice_count
    - 2
    - 参与合唱的 voice 数量
  * - `float`_
    - wet
    - 0.5
    - 效果信号电平
  * - `float`_
    - dry
    - 1.0
    - 原始信号电平

方法
~~~~

.. _FmodAudioEffectChorus-set_voice_count:

void set_voice_count(voices: `int`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置 voice 数量。

.. _FmodAudioEffectChorus-get_voice_count:

`int`_ get_voice_count() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回 voice 数量。

.. _FmodAudioEffectChorus-set_wet:

void set_wet(amount: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置效果信号电平。

.. _FmodAudioEffectChorus-get_wet:

`float`_ get_wet() const
^^^^^^^^^^^^^^^^^^^^^^^^

返回效果信号电平。

.. _FmodAudioEffectChorus-set_dry:

void set_dry(amount: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置原始信号电平。

.. _FmodAudioEffectChorus-get_dry:

`float`_ get_dry() const
^^^^^^^^^^^^^^^^^^^^^^^^

返回原始信号电平。

.. _FmodAudioEffectChorus-set_voice_delay_ms:

void set_voice_delay_ms(voice: `int`_, delay_ms: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定 voice 的延迟时间。

.. _FmodAudioEffectChorus-get_voice_delay_ms:

`float`_ get_voice_delay_ms(voice: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定 voice 的延迟时间。

.. _FmodAudioEffectChorus-set_voice_rate_hz:

void set_voice_rate_hz(voice: `int`_, rate_hz: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定 voice 的调制速率。

.. _FmodAudioEffectChorus-get_voice_rate_hz:

`float`_ get_voice_rate_hz(voice: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定 voice 的调制速率。

.. _FmodAudioEffectChorus-set_voice_depth_ms:

void set_voice_depth_ms(voice: `int`_, depth_ms: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定 voice 的调制深度。

.. _FmodAudioEffectChorus-get_voice_depth_ms:

`float`_ get_voice_depth_ms(voice: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定 voice 的调制深度。

.. _FmodAudioEffectChorus-set_voice_level_db:

void set_voice_level_db(voice: `int`_, level_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定 voice 的电平。

.. _FmodAudioEffectChorus-get_voice_level_db:

`float`_ get_voice_level_db(voice: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定 voice 的电平。

.. _FmodAudioEffectChorus-set_voice_cutoff_hz:

void set_voice_cutoff_hz(voice: `int`_, cutoff_hz: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定 voice 的截止频率。

.. _FmodAudioEffectChorus-get_voice_cutoff_hz:

`float`_ get_voice_cutoff_hz(voice: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定 voice 的截止频率。

.. _FmodAudioEffectChorus-set_voice_pan:

void set_voice_pan(voice: `int`_, pan: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定 voice 的声像。

.. _FmodAudioEffectChorus-get_voice_pan:

`float`_ get_voice_pan(voice: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定 voice 的声像。

.. _FmodAudioEffectDistortion:

FmodAudioEffectDistortion
-------------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**失真效果，支持削波、反正切、低保真、过载、波形整形和比特压碎。**

描述
~~~~

**FmodAudioEffectDistortion** 会在效果链中创建自定义失真 DSP。它通过 ``mode`` 切换不同失真算法，并提供前级增益、驱动量、后级增益、高频保留和过采样控制。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - :ref:`Mode<FmodAudioEffectDistortion-Mode>`
    - mode
    - MODE_CLIP
    - 失真算法
  * - `float`_
    - pre_gain
    - 0.0
    - 失真前增益
  * - `float`_
    - drive
    - 0.0
    - 失真驱动量
  * - `float`_
    - post_gain
    - 0.0
    - 失真后增益
  * - `float`_
    - keep_hf_hz
    - 16000.0
    - 高频保留频率
  * - `int`_
    - oversample
    - 4
    - 过采样倍数

方法
~~~~

.. _FmodAudioEffectDistortion-set_mode:

void set_mode(mode: :ref:`Mode<FmodAudioEffectDistortion-Mode>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置失真算法。

.. _FmodAudioEffectDistortion-get_mode:

:ref:`Mode<FmodAudioEffectDistortion-Mode>` get_mode() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回失真算法。

.. _FmodAudioEffectDistortion-set_pre_gain:

void set_pre_gain(gain: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置前级增益。

.. _FmodAudioEffectDistortion-get_pre_gain:

`float`_ get_pre_gain() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回前级增益。

.. _FmodAudioEffectDistortion-set_drive:

void set_drive(drive: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置驱动量。

.. _FmodAudioEffectDistortion-get_drive:

`float`_ get_drive() const
^^^^^^^^^^^^^^^^^^^^^^^^^^

返回驱动量。

.. _FmodAudioEffectDistortion-set_post_gain:

void set_post_gain(gain: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置后级增益。

.. _FmodAudioEffectDistortion-get_post_gain:

`float`_ get_post_gain() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回后级增益。

.. _FmodAudioEffectDistortion-set_keep_hf_hz:

void set_keep_hf_hz(hz: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置高频保留频率。

.. _FmodAudioEffectDistortion-get_keep_hf_hz:

`float`_ get_keep_hf_hz() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回高频保留频率。

.. _FmodAudioEffectDistortion-set_oversample:

void set_oversample(oversample: `int`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置过采样倍数。

.. _FmodAudioEffectDistortion-get_oversample:

`int`_ get_oversample() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回过采样倍数。

枚举
~~~~

.. _FmodAudioEffectDistortion-Mode:

Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - MODE_CLIP
    - 0
    - 硬削波
  * - MODE_ATAN
    - 1
    - 反正切软削波
  * - MODE_LOFI
    - 2
    - 低保真失真
  * - MODE_OVERDRIVE
    - 3
    - 过载失真
  * - MODE_WAVESHAPE
    - 4
    - 波形整形
  * - MODE_BITCRUSH
    - 5
    - 比特压碎

.. _FmodAudioEffectPhaser:

FmodAudioEffectPhaser
---------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**移相器效果。**

描述
~~~~

**FmodAudioEffectPhaser** 通过扫频相位偏移制造流动、旋转或镂空的调制音色。``range_min_hz`` 与 ``range_max_hz`` 控制扫频范围，``rate_hz`` 控制移动速度，``depth`` 与 ``feedback`` 控制效果强度。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - depth
    - 1.0
    - 调制深度
  * - `float`_
    - feedback
    - 0.7
    - 反馈量
  * - `float`_
    - range_max_hz
    - 1600.0
    - 扫频范围上限
  * - `float`_
    - range_min_hz
    - 440.0
    - 扫频范围下限
  * - `float`_
    - rate_hz
    - 0.5
    - 调制速率

方法
~~~~

.. _FmodAudioEffectPhaser-set_depth:

void set_depth(depth: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置调制深度。

.. _FmodAudioEffectPhaser-get_depth:

`float`_ get_depth() const
^^^^^^^^^^^^^^^^^^^^^^^^^^

返回调制深度。

.. _FmodAudioEffectPhaser-set_feedback:

void set_feedback(feedback: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置反馈量。

.. _FmodAudioEffectPhaser-get_feedback:

`float`_ get_feedback() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回反馈量。

.. _FmodAudioEffectPhaser-set_range_max_hz:

void set_range_max_hz(range_max_hz: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置扫频范围上限。

.. _FmodAudioEffectPhaser-get_range_max_hz:

`float`_ get_range_max_hz() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回扫频范围上限。

.. _FmodAudioEffectPhaser-set_range_min_hz:

void set_range_min_hz(range_min_hz: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置扫频范围下限。

.. _FmodAudioEffectPhaser-get_range_min_hz:

`float`_ get_range_min_hz() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回扫频范围下限。

.. _FmodAudioEffectPhaser-set_rate_hz:

void set_rate_hz(rate_hz: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置调制速率。

.. _FmodAudioEffectPhaser-get_rate_hz:

`float`_ get_rate_hz() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回调制速率。

.. _FmodAudioEffectPitchShift:

FmodAudioEffectPitchShift
-------------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**音高变换效果。**

描述
~~~~

**FmodAudioEffectPitchShift** 用 FFT 处理改变信号音高。``pitch_scale`` 控制音高倍率，``fft_size`` 与 ``oversampling`` 会影响声音质量、延迟和 CPU 开销。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - pitch_scale
    - 1.0
    - 音高倍率
  * - :ref:`FFTSize<FmodAudioEffectPitchShift-FFTSize>`
    - fft_size
    - FFT_SIZE_2048
    - FFT 窗口大小
  * - `int`_
    - oversampling
    - 4
    - 过采样倍数

方法
~~~~

.. _FmodAudioEffectPitchShift-set_pitch_scale:

void set_pitch_scale(pitch_scale: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置音高倍率。

.. _FmodAudioEffectPitchShift-get_pitch_scale:

`float`_ get_pitch_scale() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回音高倍率。

.. _FmodAudioEffectPitchShift-set_fft_size:

void set_fft_size(fft_size: :ref:`FFTSize<FmodAudioEffectPitchShift-FFTSize>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置 FFT 窗口大小。

.. _FmodAudioEffectPitchShift-get_fft_size:

:ref:`FFTSize<FmodAudioEffectPitchShift-FFTSize>` get_fft_size() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回 FFT 窗口大小。

.. _FmodAudioEffectPitchShift-set_oversampling:

void set_oversampling(oversampling: `int`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置过采样倍数。

.. _FmodAudioEffectPitchShift-get_oversampling:

`int`_ get_oversampling() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回过采样倍数。

枚举
~~~~

.. _FmodAudioEffectPitchShift-FFTSize:

FFTSize
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FFT_SIZE_256
    - 0
    - 256 点 FFT
  * - FFT_SIZE_512
    - 1
    - 512 点 FFT
  * - FFT_SIZE_1024
    - 2
    - 1024 点 FFT
  * - FFT_SIZE_2048
    - 3
    - 2048 点 FFT
  * - FFT_SIZE_4096
    - 4
    - 4096 点 FFT
  * - FFT_SIZE_MAX
    - 5
    - 边界值

.. _FmodAudioEffectCompressor:

FmodAudioEffectCompressor
-------------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**动态压缩器。**

描述
~~~~

**FmodAudioEffectCompressor** 用于压低超过阈值的动态范围，并可通过输出增益补偿响度。``threshold_db`` 决定开始压缩的位置，``ratio`` 决定压缩强度，``attack_us`` 和 ``release_ms`` 控制响应速度，``mix`` 可用于并行压缩。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - threshold_db
    - 0.0
    - 压缩阈值
  * - `float`_
    - ratio
    - 4.0
    - 压缩比
  * - `float`_
    - gain_db
    - 0.0
    - 输出补偿增益
  * - `float`_
    - attack_us
    - 20.0
    - 启动时间，单位为微秒
  * - `float`_
    - release_ms
    - 250.0
    - 释放时间，单位为毫秒
  * - `float`_
    - mix
    - 1.0
    - 干湿混合比例
  * - `StringName`_
    - sidechain
    - 空
    - 侧链总线名；当前 FMOD 总线镜像尚未实际支持侧链路由

方法
~~~~

.. _FmodAudioEffectCompressor-set_threshold:

void set_threshold(threshold_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置压缩阈值。

.. _FmodAudioEffectCompressor-get_threshold:

`float`_ get_threshold() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回压缩阈值。

.. _FmodAudioEffectCompressor-set_ratio:

void set_ratio(ratio: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置压缩比。

.. _FmodAudioEffectCompressor-get_ratio:

`float`_ get_ratio() const
^^^^^^^^^^^^^^^^^^^^^^^^^^

返回压缩比。

.. _FmodAudioEffectCompressor-set_gain:

void set_gain(gain_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置输出补偿增益。

.. _FmodAudioEffectCompressor-get_gain:

`float`_ get_gain() const
^^^^^^^^^^^^^^^^^^^^^^^^^

返回输出补偿增益。

.. _FmodAudioEffectCompressor-set_attack_us:

void set_attack_us(attack_us: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置启动时间。

.. _FmodAudioEffectCompressor-get_attack_us:

`float`_ get_attack_us() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回启动时间。

.. _FmodAudioEffectCompressor-set_release_ms:

void set_release_ms(release_ms: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置释放时间。

.. _FmodAudioEffectCompressor-get_release_ms:

`float`_ get_release_ms() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回释放时间。

.. _FmodAudioEffectCompressor-set_mix:

void set_mix(mix: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置干湿混合比例。

.. _FmodAudioEffectCompressor-get_mix:

`float`_ get_mix() const
^^^^^^^^^^^^^^^^^^^^^^^^

返回干湿混合比例。

.. _FmodAudioEffectCompressor-set_sidechain:

void set_sidechain(sidechain: `StringName`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置侧链总线名。

.. _FmodAudioEffectCompressor-get_sidechain:

`StringName`_ get_sidechain() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回侧链总线名。

.. _FmodAudioEffectHardLimiter:

FmodAudioEffectHardLimiter
--------------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**硬限制器，用于限制峰值电平。**

描述
~~~~

**FmodAudioEffectHardLimiter** 用于阻止信号峰值超过指定上限。它常放在总线效果链后段，用于保护输出、抑制突发峰值或给某个总线做简单的安全限制。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - ceiling_db
    - -0.3
    - 输出峰值上限
  * - `float`_
    - pre_gain_db
    - 0.0
    - 限制前增益
  * - `float`_
    - release
    - 0.1
    - 释放时间

方法
~~~~

.. _FmodAudioEffectHardLimiter-set_ceiling_db:

void set_ceiling_db(ceiling_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置输出峰值上限。

.. _FmodAudioEffectHardLimiter-get_ceiling_db:

`float`_ get_ceiling_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回输出峰值上限。

.. _FmodAudioEffectHardLimiter-set_pre_gain_db:

void set_pre_gain_db(pre_gain_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置限制前增益。

.. _FmodAudioEffectHardLimiter-get_pre_gain_db:

`float`_ get_pre_gain_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回限制前增益。

.. _FmodAudioEffectHardLimiter-set_release:

void set_release(release: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置释放时间。

.. _FmodAudioEffectHardLimiter-get_release:

`float`_ get_release() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回释放时间。

.. _FmodAudioEffectPanner:

FmodAudioEffectPanner
---------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**左右声像控制。**

描述
~~~~

**FmodAudioEffectPanner** 提供简单的左右声像偏移。``pan`` 为负时偏左，为正时偏右，适合 2D UI 声音、非空间化音效或总线级声像调整。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - pan
    - 0.0
    - 声像位置，负值偏左，正值偏右

方法
~~~~

.. _FmodAudioEffectPanner-set_pan:

void set_pan(pan: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置声像位置。

.. _FmodAudioEffectPanner-get_pan:

`float`_ get_pan() const
^^^^^^^^^^^^^^^^^^^^^^^^

返回声像位置。

.. _FmodAudioEffectReverb:

FmodAudioEffectReverb
---------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**总线混响效果，参数风格接近 Godot 的 AudioEffectReverb。**

描述
~~~~

**FmodAudioEffectReverb** 是用于总线的混响效果，参数风格接近 Godot 的 ``AudioEffectReverb``。它通过房间尺寸、阻尼、预延迟、扩散和干湿比例塑造空间感，适合给一组声音统一添加环境混响。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - damping
    - 0.5
    - 高频阻尼
  * - `float`_
    - dry
    - 1.0
    - 原始信号电平
  * - `float`_
    - hipass
    - 0.0
    - 高通滤波量
  * - `float`_
    - predelay_feedback
    - 0.4
    - 预延迟反馈量
  * - `float`_
    - predelay_msec
    - 150.0
    - 预延迟时间，单位为毫秒
  * - `float`_
    - room_size
    - 0.8
    - 房间尺寸
  * - `float`_
    - spread
    - 1.0
    - 立体声扩散
  * - `float`_
    - wet
    - 0.5
    - 混响信号电平

方法
~~~~

.. _FmodAudioEffectReverb-set_damping:

void set_damping(damping: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置高频阻尼。

.. _FmodAudioEffectReverb-get_damping:

`float`_ get_damping() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回高频阻尼。

.. _FmodAudioEffectReverb-set_dry:

void set_dry(dry: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置原始信号电平。

.. _FmodAudioEffectReverb-get_dry:

`float`_ get_dry() const
^^^^^^^^^^^^^^^^^^^^^^^^

返回原始信号电平。

.. _FmodAudioEffectReverb-set_hpf:

void set_hpf(hpf: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置高通滤波量。

.. _FmodAudioEffectReverb-get_hpf:

`float`_ get_hpf() const
^^^^^^^^^^^^^^^^^^^^^^^^

返回高通滤波量。

.. _FmodAudioEffectReverb-set_predelay_feedback:

void set_predelay_feedback(predelay_feedback: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置预延迟反馈量。

.. _FmodAudioEffectReverb-get_predelay_feedback:

`float`_ get_predelay_feedback() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回预延迟反馈量。

.. _FmodAudioEffectReverb-set_predelay_msec:

void set_predelay_msec(predelay_msec: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置预延迟时间。

.. _FmodAudioEffectReverb-get_predelay_msec:

`float`_ get_predelay_msec() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回预延迟时间。

.. _FmodAudioEffectReverb-set_room_size:

void set_room_size(room_size: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置房间尺寸。

.. _FmodAudioEffectReverb-get_room_size:

`float`_ get_room_size() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回房间尺寸。

.. _FmodAudioEffectReverb-set_spread:

void set_spread(spread: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置立体声扩散。

.. _FmodAudioEffectReverb-get_spread:

`float`_ get_spread() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回立体声扩散。

.. _FmodAudioEffectReverb-set_wet:

void set_wet(wet: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置混响信号电平。

.. _FmodAudioEffectReverb-get_wet:

`float`_ get_wet() const
^^^^^^^^^^^^^^^^^^^^^^^^

返回混响信号电平。

.. _FmodAudioEffectStereoEnhance:

FmodAudioEffectStereoEnhance
----------------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**立体声增强效果。**

描述
~~~~

**FmodAudioEffectStereoEnhance** 用于加宽或强化立体声形象。``pan_pullout`` 调整左右声像拉开感，``time_pullout_ms`` 增加双声道时间差，``surround`` 控制环绕增强量。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - pan_pullout
    - 1.0
    - 声像拉开量
  * - `float`_
    - time_pullout_ms
    - 0.0
    - 时间差拉开量，单位为毫秒
  * - `float`_
    - surround
    - 0.0
    - 环绕增强量

方法
~~~~

.. _FmodAudioEffectStereoEnhance-set_pan_pullout:

void set_pan_pullout(amount: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置声像拉开量。

.. _FmodAudioEffectStereoEnhance-get_pan_pullout:

`float`_ get_pan_pullout() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回声像拉开量。

.. _FmodAudioEffectStereoEnhance-set_time_pullout:

void set_time_pullout(amount: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置时间差拉开量。

.. _FmodAudioEffectStereoEnhance-get_time_pullout:

`float`_ get_time_pullout() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回时间差拉开量。

.. _FmodAudioEffectStereoEnhance-set_surround:

void set_surround(amount: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置环绕增强量。

.. _FmodAudioEffectStereoEnhance-get_surround:

`float`_ get_surround() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回环绕增强量。

.. _FmodAudioEffectSpectrumAnalyzer:

FmodAudioEffectSpectrumAnalyzer
-------------------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**频谱分析器，可读取频段幅度、RMS 和频谱重心。**

描述
~~~~

**FmodAudioEffectSpectrumAnalyzer** 会在总线效果链中插入 FFT DSP，并从中读取频谱数据。它不会主动改变声音，主要用于可视化、节拍/能量检测、频段驱动的 UI 或调试混音。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - buffer_length
    - 2.0
    - 分析缓冲长度，单位为秒
  * - :ref:`FFTSize<FmodAudioEffectSpectrumAnalyzer-FFTSize>`
    - fft_size
    - FFT_SIZE_1024
    - FFT 窗口大小

方法
~~~~

.. _FmodAudioEffectSpectrumAnalyzer-set_buffer_length:

void set_buffer_length(buffer_length: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置分析缓冲长度。

.. _FmodAudioEffectSpectrumAnalyzer-get_buffer_length:

`float`_ get_buffer_length() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回分析缓冲长度。

.. _FmodAudioEffectSpectrumAnalyzer-set_fft_size:

void set_fft_size(fft_size: :ref:`FFTSize<FmodAudioEffectSpectrumAnalyzer-FFTSize>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置 FFT 窗口大小。

.. _FmodAudioEffectSpectrumAnalyzer-get_fft_size:

:ref:`FFTSize<FmodAudioEffectSpectrumAnalyzer-FFTSize>` get_fft_size() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回 FFT 窗口大小。

.. _FmodAudioEffectSpectrumAnalyzer-update_spectrum:

void update_spectrum()
^^^^^^^^^^^^^^^^^^^^^^

主动刷新频谱数据。

.. _FmodAudioEffectSpectrumAnalyzer-get_bin_count:

`int`_ get_bin_count() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前频谱 bin 数量。

.. _FmodAudioEffectSpectrumAnalyzer-get_rms:

`float`_ get_rms() const
^^^^^^^^^^^^^^^^^^^^^^^^

返回当前 RMS。

.. _FmodAudioEffectSpectrumAnalyzer-get_centroid:

`float`_ get_centroid() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前频谱重心。

.. _FmodAudioEffectSpectrumAnalyzer-get_magnitude_for_frequency_range:

`Vector2`_ get_magnitude_for_frequency_range(begin: `float`_, end: `float`_, mode: :ref:`MagnitudeMode<FmodAudioEffectSpectrumAnalyzer-MagnitudeMode>` = MAGNITUDE_MAX) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定频率范围内左右声道的幅度。

枚举
~~~~

.. _FmodAudioEffectSpectrumAnalyzer-FFTSize:

FFTSize
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FFT_SIZE_256
    - 0
    - 256 点 FFT
  * - FFT_SIZE_512
    - 1
    - 512 点 FFT
  * - FFT_SIZE_1024
    - 2
    - 1024 点 FFT
  * - FFT_SIZE_2048
    - 3
    - 2048 点 FFT
  * - FFT_SIZE_4096
    - 4
    - 4096 点 FFT
  * - FFT_SIZE_MAX
    - 5
    - 边界值

.. _FmodAudioEffectSpectrumAnalyzer-MagnitudeMode:

MagnitudeMode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - MAGNITUDE_AVERAGE
    - 0
    - 返回频率范围内的平均幅度
  * - MAGNITUDE_MAX
    - 1
    - 返回频率范围内的最大幅度

示例
~~~~

.. code-block:: gdscript

    @onready var bus := FmodServer.get_bus("Master")
    var analyzer := FmodAudioEffectSpectrumAnalyzer.new()

    func _ready():
        analyzer.fft_size = FmodAudioEffectSpectrumAnalyzer.FFT_SIZE_2048
        analyzer.buffer_length = 1.0
        bus.add_effect(analyzer)

    func _process(_delta):
        analyzer.update_spectrum()
        var low := analyzer.get_magnitude_for_frequency_range(20.0, 250.0, FmodAudioEffectSpectrumAnalyzer.MAGNITUDE_AVERAGE)
        var mid := analyzer.get_magnitude_for_frequency_range(250.0, 4000.0)
        var high := analyzer.get_magnitude_for_frequency_range(4000.0, 16000.0)
        print("low: ", low.length(), " mid: ", mid.length(), " high: ", high.length())
        print("rms: ", analyzer.get_rms(), " centroid: ", analyzer.get_centroid())

.. _FmodAudioEffectRecord:

FmodAudioEffectRecord
---------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**录音效果，会让信号原样通过，并在录制时缓存经过该总线的音频。**

描述
~~~~

**FmodAudioEffectRecord** 是一个通过型录音 DSP。它不会改变总线输出，而是在 ``recording_active`` 启用时把经过效果器的音频写入内部缓冲。停止录制后，可以通过 ``get_recording()`` 得到 `AudioStreamWAV`_，也可以通过 ``get_waveform_snapshot()`` 获取波形预览数据。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - :ref:`FmodAudioEffectRecord.Format<FmodAudioEffectRecord-Format>`
    - format
    - FORMAT_16_BITS
    - 导出为 `AudioStreamWAV`_ 时使用的采样格式
  * - `bool`_
    - recording_active
    - false
    - 是否正在录制

方法
~~~~

.. _FmodAudioEffectRecord-set_recording_active:

void set_recording_active(record: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

开始或停止录制。

.. _FmodAudioEffectRecord-is_recording_active:

`bool`_ is_recording_active() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前是否正在录制。

.. _FmodAudioEffectRecord-set_format:

void set_format(format: :ref:`FmodAudioEffectRecord.Format<FmodAudioEffectRecord-Format>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置导出 WAV 格式。

.. _FmodAudioEffectRecord-get_format:

:ref:`FmodAudioEffectRecord.Format<FmodAudioEffectRecord-Format>` get_format() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回导出 WAV 格式。

.. _FmodAudioEffectRecord-get_recording:

`AudioStreamWAV`_ get_recording() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前缓存内容生成的 WAV 音频流。

.. _FmodAudioEffectRecord-get_waveform_snapshot:

`PackedVector2Array`_ get_waveform_snapshot(width: `int`_ = 512, seconds: `float`_ = 5.0) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回最近一段录音的波形快照。

枚举
~~~~

.. _FmodAudioEffectRecord-Format:

Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FORMAT_8_BITS
    - 0
    - 导出 8-bit PCM WAV
  * - FORMAT_16_BITS
    - 1
    - 导出 16-bit PCM WAV
  * - FORMAT_IMA_ADPCM
    - 2
    - 请求 IMA ADPCM；当前会以有效 16-bit PCM WAV 数据导出

示例
~~~~

.. code-block:: gdscript

    @onready var bus := FmodServer.get_bus("Master")
    var recorder := FmodAudioEffectRecord.new()
    var recorded_stream: AudioStreamWAV

    func _ready():
        recorder.format = FmodAudioEffectRecord.FORMAT_16_BITS
        bus.add_effect(recorder)

    func start_recording():
        recorder.recording_active = true

    func stop_recording():
        recorder.recording_active = false
        recorded_stream = recorder.get_recording()

        if recorded_stream:
            var player := AudioStreamPlayer.new()
            add_child(player)
            player.stream = recorded_stream
            player.play()

    func get_waveform_points() -> PackedVector2Array:
        return recorder.get_waveform_snapshot(256, 3.0)

.. _FmodAudioEffectCapture:

FmodAudioEffectCapture
----------------------

继承自： :ref:`FmodAudioEffect<FmodAudioEffect>`

**捕获效果，可从环形缓冲中取出经过该总线的音频帧。**

描述
~~~~

**FmodAudioEffectCapture** 会把经过总线的音频写入内部环形缓冲，并允许脚本按帧读取 `PackedVector2Array`_。它适合做实时波形、音频驱动逻辑、简单录制前缓存，或把 FMOD 输出转交给其它 Godot 侧处理流程。

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - buffer_length
    - 1.0
    - 环形缓冲长度，单位为秒

方法
~~~~

.. _FmodAudioEffectCapture-set_buffer_length:

void set_buffer_length(buffer_length: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置环形缓冲长度。

.. _FmodAudioEffectCapture-get_buffer_length:

`float`_ get_buffer_length() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回环形缓冲长度。

.. _FmodAudioEffectCapture-can_get_buffer:

`bool`_ can_get_buffer(frames: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果缓冲中至少有指定帧数可读，则返回 ``true``。

.. _FmodAudioEffectCapture-get_buffer:

`PackedVector2Array`_ get_buffer(frames: `int`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

读取指定帧数并返回音频帧。

.. _FmodAudioEffectCapture-clear_buffer:

void clear_buffer()
^^^^^^^^^^^^^^^^^^^

清空捕获缓冲。

.. _FmodAudioEffectCapture-get_discarded_frames:

`int`_ get_discarded_frames() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回因缓冲写满而丢弃的帧数。

.. _FmodAudioEffectCapture-get_frames_available:

`int`_ get_frames_available() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前可读取的帧数。

.. _FmodAudioEffectCapture-get_pushed_frames:

`int`_ get_pushed_frames() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回已经写入缓冲的总帧数。
