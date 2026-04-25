核心类 API
==========

.. _FmodServer:


FmodServer
----------

继承自： `Object`_

**管理 FMOD 音频系统生命周期的全局单例**

描述
~~~~

**FmodServer** 是一个全局单例，用于管理 Godot 中的 FMOD Core API 音频系统。它初始化并维护主 FMOD 系统实例，注册性能监控以跟踪 CPU 和文件使用情况，管理音频总线布局，并连接到 Godot 的 `SceneTree`_ 以进行每帧更新

服务器在 `GDExtension`_ 加载期间自动初始化，并处理所有 FMOD 生命周期管理。它创建的性能监控可以在 Godot 的调试器 > 监视器选项卡中查看，以跟踪 FMOD 的资源使用情况

**性能监控：**

以下自定义监控已注册到 Godot 的性能系统：

.. list-table::

   * - FmodCPUUsage/DSP
     - DSP 处理 CPU 使用百分比
   * - FmodCPUUsage/Stream
     - 流解码 CPU 使用百分比
   * - FmodCPUUsage/Geometry
     - 3D 几何处理 CPU 使用百分比
   * - FmodCPUUsage/Update
     - 系统更新 CPU 使用百分比
   * - FmodCPUUsage/Convolution1
     - 卷积混响 1 CPU 使用百分比
   * - FmodCPUUsage/Convolution2
     - 卷积混响 2 的 CPU 使用百分比
   * - FmodFileUsage/SampleBytesRead
     - 从磁盘读取的样本字节数
   * - FmodFileUsage/StreamBytesRead
     - 从磁盘读取的流字节数
   * - FmodFileUsage/OtherBytesRead
     - 从磁盘读取的其他字节数

方法
~~~~

.. _FmodServer-generate_bus_layout:

void generate_bus_layout() static
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

生成音频总线布局

这将扫描 Godot 的 `AudioServer`_ 总线层级并创建对应的 :ref:`FmodAudioBusLayout<FmodAudioBusLayout>` 和 :ref:`FmodAudioBus<FmodAudioBus>` 实例，以确保 FMOD 的总线结构与 Godot 的总线结构同步

.. _FmodServer-get_audio_bus_layout:

:ref:`FmodAudioBusLayout<FmodAudioBusLayout>` get_audio_bus_layout() static
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回用于管理音频总线及其路由的音频总线布局。该总线布局与 Godot 的 `AudioServer`_ 总线布局同步，并提供 FMOD 特定的总线功能，包括 DSP 效果

.. _FmodServer-get_main_system:

:ref:`FmodSystem<FmodSystem>` get_main_system() static
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回主要的 FMOD 系统实例。这是创建声音、通道、DSP 效果和其他 FMOD 对象的主要接口。系统在服务器启动时会根据项目设置自动初始化

.. _FmodServer-get_master_channel_group:

:ref:`FmodChannelGroup<FmodChannelGroup>` get_master_channel_group() static
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回默认情况下所有声音通过的主通道组。它是通道组层次结构的根，可以用于控制所有正在播放声音的全局音量、音高和效果

.. _FmodServer-reset_main_system:

void reset_main_system(system: :ref:`FmodSystem<FmodSystem>`) static
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

重置主 FMOD 系统实例（用于测试或重新初始化）

.. _FmodSystem:

FmodSystem
----------

继承自： `RefCounted`_

**FMOD::System 对象的包装类，提供音频系统管理和控制**

描述
~~~~

**FmodSystem** 封装了 FMOD 核心 API 的 `FMOD::System <https://www.fmod.com/docs/2.02/api/core-api-system.html>`_ 对象，并提供全面的音频系统管理功能。该类负责系统初始化、音频设备管理、声音创建、播放控制以及录音功能

FMOD System 是 FMOD 音频引擎的核心。它管理混音器、音轨、声音、DSP 效果和输出设备。对于高级应用场景，可以创建多个 **FmodSystem** 实例；对于常规应用，则可以通过 :ref:`FmodServer<FmodServer>` 使用全局单例

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - 3d_max_world_size
    - 1000.0
    - 3D 几何遮挡使用的最大世界尺寸
  * - `int`_
    - 3d_num_listeners
    - 1
    - 3D 音频监听器数量
  * - `int`_
    - asio_num_channels
    - 0
    - ASIO 输入和输出通道数量
  * - `int`_
    - default_decode_buffer_size
    - 0
    - 流式解码双缓冲区默认大小
  * - `float`_
    - distance_factor
    - 1.0
    - 世界距离到米的换算比例
  * - `float`_
    - distance_filter_center_freq
    - 0.0
    - 距离滤波器默认中心频率
  * - `float`_
    - doppler_scale
    - 1.0
    - 多普勒效果缩放系数
  * - `int`_
    - dsp_buffer_pool_size
    - 0
    - DSP 中间混合缓冲区数量
  * - `int`_
    - geometry_max_fade_time
    - 0
    - 几何遮挡音量淡变最大时间
  * - `int`_
    - max_adpcm_codecs
    - 0
    - 最大 IMA-ADPCM 解码器数量
  * - `int`_
    - max_at9_codecs
    - 0
    - 最大 AT9 解码器数量
  * - `int`_
    - max_convolution_threads
    - 0
    - 卷积混响 DSP 最大线程数
  * - `int`_
    - max_fadpcm_codecs
    - 0
    - 最大 FADPCM 解码器数量
  * - `int`_
    - max_mpeg_codecs
    - 0
    - 最大 MPEG 解码器数量
  * - `int`_
    - max_opus_codecs
    - 0
    - 最大 Opus 解码器数量
  * - `int`_
    - max_software_channels
    - 0
    - 软件混音器最大通道数量
  * - `int`_
    - max_spatial_objects
    - 0
    - 每个系统预留的最大空间对象数量
  * - `int`_
    - max_vorbis_codecs
    - 0
    - 最大 Vorbis 解码器数量
  * - `int`_
    - max_xma_codecs
    - 0
    - 最大 XMA 解码器数量
  * - `int`_
    - profile_port
    - 0
    - FMOD Profiler 监听端口
  * - `int`_
    - random_seed
    - 0
    - 内部随机数生成器种子
  * - :ref:`FmodResamplerMethod<FmodResamplerMethod>`
    - resampler_method
    - 0
    - 软件混音器重采样方法
  * - `int`_
    - reverb_3d_instance
    - 0
    - Reverb3D 使用的全局混响实例
  * - `float`_
    - rolloff_scale
    - 1.0
    - 3D 距离衰减缩放系数
  * - `float`_
    - vol0_virtual_vol
    - 0.0
    - 低于该音量的声道转为虚拟声道

方法
~~~~

有效性检查
^^^^^^^^^^

.. _FmodSystem-system_is_null:

`bool`_ system_is_null() const
++++++++++++++++++++++++++++++

如果系统实例未初始化或无效，则返回 ``true``。这表示 FMOD 系统尚未准备好使用

.. _FmodSystem-system_is_valid:

`bool`_ system_is_valid() const
+++++++++++++++++++++++++++++++

如果系统实例已成功初始化并且 FMOD 系统可用，则返回 ``true``。这表示 FMOD 系统已准备好处理音频操作

系统管理
^^^^^^^^

.. _FmodSystem-create_system:

:ref:`FmodSystem<FmodSystem>` create_system() static
++++++++++++++++++++++++++++++++++++++++++++++++++++

创建并返回一个新的 FMOD System 实例。对于大多数应用程序，建议使用 :ref:`FmodServer<FmodServer>` 的全局单例系统，而不是直接创建多个系统实例

.. _FmodSystem-init:

void init(max_channels: `int`_ = 32, flags: :ref:`FmodInitFlags<FmodInitFlags>` = 32)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

使用指定的最大通道数和初始化标志初始化 FMOD 系统

``max_channels`` 参数限制同时播放通道的总数（范围：0-4096）

``flags`` 参数是 :ref:`FmodInitFlags<FmodInitFlags>` 值的位掩码

.. _FmodSystem-close:

void close()
++++++++++++

关闭与输出设备的连接，并将系统恢复到未初始化状态，而不释放对象。可以通过再次调用 :ref:`init()<FmodSystem-init>` 来重新初始化系统

.. _FmodSystem-release:

void release()
++++++++++++++

关闭系统连接并释放所有相关资源。调用此方法后，系统对象不再有效，且不应再使用

.. _FmodSystem-update:

void update()
+++++++++++++

更新 FMOD 系统。这个方法应该定期调用（通常每帧一次），以处理流、3D 定位和非实时输出模式

当使用 :ref:`FmodInitFlags<FmodInitFlags>` 中的 ``FMOD_INIT_FLAG_STREAM_FROM_UPDATE`` 或 ``FMOD_INIT_FLAG_MIX_FROM_UPDATE`` 时，这个方法更为关键，因为它驱动音频处理

.. _FmodSystem-mixer_suspend:

void mixer_suspend()
++++++++++++++++++++

暂停混音器线程，同时释放音频硬件的使用权，但保持内部状态。在移动平台上处理音频焦点变化时非常有用

.. _FmodSystem-mixer_resume:

void mixer_resume()
+++++++++++++++++++

恢复混音器线程并重新获取对音频硬件的访问权限。在 :ref:`mixer_suspend()<FmodSystem-mixer_suspend>` 之后使用以恢复音频处理

设备选择
^^^^^^^^

.. _FmodSystem-set_output:

void set_output(output_type: :ref:`FmodOutputType<FmodOutputType>`)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置用于运行混音器的输出接口类型。必须在 init() 之前调用。

常用选项包括 ``FMOD_OUTPUT_TYPE_AUTODETECT``、 ``FMOD_OUTPUT_TYPE_WASAPI`` （Windows）和 ``FMOD_OUTPUT_TYPE_NOSOUND`` （静音模式）

.. _FmodSystem-get_output:

:ref:`FmodOutputType<FmodOutputType>` get_output() const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回当前用于运行混音器的选定输出接口类型

.. _FmodSystem-get_num_drivers:

`int`_ get_num_drivers() const
++++++++++++++++++++++++++++++

返回当前所选输出类型可用的输出驱动程序数量

.. _FmodSystem-get_driver_info:

`Dictionary`_ get_driver_info(id: `int`_) const
+++++++++++++++++++++++++++++++++++++++++++++++

返回指定索引的声音设备的识别信息。

返回的字典包含：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - name
    - `String`_
    - 设备的名称
  * - guid
    - `String`_
    - 设备的唯一标识符，格式为 ``{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}``
  * - system_rate
    - `int`_
    - 设备的默认采样率
  * - speaker_mode
    - :ref:`FmodSpeakerMode<FmodSpeakerMode>`
    - 默认扬声器模式
  * - speaker_mode_channels
    - `int`_
    - 默认扬声器模式下的通道数

.. _FmodSystem-set_driver:

void set_driver(driver: `int`_)
+++++++++++++++++++++++++++++++

设置当前选定输出类型的输出驱动程序。使用 :ref:`get_driver_info()<FmodSystem-get_driver_info>` 枚举可用的驱动程序

.. _FmodSystem-get_driver:

`int`_ get_driver() const
+++++++++++++++++++++++++

返回当前选定输出类型的活动输出驱动程序的索引

常规设置
^^^^^^^^

.. _FmodSystem-set_software_format:
  
void set_software_format(sample_rate: `int`_, speaker_mode: :ref:`FmodSpeakerMode<FmodSpeakerMode>`, num_raw_speakers: `int`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置软件混音器的输出格式

- ``sample_rate`` —— 输出采样率，单位为赫兹（通常为44100或48000）
- ``speaker_mode`` —— 扬声器输出配置（立体声、5.1声道等）
- ``num_raw_speakers`` —— 原始扬声器模式下的扬声器数量

.. warning:: 必须在调用 :ref:`init()<FmodSystem-init>` 之前调用

.. _FmodSystem-get_software_format:

`Dictionary`_ get_software_format() const
+++++++++++++++++++++++++++++++++++++++++

以字典形式返回当前的软件格式设置

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - sample_rate
    - `int`_
    - 当前输出采样率
  * - speaker_mode
    - :ref:`FmodSpeakerMode<FmodSpeakerMode>`
    - 当前扬声器输出配置
  * - num_raw_speakers
    - `int`_
    - 原始扬声器模式下的扬声器数量

.. _FmodSystem-set_dsp_buffer_size:

void set_dsp_buffer_size(buffer_length: `int`_, num_buffers: `int`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置软件混音器的 DSP 缓冲区大小

较小的缓冲区可以减少延迟，但会增加 CPU 使用率并增加音频中断的风险

.. warning:: 必须在 :ref:`init()<FmodSystem-init>` 之前调用

.. _FmodSystem-get_dsp_buffer_size:

`Dictionary`_ get_dsp_buffer_size() const
+++++++++++++++++++++++++++++++++++++++++

返回当前 DSP 缓冲区大小设置，格式为字典，包括：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - buffer_length
    - `int`_
    - 每个缓冲区的样本长度
  * - num_buffers
    - `int`_
    - 环形缓冲区中的缓冲区数量

.. _FmodSystem-set_stream_buffer_size:

void set_stream_buffer_size(file_buffer_size: `int`_ = 16384, file_buffer_size_type: :ref:`FmodTimeUnit<FmodTimeUnit>` = FMOD_TIME_UNIT_RAWBYTES)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置流式声音的默认缓冲区大小

这会影响为流式音频文件预读的数据量

.. _FmodSystem-get_stream_buffer_size:

`Dictionary`_ get_stream_buffer_size() const
++++++++++++++++++++++++++++++++++++++++++++

以字典的形式返回当前流缓冲区大小设置，包括：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - file_buffer_size
    - `int`_
    - 流缓冲区的大小
  * - file_buffer_size_type
    - :ref:`FmodTimeUnit<FmodTimeUnit>`
    - 缓冲区大小使用的时间单位
  
.. _FmodSystem-set_speaker_position:

void set_speaker_position(speaker: :ref:`FmodSpeaker<FmodSpeaker>`, x: `float`_, y: `float`_, active: `bool`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置扬声器在扬声器配置中的位置

这允许为非标准扬声器设置自定义扬声器位置

位置是相对于听者以二维坐标指定的

.. _FmodSystem-get_speaker_position:

`Dictionary`_ get_speaker_position(speaker: :ref:`FmodSpeaker<FmodSpeaker>`) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回指定扬声器的位置，作为一个字典，包括：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - x
    - `float`_
    - X 坐标
  * - y
    - `float`_
    - Y 坐标
  * - active
    - `bool`_
    - 扬声器是否激活

网络配置
^^^^^^^^

.. _FmodSystem-set_network_proxy:

void set_network_proxy(proxy: `String`_)
++++++++++++++++++++++++++++++++++++++++

为所有后续的互联网流连接设置代理服务器 URL

传递空字符串以禁用代理

.. note::
  以 host:port 格式指定代理，例如 ``www.fmod.com:8888`` （如果未指定端口，则默认为端口 80）

  基本身份验证支持使用 ``user:password@host:port`` 格式，例如 ``bob:sekrit123@www.fmod.com:8888``

.. _FmodSystem-get_network_proxy:

`String`_ get_network_proxy() const
+++++++++++++++++++++++++++++++++++

返回用于互联网流媒体连接的代理服务器的 URL

.. _FmodSystem-set_network_timeout:

void set_network_timeout(timeout: `int`_)
+++++++++++++++++++++++++++++++++++++++++

设置网络流的超时时间（以毫秒为单位）。这会影响 FMOD 在将流视为停滞之前等待数据的时间
  
.. _FmodSystem-get_network_timeout:

`int`_ get_network_timeout() const
++++++++++++++++++++++++++++++++++

返回网络流的超时时间（以毫秒为单位）

系统信息
^^^^^^^^

.. _FmodSystem-get_version:

`Dictionary`_ get_version() const
+++++++++++++++++++++++++++++++++

返回 FMOD 版本信息

返回的字典包含：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - version
    - `String`_
    - FMOD 版本字符串的格式为 ``product.major.minor``
  * - build_number
    - `String`_
    - FMOD 构建号字符串

.. _FmodSystem-get_output_handle:

`int`_ get_output_handle() const
++++++++++++++++++++++++++++++++

返回输出类型特定的本地句柄。对于 Windows，这通常是 WASAPI 或 DirectSound 设备句柄

这对于需要直接访问底层音频设备的高级用户很有用

.. _FmodSystem-get_channels_playing:

`Dictionary`_ get_channels_playing() const
++++++++++++++++++++++++++++++++++++++++++

返回一个包含当前播放频道信息的字典

返回的字典包含：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - channels
    - `int`_
    - 当前正在播放的频道总数
  * - real_channels
    - `int`_
    - 实际可听的声道数量

声音与获取
^^^^^^^^^^

.. _FmodSystem-create_sound_from_file:

:ref:`FmodSound<FmodSound>` create_sound_from_file(path: `String`_, mode: `int`_) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

从文件路径创建一个 :ref:`FmodSound<FmodSound>`。如果路径以 ``res://`` 开头，它将内部使用 :ref:`create_sound_from_res()<FmodSystem-create_sound_from_res>`

``mode`` 参数使用 :ref:`FmodMode<FmodMode>` 标志指定创建选项

.. _FmodSystem-create_sound_from_memory:

:ref:`FmodSound<FmodSound>` create_sound_from_memory(data: PackedByteArray, mode: `int`_) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

从内存中加载的音频数据创建一个 :ref:`FmodSound<FmodSound>`，它会自动添加 ``FMOD_MODE_OPENMEMORY`` 标志。音频数据数组在声音使用期间必须保持有效。这对于从加密文件或网络流加载声音非常有用

``mode`` 参数使用 :ref:`FmodMode<FmodMode>` 标志指定创建选项

.. _FmodSystem-create_sound_from_res:

:ref:`FmodSound<FmodSound>` create_sound_from_res(path: `String`_, mode: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

从 Godot 资源路径（以 ``res://`` 开头）创建一个 :ref:`FmodSound<FmodSound>`，它会内部使用 :ref:`create_sound_from_memory()<FmodSystem-create_sound_from_memory>` 方法。文件通过 Godot 的文件系统加载进内存，然后传递给 FMOD

``mode`` 参数使用 :ref:`FmodMode<FmodMode>` 标志指定创建选项

.. _FmodSystem-create_stream_from_file:

:ref:`FmodSound<FmodSound>` create_stream_from_file(path: `String`_, mode: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

从文件创建一个流式 :ref:`FmodSound<FmodSound>`。流式会即时解码音频数据，对于像背景音乐这样的大文件非常节省内存

``mode`` 参数使用 :ref:`FmodMode<FmodMode>` 标志指定创建选项

.. _FmodSystem-create_dsp:

:ref:`FmodDSP<FmodDSP>` create_dsp(name: `String`_) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

使用指定的名称创建自定义 DSP 效果。创建的 DSP 可以插入信号链中以实时处理音频

.. _FmodSystem-create_dsp_by_type:

:ref:`FmodDSP<FmodDSP>` create_dsp_by_type(type: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

创建指定内置类型的 DSP 效果。使用 :ref:`get_dsp_info_by_type()<FmodSystem-get_dsp_info_by_type>` 查询可用的 DSP 类型及其信息

.. _FmodSystem-create_channel_group:

:ref:`FmodChannelGroup<FmodChannelGroup>` create_channel_group(name: `String`_) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

使用指定的名称创建一个新的 :ref:`FmodChannelGroup<FmodChannelGroup>`。通道组允许您组织通道，以便对音量、音调和效果进行集体控制

.. _FmodSystem-create_sound_group:

:ref:`FmodSoundGroup<FmodSoundGroup>` create_sound_group(name: `String`_) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

使用指定的名称创建一个新的 :ref:`FmodSoundGroup<FmodSoundGroup>`

声音组允许您将声音组织到具有共享播放限制和集体控制的类别中

对于管理武器声音、环境声音或具有最大可听限制的对话非常有用

.. _FmodSystem-create_reverb_3d:

:ref:`FmodReverb3D<FmodReverb3D>` create_reverb_3d() const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

创建一个用于空间音频混响效果的3D混响区域

返回一个 :ref:`FmodReverb3D<FmodReverb3D>` 对象，该对象可以在3D空间中定位并配置混响参数

使用此功能可以创建如洞穴、礼堂或房间等环境音效
  
.. _FmodSystem-play_sound:

:ref:`FmodChannel<FmodChannel>` play_sound(sound: :ref:`FmodSound<FmodSound>`, channel_group: :ref:`FmodChannelGroup<FmodChannelGroup>`, paused: `bool`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

在一个通道上播放声音，通过指定的通道组路由

如果 ``paused`` 为 ``true``，通道将以暂停状态开始，直到调用 :ref:`FmodChannel.set_paused()<FmodChannel-set_paused>` 并传入 ``false`` 才会产生声音

返回一个 :ref:`FmodChannel<FmodChannel>` 句柄，可用于控制播放
  
.. _FmodSystem-play_dsp:

FmodChannel play_dsp(dsp: :ref:`FmodDSP<FmodDSP>`, channel_group: :ref:`FmodChannelGroup<FmodChannelGroup>`, paused: `bool`_) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

在通道上播放 DSP 及其输入信号，通过指定的通道组路由

如果 ``paused`` 为 ``true``，通道将以暂停状态开始，并且在调用 :ref:`FmodChannel.set_paused()<FmodChannel-set_paused>` 并传入 ``false`` 之前不会发出声音
  
返回一个 :ref:`FmodChannel<FmodChannel>` 句柄，可用于控制播放
  
.. _FmodSystem-get_channel:

FmodChannel get_channel(id: `int`_) const
+++++++++++++++++++++++++++++++++++++++++

通过其 ID 检索 :ref:`FmodChannel<FmodChannel>` 句柄。通道在分配时会按顺序分配 ID
  
.. _FmodSystem-get_dsp_info_by_type:

`Dictionary`_ get_dsp_info_by_type(type: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++

检索有关内置 DSP 类型的信息

返回的字典包含：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - name
    - `String`_
    - DSP 的名称
  * - version
    - `int`_
    - 插件版本号
  * - plugin_sdk_version
    - `int`_
    - FMOD 插件 SDK 版本
  * - num_input_buffers
    - `int`_
    - 输入缓冲区数量
  * - num_output_buffers
    - `int`_
    - 输出缓冲区数量
  * - has_create
    - `bool`_
    - DSP 是否有创建回调
  * - has_release
    - `bool`_
    - DSP 是否有释放回调
  * - has_reset
    - `bool`_
    - DSP 是否有重置回调
  * - has_setposition
    - `bool`_
    - DSP 是否有设置位置回调
  * - has_read
    - `bool`_
    - DSP 是否有读取回调
  * - has_should_i_process
    - `bool`_
    - DSP 是否有在实际处理前的回调
  
.. _FmodSystem-get_master_channel_group:

:ref:`FmodChannelGroup<FmodChannelGroup>` get_master_channel_group() const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回所有声音最终路由到的主通道组。使用它来控制全局音量、添加主效果或监控整体输出
  
.. _FmodSystem-get_master_sound_group:

:ref:`FmodSoundGroup<FmodSoundGroup>` get_master_sound_group() const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回所有声音默认所属的主声音组

主声音组可用于设置全局播放限制并控制所有声音的整体行为

运行控制
^^^^^^^^

.. _FmodSystem-set_3d_listener_attributes:

void set_3d_listener_attributes(listener: `int`_, position: `Vector3`_, velocity: `Vector3`_, forward: `vector3`_, up: `Vector3`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置3D监听器的位置、速度和方向

监听器索引指定要配置的监听器（用于多监听器设置）

- ``position`` —— 听者的世界位置
- ``velocity`` —— 听者的速度，用于多普勒计算
- ``forward`` —— 听者的前向量
- ``up`` —— 听者的上向量

.. _FmodSystem-get_3d_listener_attributes:

`Dictionary`_ get_3d_listener_attributes(listener: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

以字典形式返回指定监听器的 3D 属性：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - position
    - `Vector3`_
    - 听者的世界位置
  * - velocity
    - `Vector3`_
    - 听者的速度，用于多普勒计算
  * - forward
    - `Vector3`_
    - 听者的前向量
  * - up
    - `Vector3`_
    - 听者的上向量

.. _FmodSystem-set_reverb_properties:

void set_reverb_properties(instance: `int`_, decay_time: `float`_, early_delay: `float`_, late_delay: `float`_, hf_reference: `float`_, hf_decay_ratio: `float`_, diffusion: `float`_, density: `float`_, low_shelf_frequency: `float`_, low_shelf_gain: `float`_, high_cut: `float`_, early_late_mix: `float`_, wet_level: `float`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置指定混响实例的混响属性

混响实例 ID 是通过 :ref:`create_reverb_3d()<FmodSystem-reate_reverb_3d>` 创建的 :ref:`FmodReverb3D` 对象的 ID

- ``decay_time`` —— 混响衰减时间，单位为毫秒
- ``early_delay`` —— 早期反射的延迟时间，单位为毫秒
- ``late_delay`` —— 后期反射的延迟时间，单位为毫秒
- ``hf_reference`` —— 高频衰减参考频率，单位为赫兹
- ``hf_decay_ratio`` —— 高频衰减时间与整体衰减时间的比率
- ``diffusion`` —— 混响扩散程度
- ``density`` —— 混响密度
- ``low_shelf_frequency`` —— 低通滤波器频率，单位为赫兹
- ``low_shelf_gain`` —— 低通滤波器增益，单位为分贝
- ``high_cut`` —— 混响高频截止频率，单位为赫兹
- ``early_late_mix`` —— 早期反射与后期反射的混合比例
- ``wet_level`` —— 湿信号（混响）级别，单位为分贝

.. _FmodSystem-get_reverb_properties:

`Dictionary`_ get_reverb_properties(instance: `int`_) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

以字典形式返回指定全局混响实例的混响属性，包括所有参数：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - decay_time
    - `float`_
    - 混响衰减时间，单位为毫秒，默认 1500 毫秒，范围：0-20000 毫秒
  * - early_delay
    - `float`_
    - 早期反射的延迟时间，单位为毫秒，默认 7 毫秒，范围：0-300 毫秒
  * - late_delay
    - `float`_
    - 后期反射的延迟时间，单位为毫秒，默认 11 毫秒，范围：0-100 毫秒
  * - hf_reference
    - `float`_
    - 高频衰减参考频率，单位为赫兹，默认 5000 赫兹，范围：20-20000 赫兹
  * - hf_decay_ratio
    - `float`_
    - 高频衰减时间与整体衰减时间的比率，默认 50%，范围：10-100%
  * - diffusion
    - `float`_
    - 混响扩散程度，默认 50%，范围 10-100%
  * - density
    - `float`_
    - 混响密度，默认 100%，范围 0-100%
  * - low_shelf_frequency
    - `float`_
    - 低架滤波器频率，单位为赫兹，默认 250 赫兹，范围：20-1000赫兹
  * - low_shelf_gain
    - `float`_
    - 低架滤波器增益，单位为分贝，默认 0 分贝，范围：-36-12 分贝
  * - high_cut
    - `float`_
    - 混响高频截止频率，单位为赫兹，默认 20000 赫兹，范围：0-20000
  * - early_late_mix
    - `float`_
    - 早期反射与后期反射的混合比例，默认 50%，范围：0-100%
  * - wet_level
    - `float`_
    - 湿信号（混响）级别，单位为分贝，默认 -6 分贝，范围：-80-20 分贝

.. _FmodSystem-attach_channel_group_to_port:

void attach_channel_group_to_port(channel_group: :ref:`FmodChannelGroup<FmodChannelGroup>`, prot_type: :ref:`FmodPortType<FmodPortType>`, port_index: `int`_ = -1, pass_thru: `bool`_ = false)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

将通道组的输出附加到输出驱动器上的音频端口

这允许将音频路由到特定的输出目标，例如控制器扬声器或辅助输出

.. seealso:: :ref:`FmodPortType<FmodPortType>` 了解可用的端口类型

.. _FmodSystem-detach_channel_group_from_port:

void detach_channel_group_from_port(channel_group: :ref:`FmodChannelGroup<FmodChannelGroup>`)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

将通道组从其分配的音频端口中分离

通道组将恢复到主输出的正常路由

录音
^^^^

.. _FmodSystem-get_record_num_drivers:

`Dictionary`_ get_record_num_drivers() const
++++++++++++++++++++++++++++++++++++++++++++

返回有关可用录音设备的信息

返回的字典包含：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - num_drivers
    - 可用录音设备的总数
  * - num_connected
    - 当前连接的录音设备数量
  
.. _FmodSystem-get_record_driver_info:

`Dictionary`_ get_record_driver_info(id: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回由其索引指定的录音设备的识别信息

返回的字典包含：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - name
    - `String`_
    - 录音设备的名称
  * - guid
    - `String`_
    - 设备的唯一标识符，格式为 ``{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}``
  * - system_rate
    - `int`_
    - 设备的默认采样率
  * - speaker_mode
    - :ref:`FmodSpeakerMode<FmodSpeakerMode>`
    - 扬声器模式
  * - speaker_mode_channels
    - `int`_
    - 通道数量
  * - state
    - `int`_
    - 驱动状态标志（1 为已连接，2 为默认）
  
.. _FmodSystem-get_record_position:

`int`_ get_record_position(id: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++

返回指定录音设备的当前 PCM 采样录音位置
  
.. _FmodSystem-record_start:

void record_start(id: `int`_, sound: FmodSound, loop: `bool`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

从指定设备开始录音到提供的音频对象中

如果 ``loop`` 为 ``true``，当录音达到缓冲区末尾时，会从音频缓冲区的开头重新开始录音
  
.. _FmodSystem-record_stop:

void record_stop(id: `int`_)
++++++++++++++++++++++++++++

停止从指定设备录制
  
.. _FmodSystem-is_recording:

`bool`_ is_recording(id: `int`_) const
++++++++++++++++++++++++++++++++++++++

如果指定的录音设备当前正在录音，则返回 ``true``

几何管理
^^^^^^^^

.. _FmodSystem-create_geometry:

:ref:`FmodGeometry<FmodGeometry>` create_geometry(max_polygons: `int`_ = 9999, max_vertices: `int`_ = 9999) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

为 3D 遮挡计算创建一个几何体对象，用于模拟场景中物理物体对声音的遮挡

- ``max_polygons`` —— 参数指定几何体中允许的最大多边形数量
- ``max_vertices`` —— 参数指定几何体中允许的最大顶点数量

.. _FmodSystem-load_geometry:

:ref:`FmodGeometry<FmodGeometry>` load_geometry(data: `PackedByteArray`_) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

从提供的 **PackedByteArray** 加载几何数据并创建一个 :ref:`FmodGeometry<FmodGeometry>` 对象，对于从磁盘加载复杂几何形状非常有用

.. warning:: 数据格式必须符合 FMOD 的几何数据规范，通常包含顶点和多边形信息
  
.. _FmodSystem-get_geometry_occlusion:

`Dictionary`_ get_geometry_occlusion(listener: `Vector3`_, source: `Vector3`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

计算听者与声源位置之间的遮挡情况

返回的字典包含：

.. list-table::
  :header-rows: 1

  * - 键名
    - 类型
    - 说明
  * - direct
    - `float`_
    - 直接声音的遮挡值（0.0-1.0）
  * - reverb
    - `float`_
    - 混响声音的遮挡值（0.0-1.0）
    
.. note:: 如果已经创建了单面多边形，重要的是要正确获取源和监听器的位置，因为从点A到点B的遮挡可能与从点B到点A的遮挡不同

其它
^^^^

.. _FmodSystem-lock_dsp:

void lock_dsp()
+++++++++++++++

锁住 DSP 引擎互斥锁

在需要原子操作的多次DSP调用时使用，这对于确保在执行这些调用时 DSP 处理不会被中断非常有用

.. warning:: 始终与 :ref:`unlock_dsp()<FmodSystem-unlock_dsp>` 配对使用

.. _FmodSystem-unlock_dsp:

void unlock_dsp()
+++++++++++++++++

解锁 DSP 引擎互斥锁

.. warning:: 必须在 :ref:`unlock_dsp()<FmodSystem-lock_dsp>` 之后调用

枚举
~~~~

.. _FmodInitFlags:

FmodInitFlags
^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_INIT_FLAG_NORMAL
    - 0
    - 正常初始化
  * - FMOD_INIT_FLAG_STREAM_FROM_UPDATE
    - 1
    - 内部不创建流线程。流由 :ref:`FmodSystem.update()<FmodSystem-update>` 驱动。主要用于非实时输出
  * - FMOD_INIT_FLAG_MIX_FROM_UPDATE
    - 2
    - 内部不创建混合线程。混合由 :ref:`FmodSystem.update()<FmodSystem-update>` 驱动。仅适用于基于轮询的输出模式，如 :ref:`FmodOutputType` 中的 ``FMOD_OUTPUT_TYPE_NOSOUND``、 ``FMOD_OUTPUT_TYPE_WAVWRITER``
  * - FMOD_INIT_FLAG_3D_RIGHTHANDED
    - 4
    - 三维计算将采用右手坐标进行，而非默认的左手坐标。更多信息请参见词汇表的“惯性”部分
  * - FMOD_INIT_FLAG_CLIP_OUTPUT
    - 8
    - 支持对输出值大于1.0f或小于-1.0f进行硬削波
  * - FMOD_INIT_FLAG_CHANNEL_LOWPASS
    - 256
    - 启用 ChannelControl::setLowPassGain、ChannelControl::set3DOcclusion，或 Geometry API 的自动使用。所有语音都会在 DSP 链中添加软件低通滤波效果，除非使用上述功能或特性，否则该效果处于空闲状态
  * - FMOD_INIT_FLAG_CHANNEL_DISTANCEFILTER
    - 512
    - 所有基于 :ref:`FmodMode` 中的 ``FMOD_MODE_3D`` 的语音都会在DSP链中添加软件低通和高通滤波效果，作为距离自动带通滤波器。请调整 FmodSystem 属性来处理中心频率
  * - FMOD_INIT_FLAG_PROFILE_ENABLE
    - 65536
    - 启用基于TCP/IP的主机，允许FMOD Studio或FMOD Profiler连接，实时查看内存、CPU 和 DSP 图表
  * - FMOD_INIT_FLAG_VOL0_BECOMES_VIRTUAL
    - 131072
    - 任何音量为0的声音都会变成虚拟声音，除了它们的位置在虚拟中更新外不会被处理。请调整 FmodSystem 属性来处理除了 0 以外的音量切换到虚拟
  * - FMOD_INIT_FLAG_GEOMETRY_USECLOSEST
    - 262144
    - 使用几何引擎时，只需处理最近的多边形，而不是累积所有声音到听者线路相交的多边形
  * - FMOD_INIT_FLAG_PREFER_DOLBY_DOWNMIX
    - 524288
    - 使用立体声输出设备 :ref:`FmodSpeakerMode` 中的 ``FMOD_SPEAKER_MODE_5POINT1`` 时，请使用 Dolby Pro Logic II 的下混算法，而非默认的立体声下混算法
  * - FMOD_INIT_FLAG_THREAD_UNSAFE
    - 1048576
    - 禁用 API 调用的线程安全。只有在从 FMOD 从单线程调用且未使用 Studio API 时才使用！
  * - FMOD_INIT_FLAG_PROFILE_METER_ALL
    - 2097152
    - 虽然速度较慢，但可以为图表中的每个DSP单元添加电平计量。使用DSP::setMeteringEnable来单独关闭电表。设置这个标志意味着有 ``FMOD_INIT_PROFILE_ENABLE``
  * - FMOD_INIT_FLAG_MEMORY_TRACKING
    - 4194304
    - 启用内存分配追踪。目前仅在使用 Studio API 时有效。增加内存占用并降低性能。该标志由 `FMOD_STUDIO_INIT_MEMORY_TRACKING <https://www.fmod.com/docs/2.02/api/studio-api-system.html#fmod_studio_init_memory_tracking>`_ 隐含
  
.. seealso:: :ref:`FmodSystem.init()<FmodSystem-init>` 来初始化 FMOD 系统

.. _FmodOutputType:

FmodOutputType
^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 平台
    - 说明
  * - FMOD_OUTPUT_TYPE_AUTODETECT
    - 0
    - 全部
    - 选择平台的最佳输出模式，这是默认的
  * - FMOD_OUTPUT_TYPE_UNKNOWN
    - 1
    - --
    - 仅用于 :ref:`FmodSystem.get_output()<FmodSystem-get_output>`
  * - FMOD_OUTPUT_TYPE_NOSOUND
    - 2
    - 全部
    - 执行所有混音，但丢弃最终输出
  * - FMOD_OUTPUT_TYPE_WAVWRITER
    - 3
    - 全部
    - 将输出写入.wav文件
  * - FMOD_OUTPUT_TYPE_NOSOUND_NRT
    - 4
    - 全部
    - 非实时版本的 ``FMOD_OUTPUT_TYPE_NOSOUND``，每个系统更新一次混音
  * - FMOD_OUTPUT_TYPE_WAVWRITER_NRT
    - 5
    - 全部
    - 非实时版本的 ``FMOD_OUTPUT_TYPE_WAVWRITER``，每个系统更新一次混音
  * - FMOD_OUTPUT_TYPE_WASAPI
    - 6
    - Win、UWP、Xbox One、Game Core
    - Windows 音频会话 API（Windows、Xbox One、Game Core 和 UWP 默认使用）
  * - FMOD_OUTPUT_TYPE_ASIO
    - 7
    - Win
    - 低延迟ASIO 2.0
  * - FMOD_OUTPUT_TYPE_PULSEAUDIO
    - 8
    - Linux
    - 脉冲音频（如果有，默认使用 Linux 版本）
  * - FMOD_OUTPUT_TYPE_ALSA
    - 9
    - Linux
    - 高级 Linux 声音架构（如果 Linux 上没有 PulseAudio，默认使用 Linux 版本）
  * - FMOD_OUTPUT_TYPE_COREAUDIO
    - 10
    - Mac、iOS
    - 核心音频（Mac 和 iOS 默认）
  * - FMOD_OUTPUT_TYPE_AUDIOTRACK
    - 11
    - Android
    - Java 音频轨（Android 2.2及以下默认）
  * - FMOD_OUTPUT_TYPE_OPENSL
    - 12
    - Android
    - OpenSL ES（默认支持 Android 2.3 至 7.1）
  * - FMOD_OUTPUT_TYPE_AUDIOOUT
    - 13
    - PS4、PS5
    - 音频输出（PS4、PS5默认）
  * - FMOD_OUTPUT_TYPE_AUDIO3D
    - 14
    - PS4
    - Audio3D
  * - FMOD_OUTPUT_TYPE_WEBAUDIO
    - 15
    - HTML5
    - Web Audio ScriptProcessorNode 输出（如果 AudioWorkletNode 不可用，默认为 HTML5）
  * - FMOD_OUTPUT_TYPE_NNAUDIO
    - 16
    - Nintendo Switch
    - 音频输出（Switch默认）
  * - FMOD_OUTPUT_TYPE_WINSONIC
    - 17
    - Win10、Xbox One、Game Core
    - Windows Sonic
  * - FMOD_OUTPUT_TYPE_AAUDIO
    - 18
    - Android
    - AAudio（Android 8.1及以上默认）
  * - FMOD_OUTPUT_TYPE_AUDIOWORKLET
    - 19
    - HTML5
    - Web Audio AudioWorkletNode 输出（如果有，默认为 HTML5）
  * - FMOD_OUTPUT_TYPE_PHASE
    - 20
    - iOS
    - PHASE 框架（禁用）
  * - FMOD_OUTPUT_TYPE_OHAUDIO
    - 21
    - OpenHarmony
    - OHAudio
  * - FMOD_OUTPUT_TYPE_MAX
    - 22
    - --
    - 支持的最大输出类型数量
  * - FMOD_OUTPUT_TYPE_FORCEINT
    - 65536
    - --
    - 将枚举强制为 32 位大小

.. _FmodSpeaker:

FmodSpeaker
^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_SPEAKER_NONE
    - -1
    - 未指定扬声器
  * - FMOD_SPEAKER_FRONT_LEFT
    - 0
    - 前置左声道
  * - FMOD_SPEAKER_FRONT_RIGHT
    - 1
    - 前置右声道
  * - FMOD_SPEAKER_FRONT_CENTER
    - 2
    - 前置中置声道
  * - FMOD_SPEAKER_LOW_FREQUENCY
    - 3
    - 低频效果声道
  * - FMOD_SPEAKER_SURROUND_LEFT
    - 4
    - 环绕左声道
  * - FMOD_SPEAKER_SURROUND_RIGHT
    - 5
    - 环绕右声道
  * - FMOD_SPEAKER_BACK_LEFT
    - 6
    - 后置左声道
  * - FMOD_SPEAKER_BACK_RIGHT
    - 7
    - 后置右声道
  * - FMOD_SPEAKER_TOP_FRONT_LEFT
    - 8
    - 顶部前左声道
  * - FMOD_SPEAKER_TOP_FRONT_RIGHT
    - 9
    - 顶部前右声道
  * - FMOD_SPEAKER_TOP_BACK_LEFT
    - 10
    - 顶部后左声道
  * - FMOD_SPEAKER_TOP_BACK_RIGHT
    - 11
    - 顶部后右声道
  * - FMOD_SPEAKER_MAX
    - 12
    - 扬声器枚举数量
  * - FMOD_SPEAKER_FORCEINT
    - 65536
    - 强制枚举为 32 位整数

.. _FmodSpeakerMode:

FmodSpeakerMode
^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_SPEAKER_MODE_DEFAULT
    - 0
    - 平台默认扬声器模式
  * - FMOD_SPEAKER_MODE_RAW
    - 1
    - 原始扬声器映射
  * - FMOD_SPEAKER_MODE_MONO
    - 2
    - 单声道输出
  * - FMOD_SPEAKER_MODE_STEREO
    - 3
    - 立体声输出
  * - FMOD_SPEAKER_MODE_QUAD
    - 4
    - 四声道输出
  * - FMOD_SPEAKER_MODE_SURROUND
    - 5
    - 五声道环绕输出
  * - FMOD_SPEAKER_MODE_5POINT1
    - 6
    - 5.1 环绕输出
  * - FMOD_SPEAKER_MODE_7POINT1
    - 7
    - 7.1 环绕输出
  * - FMOD_SPEAKER_MODE_7POINT1POINT4
    - 8
    - 7.1.4 沉浸式输出
  * - FMOD_SPEAKER_MODE_MAX
    - 9
    - 扬声器模式数量
  * - FMOD_SPEAKER_FORCEINT
    - 65536
    - 强制枚举为 32 位整数

.. _FmodMode:

FmodMode
^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_MODE_DEFAULT
    - 0
    - 默认创建模式
  * - FMOD_MODE_LOOP_OFF
    - 1
    - 禁用循环播放
  * - FMOD_MODE_LOOP_NORMAL
    - 2
    - 正常循环播放
  * - FMOD_MODE_LOOP_BIDI
    - 4
    - 双向循环播放
  * - FMOD_MODE_2D
    - 8
    - 作为 2D 声音播放
  * - FMOD_MODE_3D
    - 16
    - 作为 3D 声音播放
  * - FMOD_MODE_CREATESTREAM
    - 128
    - 创建流式声音
  * - FMOD_MODE_CREATESAMPLE
    - 256
    - 创建解压采样
  * - FMOD_MODE_CREATECOMPRESSEDSAMPLE
    - 512
    - 创建压缩采样
  * - FMOD_MODE_OPENUSER
    - 1024
    - 使用用户回调打开
  * - FMOD_MODE_OPENMEMORY
    - 2048
    - 从内存数据打开
  * - FMOD_MODE_OPENMEMORY_POINT
    - 268435456
    - 直接引用内存数据
  * - FMOD_MODE_OPENRAW
    - 4096
    - 按原始 PCM 数据打开
  * - FMOD_MODE_OPENONLY
    - 8192
    - 仅打开不预载
  * - FMOD_MODE_ACCURATETIME
    - 16384
    - 精确计算长度
  * - FMOD_MODE_MPEGSEARCH
    - 32768
    - 扫描 MPEG 帧信息
  * - FMOD_MODE_NONBLOCKING
    - 65536
    - 非阻塞方式打开
  * - FMOD_MODE_UNIQUE
    - 131072
    - 创建唯一声音实例
  * - FMOD_MODE_3D_HEADRELATIVE
    - 262144
    - 3D 位置相对听者
  * - FMOD_MODE_3D_WORLDRELATIVE
    - 524288
    - 3D 位置相对世界
  * - FMOD_MODE_3D_INVERSEROLLOFF
    - 1048576
    - 反比距离衰减
  * - FMOD_MODE_3D_LINEARROLLOFF
    - 2097152
    - 线性距离衰减
  * - FMOD_MODE_3D_LINEARSQUAREROLLOFF
    - 4194304
    - 线性平方距离衰减
  * - FMOD_MODE_3D_INVERSETAPEREDROLLOFF
    - 8388608
    - 锥形反比距离衰减
  * - FMOD_MODE_3D_CUSTOMROLLOFF
    - 67108864
    - 自定义距离衰减
  * - FMOD_MODE_3D_IGNOREGEOMETRY
    - 1073741824
    - 忽略几何遮挡
  * - FMOD_MODE_IGNORETAGS
    - 33554432
    - 忽略文件标签
  * - FMOD_MODE_LOWMEM
    - 134217728
    - 使用低内存模式
  * - FMOD_MODE_VIRTUAL_PLAYFROMSTART
    - -2147483648
    - 虚拟声道从头播放

.. _FmodTimeUnit:

FmodTimeUnit
^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_TIME_UNIT_MS
    - 1
    - 毫秒时间单位
  * - FMOD_TIME_UNIT_PCM
    - 2
    - PCM 采样单位
  * - FMOD_TIME_UNIT_PCMBYTES
    - 4
    - PCM 字节单位
  * - FMOD_TIME_UNIT_RAWBYTES
    - 8
    - 原始字节单位
  * - FMOD_TIME_UNIT_PCMFRACTION
    - 16
    - PCM 小数位置单位
  * - FMOD_TIME_UNIT_MODORDER
    - 256
    - 模块音乐顺序单位
  * - FMOD_TIME_UNIT_MODROW
    - 512
    - 模块音乐行单位
  * - FMOD_TIME_UNIT_MODPATTERN
    - 1024
    - 模块音乐样式单位

.. _FmodResamplerMethod:

FmodResamplerMethod
^^^^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_RESAMPLER_DEFAULT
    - 0
    - 默认重采样方式
  * - FMOD_RESAMPLER_NOINTERP
    - 1
    - 无插值重采样
  * - FMOD_RESAMPLER_LINEAR
    - 2
    - 线性插值重采样
  * - FMOD_RESAMPLER_CUBIC
    - 3
    - 三次插值重采样
  * - FMOD_RESAMPLER_SPLINE
    - 4
    - 样条插值重采样
  * - FMOD_RESAMPLER_MAX
    - 5
    - 重采样方式数量
  * - FMOD_RESAMPLER_FORCEINT
    - 65536
    - 强制枚举为 32 位整数

.. _FmodPortType:

FmodPortType
^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_PORT_TYPE_MUSIC
    - 0
    - 音乐输出端口
  * - FMOD_PORT_TYPE_COPYRIGHT_MUSIC
    - 1
    - 受版权保护音乐端口
  * - FMOD_PORT_TYPE_VOICE
    - 2
    - 语音输出端口
  * - FMOD_PORT_TYPE_CONTROLLER
    - 3
    - 控制器输出端口
  * - FMOD_PORT_TYPE_PERSONAL
    - 4
    - 个人音频输出端口
  * - FMOD_PORT_TYPE_VIBRATION
    - 5
    - 振动输出端口
  * - FMOD_PORT_TYPE_AUX
    - 6
    - 辅助输出端口
  * - FMOD_PORT_TYPE_PASSTHROUGH
    - 7
    - 直通输出端口
  * - FMOD_PORT_TYPE_VR_VIBRATION
    - 8
    - VR 振动输出端口
  * - FMOD_PORT_TYPE_MAX
    - 9
    - 端口类型数量
