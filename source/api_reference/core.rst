核心类 API
==========

.. _FmodServer:

FmodServer
----------

**管理 FMOD 音频系统生命周期的全局单例**

描述
~~~~

FmodServer 是一个全局单例，用于管理 Godot 中的 FMOD Core API 音频系统。它初始化并维护主 FMOD 系统实例，注册性能监控以跟踪 CPU 和文件使用情况，管理音频总线布局，并连接到 Godot 的 SceneTree 以进行每帧更新

服务器在 GDExtension 加载期间自动初始化，并处理所有 FMOD 生命周期管理。它创建的性能监控可以在 Godot 的调试器 > 监视器选项卡中查看，以跟踪 FMOD 的资源使用情况

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

.. note:: 这个类是单例。使用 ``get_singleton()`` 来访问实例，或者直接使用静态方法

方法
~~~~

.. list-table::

   * - void
     - generate_bus_layout() static
   * - :ref:`FmodAudioBusLayout<FmodAudioBusLayout>`
     - get_audio_bus_layout() static
   * - :ref:`FmodSystem<FmodSystem>`
     - get_main_system() static
   * - :ref:`FmodChannelGroup<FmodChannelGroup>`
     - get_master_channel_group() static
   * - :ref:`FmodServer<FmodServer>`
     - get_singleton() static
   * - void
     - reset_main_system(system: :ref:`FmodSystem<FmodSystem>`) static

方法说明
~~~~~~~~

.. glossary::

  void generate_bus_layout() static
    生成音频总线布局

    这将扫描 Godot 的 **AudioServer** 总线层级并创建对应的 **FmodAudioBusLayout** 和 **FmodAudioBus** 实例，以确保 FMOD 的总线结构与 Godot 的总线结构同步
  
  :ref:`FmodAudioBusLayout<FmodAudioBusLayout>` get_audio_bus_layout() static
    返回用于管理音频总线及其路由的音频总线布局。该总线布局与 Godot 的 AudioServer 总线布局同步，并提供 FMOD 特定的总线功能，包括 DSP 效果
  
  :ref:`FmodSystem<FmodSystem>` get_main_system() static
    返回主要的 FMOD 系统实例。这是创建声音、通道、DSP 效果和其他 FMOD 对象的主要接口。系统在服务器启动时会根据项目设置自动初始化
  
  :ref:`FmodChannelGroup<FmodChannelGroup>` get_master_channel_group() static
    返回默认情况下所有声音通过的主通道组。它是通道组层次结构的根，可以用于控制所有正在播放声音的全局音量、音高和效果
  
  :ref:`FmodServer<FmodServer>` get_singleton() static
    返回 **FmodServer** 单例实例。这是管理 FMOD 系统的全局实例。如果服务器尚未初始化，则返回 ``null``
  
  void reset_main_system(system: FmodSystem) static
    重置主 FMOD 系统实例（用于测试或重新初始化）

.. _FmodSystem:

FmodSystem
----------

**FMOD::System 对象的包装类，提供音频系统管理和控制**

描述
~~~~

FmodSystem 封装了 FMOD 核心 API 的 FMOD::System 对象，并提供全面的音频系统管理功能。该类负责系统初始化、音频设备管理、声音创建、播放控制以及录音功能

FMOD System 是 FMOD 音频引擎的核心。它管理混音器、音轨、声音、DSP 效果和输出设备。对于高级应用场景，可以创建多个 System 实例；对于常规应用，则可以通过 **FmodServer** 使用全局单例

属性
~~~~

.. list-table::

  * - `float`_
    - 3d_max_world_size
    - 1000.0
  * - `int`_
    - 3d_num_listeners
    - 1
  * - `int`_
    - asio_num_channels
    - 0
  * - `int`_
    - default_decode_buffer_size
    - 0
  * - `float`_
    - distance_factor
    - 1.0
  * - `float`_
    - distance_filter_center_freq
    - 0.0
  * - `float`_
    - doppler_scale
    - 1.0
  * - `int`_
    - dsp_buffer_pool_size
    - 0
  * - `int`_
    - geometry_max_fade_time
    - 0
  * - `int`_
    - max_adpcm_codecs
    - 0
  * - `int`_
    - max_at9_codecs
    - 0
  * - `int`_
    - max_convolution_threads
    - 0
  * - `int`_
    - max_fadpcm_codecs
    - 0
  * - `int`_
    - max_mpeg_codecs
    - 0
  * - `int`_
    - max_opus_codecs
    - 0
  * - `int`_
    - max_software_channels
    - 0
  * - `int`_
    - max_spatial_objects
    - 0
  * - `int`_
    - max_vobis_codecs
    - 0
  * - `int`_
    - max_xma_codecs
    - 0
  * - `int`_
    - profile_port
    - 0
  * - `int`_
    - random_seed
    - 0
  * - :ref:`FmodResamplerMethod<FmodResamplerMethod>`
    - resampler_method
    - 0
  * - `int`_
    - reverb_3d_instance
    - 0
  * - `float`_
    - rolloff_scale
    - 1.0
  * - `float`_
    - vol0_virtual_vol
    - 0.0

方法
~~~~

有效性检查
^^^^^^^^^^

.. list-table::

  * - `bool`_
    - system_is_null() const
  * - `bool`_
    - system_is_valid() const

系统管理
^^^^^^^^

.. list-table::

  * - :ref:`FmodSystem<FmodSystem>`
    - create_system() static
  * - void
    - init(max_channels: `int`_ = 32, flags: :ref:`FmodInitFlags<FmodInitFlags>` = 32)
  * - void
    - close()
  * - void
    - release()
  * - void
    - update()
  * - void
    - mixer_suspend()
  * - void
    - mixer_resume()

设备选择
^^^^^^^^

.. list-table::

  * - void
    - set_output(output_type: :ref:`FmodOutputType<FmodOutputType>`)
  * - :ref:`FmodOutputType<FmodOutputType>`
    - get_output() const
  * - `int`_
    - get_num_drivers() const
  * - `Dictionary`_
    - get_driver_info(id: `int`_) const
  * - void
    - set_driver(driver: `int`_)
  * - `int`_
    - get_driver() const

常规设置
^^^^^^^^

.. list-table::

  * - void
    - set_software_format(sample_rate: `int`_, speaker_mode: FmodSpeakerMode, num_raw_speakers: `int`_)
  * - `Dictionary`_
    - get_software_format() const
  * - void
    - set_dsp_buffer_size(buffer_length: `int`_, num_buffers: `int`_)
  * - `Dictionary`_
    - get_dsp_buffer_size() const
  * - void
    - set_stream_buffer_size(file_buffer_size: `int`_ = 16384, file_buffer_size_type: :ref:`FmodTimeUnit<FmodTimeUnit>` = FMOD_TIME_UNIT_RAWBYTES)
  * - `Dictionary`_
    - get_stream_buffer_size() const
  * - void
    - set_speaker_position(speaker: :ref:`FmodSpeaker<FmodSpeaker>`, x: `float`_, y: `float`_, active: `bool`_)
  * - `Dictionary`_
    - get_speaker_position(speaker: :ref:`FmodSpeaker<FmodSpeaker>`) const

网络配置
^^^^^^^^

.. list-table::

  * - void
    - set_network_proxy(proxy: `String`_)
  * - `String`_
    - get_network_proxy() const
  * - void
    - set_network_timeout(timeout: `int`_)
  * - `int`_
    - get_network_timeout() const

系统信息
^^^^^^^^

.. list-table::

  * - `Dictionary`_
    - get_version() const
  * - `int`_
    - get_output_handle() const
  * - `Dictionary`_
    - get_channels_playing() const

声音与获取
^^^^^^^^^^

.. list-table::

  * - :ref:`FmodSound<FmodSound>`
    - create_sound_from_file(path: `String`_, mode: `int`_) const
  * - :ref:`FmodSound<FmodSound>`
    - create_sound_from_memory(data: PackedByteArray, mode: `int`_) const
  * - :ref:`FmodSound<FmodSound>`
    - create_sound_from_res(path: `String`_, mode: `int`_) const
  * - :ref:`FmodSound<FmodSound>`
    - create_stream_from_file(path: `String`_, mode: `int`_) const
  * - FmodDSP
    - create_dsp(name: `String`_) const
  * - FmodDSP
    - create_dsp_by_type(type: `int`_) const
  * - FmodChannelGroup
    - create_channel_group(name: `String`_) const
  * - FmodSoundGroup
    - create_sound_group(name: `String`_) const
  * - FmodReverb3D
    - create_reverb_3d() const
  * - FmodChannel
    - play_sound(sound: :ref:`FmodSound<FmodSound>`, channel_group: FmodChannelGroup, paused: `bool`_) const
  * - FmodChannel
    - play_dsp(dsp: FmodDSP, channel_group: FmodChannelGroup, paused: `bool`_) const
  * - FmodChannel
    - get_channel(id: `int`_) const
  * - `Dictionary`_
    - get_dsp_info_by_type(type: `int`_) const
  * - FmodChannelGroup
    - get_master_channel_group() const
  * - FmodSoundGroup
    - get_master_sound_group() const

运行控制
^^^^^^^^

.. list-table::

  * - void
    - set_3d_listener_attributes(listener: `int`_, position: Vector3, velocity: Vector3, forward: vector3, up: Vector3)
  * - `Dictionary`_
    - get_3d_listener_attributes(listener: `int`_) const
  * - void
    - set_reverb_properties(instance: `int`_, decay_time: `float`_, early_delay: `float`_, late_delay: `float`_, hf_reference: `float`_, hf_decay_ratio: `float`_, diffusion: `float`_, density: `float`_, low_shelf_frequency: `float`_, low_shelf_gain: `float`_, high_cut: `float`_, early_late_mix: `float`_, wet_level: `float`_)
  * - `Dictionary`_
    - get_reverb_properties(instance: `int`_) const
  * - void
    - attach_channel_group_to_port(channel_group: FmodChannelGroup, prot_type: :ref:`FmodPortType<FmodPortType>`, port_index: `int`_ = -1, pass_thru: `bool`_ = false)
  * - void
    - detach_channel_group_from_port(channel_group: FmodChannelGroup)

录音
^^^^

.. list-table::

  * - `Dictionary`_
    - get_record_num_drivers() const
  * - `Dictionary`_
    - get_record_driver_info(id: `int`_) const
  * - `int`_
    - get_record_position(id: `int`_) const
  * - void
    - record_start(id: `int`_, sound: :ref:`FmodSound<FmodSound>`, loop: `bool`_)
  * - void
    - record_stop(id: `int`_)
  * - `bool`_
    - is_recording(id: `int`_) const

几何管理
^^^^^^^^

.. list-table::

  * - FmodGeometry
    - create_geometry(max_polygons: `int`_ = 9999, max_vertices: `int`_ = 9999) const
  * - FmodGeometry
    - load_geometry(data: PackedByteArray) const
  * - `Dictionary`_
    - get_geometry_occlusion( listener: Vector3, source: Vector3) const

其它
^^^^

.. list-table::

  * - void
    - lock_dsp()
  * - void
    - unlock_dsp()

枚举
~~~~

.. _FmodInitFlags:

FmodInitFlags
^^^^^^^^^^^^^

.. list-table::

  * - FMOD_INIT_FLAG_NORMAL
    - 0
  * - FMOD_INIT_FLAG_STREAM_FROM_UPDATE
    - 1
  * - FMOD_INIT_FLAG_MIX_FROM_UPDATE
    - 2
  * - FMOD_INIT_FLAG_3D_RIGHTHANDED
    - 4
  * - FMOD_INIT_FLAG_CLIP_OUTPUT
    - 8
  * - FMOD_INIT_FLAG_CHANNEL_LOWPASS
    - 256
  * - FMOD_INIT_FLAG_CHANNEL_DISTANCEFILTER
    - 512
  * - FMOD_INIT_FLAG_PROFILE_ENABLE
    - 65536
  * - FMOD_INIT_FLAG_VOL0_BECOMES_VIRTUAL
    - 131072
  * - FMOD_INIT_FLAG_GEOMETRY_USECLOSEST
    - 262144
  * - FMOD_INIT_FLAG_PREFER_DOLBY_DOWNMIX
    - 524288
  * - FMOD_INIT_FLAG_THREAD_UNSAFE
    - 1048576
  * - FMOD_INIT_FLAG_PROFILE_METER_ALL
    - 2097152
  * - FMOD_INIT_FLAG_MEMORY_TRACKING
    - 4194304

.. _FmodOutputType:

FmodOutputType
^^^^^^^^^^^^^^

.. list-table::

  * - FMOD_OUTPUT_TYPE_AUTODETECT
    - 0
  * - FMOD_OUTPUT_TYPE_UNKNOWN
    - 1
  * - FMOD_OUTPUT_TYPE_NOSOUND
    - 2
  * - FMOD_OUTPUT_TYPE_WAVWRITER
    - 3
  * - FMOD_OUTPUT_TYPE_NOSOUND_NRT
    - 4
  * - FMOD_OUTPUT_TYPE_WAVWRITER_NRT
    - 5
  * - FMOD_OUTPUT_TYPE_WASAPI
    - 6
  * - FMOD_OUTPUT_TYPE_ASIO
    - 7
  * - FMOD_OUTPUT_TYPE_PULSEAUDIO
    - 8
  * - FMOD_OUTPUT_TYPE_ALSA
    - 9
  * - FMOD_OUTPUT_TYPE_COREAUDIO
    - 10
  * - FMOD_OUTPUT_TYPE_AUDIOTRACK
    - 11
  * - FMOD_OUTPUT_TYPE_OPENSL
    - 12
  * - FMOD_OUTPUT_TYPE_AUDIOOUT
    - 13
  * - FMOD_OUTPUT_TYPE_AUDIO3D
    - 14
  * - FMOD_OUTPUT_TYPE_WEBAUDIO
    - 15
  * - FMOD_OUTPUT_TYPE_NNAUDIO
    - 16
  * - FMOD_OUTPUT_TYPE_WINSONIC
    - 17
  * - FMOD_OUTPUT_TYPE_AAUDIO
    - 18
  * - FMOD_OUTPUT_TYPE_AUDIOWORKLET
    - 19
  * - FMOD_OUTPUT_TYPE_PHASE
    - 20
  * - FMOD_OUTPUT_TYPE_OHAUDIO
    - 21
  * - FMOD_OUTPUT_TYPE_MAX
    - 22
  * - FMOD_OUTPUT_TYPE_FORCEINT
    - 65536

.. _FmodSpeaker:

FmodSpeaker
^^^^^^^^^^^

.. list-table::

  * - FMOD_SPEAKER_NONE
    - -1
  * - FMOD_SPEAKER_FRONT_LEFT
    - 0
  * - FMOD_SPEAKER_FRONT_RIGHT
    - 1
  * - FMOD_SPEAKER_FRONT_CENTER
    - 2
  * - FMOD_SPEAKER_LOW_FREQUENCY
    - 3
  * - FMOD_SPEAKER_SURROUND_LEFT
    - 4
  * - FMOD_SPEAKER_SURROUND_RIGHT
    - 5
  * - FMOD_SPEAKER_BACK_LEFT
    - 6
  * - FMOD_SPEAKER_BACK_RIGHT
    - 7
  * - FMOD_SPEAKER_TOP_FRONT_LEFT
    - 8
  * - FMOD_SPEAKER_TOP_FRONT_RIGHT
    - 9
  * - FMOD_SPEAKER_TOP_BACK_LEFT
    - 10
  * - FMOD_SPEAKER_TOP_BACK_RIGHT
    - 11
  * - FMOD_SPEAKER_MAX
    - 12
  * - FMOD_SPEAKER_FORCEINT
    - 65536

.. _FmodSpeakerMode:

FmodSpeakerMode
^^^^^^^^^^^^^^^

.. list-table::

  * - FMOD_SPEAKER_MODE_DEFAULT
    - 0
  * - FMOD_SPEAKER_MODE_RAW
    - 1
  * - FMOD_SPEAKER_MODE_MONO
    - 2
  * - FMOD_SPEAKER_MODE_STEREO
    - 3
  * - FMOD_SPEAKER_MODE_QUAD
    - 4
  * - FMOD_SPEAKER_MODE_SURROUND
    - 5
  * - FMOD_SPEAKER_MODE_5POINT1
    - 6
  * - FMOD_SPEAKER_MODE_7POINT1
    - 7
  * - FMOD_SPEAKER_MODE_7POINT1POINT4
    - 8
  * - FMOD_SPEAKER_MODE_MAX
    - 9
  * - FMOD_SPEAKER_FORCEINT
    - 65536

.. _FmodMode:

FmodMode
^^^^^^^^

.. list-table::

  * - FMOD_MODE_DEFAULT
    - 0
  * - FMOD_MODE_LOOP_OFF
    - 1
  * - FMOD_MODE_LOOP_NORMAL
    - 2
  * - FMOD_MODE_LOOP_BIDI
    - 4
  * - FMOD_MODE_2D
    - 8
  * - FMOD_MODE_3D
    - 16
  * - FMOD_MODE_CREATESTREAM
    - 128
  * - FMOD_MODE_CREATESAMPLE
    - 256
  * - FMOD_MODE_CREATECOMPRESSEDSAMPLE
    - 512
  * - FMOD_MODE_OPENUSER
    - 1024
  * - FMOD_MODE_OPENMEMORY
    - 2048
  * - FMOD_MODE_OPENMEMORY_POINT
    - 268435456
  * - FMOD_MODE_OPENRAW
    - 4096
  * - FMOD_MODE_OPENONLY
    - 8192
  * - FMOD_MODE_ACCURATETIME
    - 16384
  * - FMOD_MODE_MPEGSEARCH
    - 32768
  * - FMOD_MODE_NONBLOCKING
    - 65536
  * - FMOD_MODE_UNIQUE
    - 131072
  * - FMOD_MODE_3D_HEADRELATIVE
    - 262144
  * - FMOD_MODE_3D_WORLDRELATIVE
    - 524288
  * - FMOD_MODE_3D_INVERSEROLLOFF
    - 1048576
  * - FMOD_MODE_3D_LINEARROLLOFF
    - 2097152
  * - FMOD_MODE_3D_LINEARSQUAREROLLOFF
    - 4194304
  * - FMOD_MODE_3D_INVERSETAPEREDROLLOFF
    - 8388608
  * - FMOD_MODE_3D_CUSTOMROLLOFF
    - 67108864
  * - FMOD_MODE_3D_IGNOREGEOMETRY
    - 1073741824
  * - FMOD_MODE_IGNORETAGS
    - 33554432
  * - FMOD_MODE_LOWMEM
    - 134217728
  * - FMOD_MODE_VIRTUAL_PLAYFROMSTART
    - -2147483648

.. _FmodTimeUnit:

FmodTimeUnit
^^^^^^^^^^^^

.. list-table::

  * - FMOD_TIME_UNIT_MS
    - 1
  * - FMOD_TIME_UNIT_PCM
    - 2
  * - FMOD_TIME_UNIT_PCMBYTES
    - 4
  * - FMOD_TIME_UNIT_RAWBYTES
    - 8
  * - FMOD_TIME_UNIT_PCMFRACTION
    - 16
  * - FMOD_TIME_UNIT_MODORDER
    - 256
  * - FMOD_TIME_UNIT_MODROW
    - 512
  * - FMOD_TIME_UNIT_MODPATTERN
    - 1024

.. _FmodResamplerMethod:

FmodResamplerMethod
^^^^^^^^^^^^^^^^^^^

.. list-table::

  * - FMOD_RESAMPLER_DEFAULT
    - 0
  * - FMOD_RESAMPLER_NOINTERP
    - 1
  * - FMOD_RESAMPLER_LINEAR
    - 2
  * - FMOD_RESAMPLER_CUBIC
    - 3
  * - FMOD_RESAMPLER_SPLINE
    - 4

方法说明
~~~~~~~~

有效性检查
^^^^^^^^^^

.. glossary::

  `bool`_ system_is_null() const
    如果系统实例未初始化或无效，则返回 ``true``。这表示 FMOD 系统尚未准备好使用
  
  `bool`_ system_is_valid() const
    如果系统实例已成功初始化并且 FMOD 系统可用，则返回 ``true``。这表示 FMOD 系统已准备好处理音频操作

系统管理
^^^^^^^^

.. glossary::

  :ref:`FmodSystem<FmodSystem>` create_system() static
    创建并返回一个新的 FMOD System 实例。对于大多数应用程序，建议使用 **FmodServer** 的全局单例系统，而不是直接创建多个系统实例
  
  void init(max_channels: `int`_ = 32, flags: :ref:`FmodInitFlags<FmodInitFlags>` = 32)
    使用指定的最大通道数和初始化标志初始化 FMOD 系统

    max_channels 参数限制同时播放通道的总数（范围：0-4096）

    flags 参数是 **FmodInitFlags** 值的位掩码
  
  void close()
    关闭与输出设备的连接，并将系统恢复到未初始化状态，而不释放对象。可以通过再次调用 ``init()`` 来重新初始化系统
  
  void release()
    关闭系统连接并释放所有相关资源。调用此方法后，系统对象不再有效，且不应再使用
  
  void update()
    更新 FMOD 系统。这个方法应该定期调用（通常每帧一次），以处理流、3D 定位和非实时输出模式

    当使用 ``FMOD_INIT_FLAG_STREAM_FROM_UPDATE`` 或 ``FMOD_INIT_FLAG_MIX_FROM_UPDATE`` 时，这个方法更为关键，因为它驱动音频处理
  
  void mixer_suspend()
    暂停混音器线程，同时释放音频硬件的使用权，但保持内部状态。在移动平台上处理音频焦点变化时非常有用
  
  void mixer_resume()
    恢复混音器线程并重新获取对音频硬件的访问权限。在 ``mixer_suspend()`` 之后使用以恢复音频处理

设备选择
^^^^^^^^

.. glossary::

  void set_output(output_type: :ref:`FmodOutputType<FmodOutputType>`)
    设置用于运行混音器的输出接口类型。必须在 init() 之前调用。

    常用选项包括 **FMOD_OUTPUT_TYPE_AUTODETECT**、 **FMOD_OUTPUT_TYPE_WASAPI** （Windows）和 **FMOD_OUTPUT_TYPE_NOSOUND** （静音模式）
  
  :ref:`FmodOutputType<FmodOutputType>` get_output() const
    返回当前用于运行混音器的选定输出接口类型
  
  `int`_ get_num_drivers() const
    返回当前所选输出类型可用的输出驱动程序数量
  
  `Dictionary`_ get_driver_info(id: `int`_) const
    返回指定索引的声音设备的识别信息。

    返回的字典包含：

    .. list-table::

      * - name
        - 设备的名称
      * - guid
        - 设备的唯一标识符
      * - system_rate
        - 设备的默认采样率
      * - speaker_mode
        - 默认扬声器模式（FmodSpeakerMode）
      * - speaker_mode_channels
        - 默认扬声器模式下的通道数
  
  void set_driver(driver: `int`_)
    设置当前选定输出类型的输出驱动程序。使用 ``get_driver_info()`` 枚举可用的驱动程序
  
  `int`_ get_driver() const
    返回当前选定输出类型的活动输出驱动程序的索引

常规设置
^^^^^^^^

.. glossary::
  
  void set_software_format(sample_rate: `int`_, speaker_mode: FmodSpeakerMode, num_raw_speakers: `int`_)
    设置软件混音器的输出格式

    .. list-table::

      * - sample_rate
        - 输出采样率，单位为赫兹（通常为44100或48000）
      * - speaker_mode
        - 扬声器输出配置（立体声、5.1声道等）
      * - num_raw_speakers
        - 原始扬声器模式下的扬声器数量

    必须在调用 ``init()`` 之前调用
  
  `Dictionary`_ get_software_format() const
    以字典形式返回当前的软件格式设置

    .. list-table::

      * - sample_rate
        - 当前输出采样率
      * - speaker_mode
        - 当前扬声器输出配置
      * - num_raw_speakers
        - 原始扬声器模式下的扬声器数量
  
  void set_dsp_buffer_size(buffer_length: `int`_, num_buffers: `int`_)
    设置软件混音器的 DSP 缓冲区大小

    较小的缓冲区可以减少延迟，但会增加 CPU 使用率并增加音频中断的风险

    必须在 ``init()`` 之前调用
  
  `Dictionary`_ get_dsp_buffer_size() const
    返回当前 DSP 缓冲区大小设置，格式为字典，包括：

    .. list-table::
      
      * - buffer_length
        - 每个缓冲区的样本长度
      * - num_buffers
        - 环形缓冲区中的缓冲区数量
  
  void set_stream_buffer_size(file_buffer_size: `int`_ = 16384, file_buffer_size_type: :ref:`FmodTimeUnit<FmodTimeUnit>` = FMOD_TIME_UNIT_RAWBYTES)
    设置流式声音的默认缓冲区大小

    这会影响为流式音频文件预读的数据量
  
  `Dictionary`_ get_stream_buffer_size() const
    以字典的形式返回当前流缓冲区大小设置，包括：

    .. list-table::

      * - file_buffer_size
        - 流缓冲区的大小
      * - file_buffer_size_type
        - 缓冲区大小使用的时间单位
  
  void set_speaker_position(speaker: :ref:`FmodSpeaker<FmodSpeaker>`, x: `float`_, y: `float`_, active: `bool`_)
    设置扬声器在扬声器配置中的位置

    这允许为非标准扬声器设置自定义扬声器位置

    位置是相对于听者以二维坐标指定的
  
  `Dictionary`_ get_speaker_position(speaker: :ref:`FmodSpeaker<FmodSpeaker>`) const
    返回指定扬声器的位置，作为一个字典，包括：

    .. list-table::

      * - x
        - X 坐标
      * - y
        - Y 坐标
      * - active
        - 扬声器是否激活

网络配置
^^^^^^^^
.. glossary::

  void set_network_proxy(proxy: `String`_)
    为所有后续的互联网流连接设置代理服务器 URL

    传递空字符串以禁用代理

    .. note::
      以 host:port 格式指定代理，例如 ``www.fmod.com:8888`` （如果未指定端口，则默认为端口 80）

      基本身份验证支持使用 ``user:password@host:port`` 格式，例如 ``bob:sekrit123@www.fmod.com:8888``


  `String`_ get_network_proxy() const
    返回用于互联网流媒体连接的代理服务器的 URL
  
  void set_network_timeout(timeout: `int`_)
    设置网络流的超时时间（以毫秒为单位）。这会影响 FMOD 在将流视为停滞之前等待数据的时间
  
  `int`_ get_network_timeout() const
    返回网络流的超时时间（毫秒）

系统信息
^^^^^^^^
.. glossary::

  `Dictionary`_ get_version() const
    返回 FMOD 版本信息

    返回的字典包含：

    .. list-table::

      * - version
        - FMOD 版本字符串的格式为 "product.major.minor"
      * - build_number
        - FMOD 构建号字符串
  
  `int`_ get_output_handle() const
    返回输出类型特定的本地句柄。对于 Windows，这通常是 WASAPI 或 DirectSound 设备句柄

    这对于需要直接访问底层音频设备的高级用户很有用
  
  `Dictionary`_ get_channels_playing() const
    返回一个包含当前播放频道信息的字典

    返回的字典包含：

    .. list-table::

      * - channels
        - 当前正在播放的频道总数（包括虚拟声道）
      * - real_channels
        - 实际可听的声道数量（非虚拟声道）

声音与获取
^^^^^^^^^^

.. glossary::

  :ref:`FmodSound<FmodSound>` create_sound_from_file(path: `String`_, mode: `int`_) const
    从文件路径创建一个 **FmodSound**。如果路径以 ``res://`` 开头，它将内部使用 ``create_sound_from_res()``

    ``mode`` 参数使用 **FmodMode** 标志指定创建选项
  
  :ref:`FmodSound<FmodSound>` create_sound_from_memory(data: PackedByteArray, mode: `int`_) const
    从内存中加载的音频数据创建一个 **FmodSound**，它会自动添加 ``FMOD_MODE_OPENMEMORY`` 标志。音频数据数组在声音使用期间必须保持有效。这对于从加密文件或网络流加载声音非常有用

    ``mode`` 参数使用 **FmodMode** 标志指定创建选项
  
  :ref:`FmodSound<FmodSound>` create_sound_from_res(path: `String`_, mode: `int`_) const
    从 Godot 资源路径（以 ``res://`` 开头）创建一个 **FmodSound**，它会内部使用 ``create_sound_from_memory()`` 方法。文件通过 Godot 的文件系统加载进内存，然后传递给 FMOD

    ``mode`` 参数使用 **FmodMode** 标志指定创建选项
  
  :ref:`FmodSound<FmodSound>` create_stream_from_file(path: `String`_, mode: `int`_) const
    从文件创建一个流式 **FmodSound**。流式会即时解码音频数据，对于像背景音乐这样的大文件非常节省内存

    ``mode`` 参数使用 **FmodMode** 标志指定创建选项
  
  FmodDSP create_dsp(name: `String`_) const
    使用指定的名称创建自定义 DSP（数字信号处理器）效果。创建的 DSP 可以插入信号链中以实时处理音频
  
  FmodDSP create_dsp_by_type(type: `int`_) const
    创建指定内置类型的 DSP 效果。使用 ``get_dsp_info_by_type()`` 查询可用的 DSP 类型及其信息
  
  FmodChannelGroup create_channel_group(name: `String`_) const
    使用指定的名称创建一个新的 **FmodChannelGroup**。通道组允许您组织通道，以便对音量、音调和效果进行集体控制
  
  FmodSoundGroup create_sound_group(name: `String`_) const
    使用指定的名称创建一个新的 **FmodSoundGroup**

    声音组允许您将声音组织到具有共享播放限制和集体控制的类别中

    对于管理武器声音、环境声音或具有最大可听限制的对话非常有用
  
  FmodReverb3D create_reverb_3d() const
    创建一个用于空间音频混响效果的3D混响区域

    返回一个 **FmodReverb3D** 对象，该对象可以在3D空间中定位并配置混响参数

    使用此功能可以创建如洞穴、礼堂或房间等环境音效
  
  FmodChannel play_sound(sound: FmodSound, channel_group: FmodChannelGroup, paused: `bool`_) const
    在一个通道上播放声音，通过指定的通道组路由

    如果 paused 为 ``true``，通道将以暂停状态开始，直到调用 ``FmodChannel.set_paused()`` 并传入 ``false`` 才会产生声音

    返回一个 **FmodChannel** 句柄，可用于控制播放
    
  FmodChannel play_dsp(dsp: FmodDSP, channel_group: FmodChannelGroup, paused: `bool`_) const
    在通道上播放 DSP 及其输入信号，通过指定的通道组路由

    如果 paused 为 ``true``，通道将以暂停状态开始，并且在调用 ``FmodChannel.set_paused()`` 并传入 ``false`` 之前不会发出声音
  
    返回一个 **FmodChannel** 句柄，可用于控制播放
  
  FmodChannel get_channel(id: `int`_) const
    通过其 ID 检索 **FmodChannel** 句柄。通道在分配时会按顺序分配 ID
  
  `Dictionary`_ get_dsp_info_by_type(type: `int`_) const
    检索有关内置 DSP 类型的信息

    返回的字典包含：

    .. list-table::

       * - name
         - DSP 的名称
       * - version
         - 插件版本号
       * - plugin_sdk_version
         - FMOD 插件 SDK 版本
       * - num_input_buffers
         - 输入缓冲区数量
       * - num_output_buffers
         - 输出缓冲区数量
       * - has_create
         - DSP 是否有创建回调
       * - has_release
         - DSP 是否有释放回调
       * - has_reset
         - DSP 是否有重置回调
  
  FmodChannelGroup get_master_channel_group() const
    返回所有声音最终路由到的主通道组。使用它来控制全局音量、添加主效果或监控整体输出
  
  FmodSoundGroup get_master_sound_group() const
    返回所有声音默认所属的主声音组

    主声音组可用于设置全局播放限制并控制所有声音的整体行为

运行控制
^^^^^^^^

.. glossary::

  void set_3d_listener_attributes(listener: `int`_, position: Vector3, velocity: Vector3, forward: vector3, up: Vector3)
    设置3D监听器的位置、速度和方向

    监听器索引指定要配置的监听器（用于多监听器设置）

    .. list-table::
      * - position
        - 听者的世界位置
      * - velocity
        - 听者的速度，用于多普勒计算
      * - forward
        - 听者的前向量
      * - up
        - 听者的上向量

  `Dictionary`_ get_3d_listener_attributes(listener: `int`_) const
    以字典形式返回指定监听器的 3D 属性：

    .. list-table::

      * - position
        - 听者的世界位置
      * - velocity
        - 听者的速度，用于多普勒计算
      * - forward
        - 听者的前向量
      * - up
        - 听者的上向量
  
  void set_reverb_properties(instance: `int`_, decay_time: `float`_, early_delay: `float`_, late_delay: `float`_, hf_reference: `float`_, hf_decay_ratio: `float`_, diffusion: `float`_, density: `float`_, low_shelf_frequency: `float`_, low_shelf_gain: `float`_, high_cut: `float`_, early_late_mix: `float`_, wet_level: `float`_)
    设置指定混响实例的混响属性

    混响实例 ID 是通过 ``create_reverb_3d()`` 创建的 **FmodReverb3D** 对象的 ID

    .. list-table::

      * - decay_time
        - 混响衰减时间，单位为秒
      * - early_delay
        - 早期反射的延迟时间，单位为毫秒
      * - late_delay
        - 后期反射的延迟时间，单位为毫秒
      * - hf_reference
        - 高频衰减参考频率，单位为赫兹
      * - hf_decay_ratio
        - 高频衰减时间与整体衰减时间的比率
      * - diffusion
        - 混响扩散程度（0-100%）
      * - density
        - 混响密度（0-100%）
      * - low_shelf_frequency
        - 低架滤波器频率，单位为赫兹
      * - low_shelf_gain
        - 低架滤波器增益，单位为分贝
      * - high_cut
        - 混响高频截止频率，单位为赫兹
      * - early_late_mix
        - 早期反射与后期反射的混合比例（0-100%）
      * - wet_level
        - 湿信号（混响）级别，单位为分贝
  
  `Dictionary`_ get_reverb_properties(instance: `int`_) const
    以字典形式返回指定全局混响实例的混响属性，包括所有参数：

    .. list-table::

      * - decay_time
        - 混响衰减时间，单位为秒
      * - early_delay
        - 早期反射的延迟时间，单位为毫秒
      * - late_delay
        - 后期反射的延迟时间，单位为毫秒
      * - hf_reference
        - 高频衰减参考频率，单位为赫兹
      * - hf_decay_ratio
        - 高频衰减时间与整体衰减时间的比率
      * - diffusion
        - 混响扩散程度（0-100%）
      * - density
        - 混响密度（0-100%）
      * - low_shelf_frequency
        - 低架滤波器频率，单位为赫兹
      * - low_shelf_gain
        - 低架滤波器增益，单位为分贝
      * - high_cut
        - 混响高频截止频率，单位为赫兹
      * - early_late_mix
        - 早期反射与后期反射的混合比例（0-100%）
      * - wet_level
        - 湿信号（混响）级别，单位为分贝

  void attach_channel_group_to_port(channel_group: FmodChannelGroup, prot_type: :ref:`FmodPortType<FmodPortType>`, port_index: `int`_ = -1, pass_thru: `bool`_ = false)
    将通道组的输出附加到输出驱动器上的音频端口

    这允许将音频路由到特定的输出目标，例如控制器扬声器或辅助输出

    请参阅 **FmodPortType** 了解可用的端口类型
  
  void detach_channel_group_from_port(channel_group: FmodChannelGroup)
    将通道组从其分配的音频端口中分离

    通道组将恢复到主输出的正常路由

录音
^^^^

.. glossary::

  `Dictionary`_ get_record_num_drivers() const
    返回有关可用录音设备的信息

    返回的字典包含：

    .. list-table::

       * - num_drivers
         - 可用录音设备的总数
       * - num_connected
         - 当前连接的录音设备数量
  
  `Dictionary`_ get_record_driver_info(id: `int`_) const
    返回由其索引指定的录音设备的识别信息

    返回的字典包含：

    .. list-table::

      * - name
        - 录音设备的名称
      * - guid
        - 设备的唯一标识符
      * - system_rate
        - 设备的默认采样率
      * - speaker_mode
        - 扬声器模式（FmodSpeakerMode）
      * - speaker_mode_channels
        - 通道数量
      * - state
        - 驱动状态标志
  
  `int`_ get_record_position(id: `int`_) const
    返回指定录音设备的当前 PCM 采样录音位置
  
  void record_start(id: `int`_, sound: FmodSound, loop: `bool`_)
    从指定设备开始录音到提供的音频对象中

    如果 loop 为 ``true``，当录音达到缓冲区末尾时，会从音频缓冲区的开头重新开始录音
  
  void record_stop(id: `int`_)
    停止从指定设备录制
  
  `bool`_ is_recording(id: `int`_) const
    如果指定的录音设备当前正在录音，则返回 ``true``

几何管理
^^^^^^^^

.. glossary::

  FmodGeometry create_geometry(max_polygons: `int`_ = 9999, max_vertices: `int`_ = 9999) const
    为 3D 遮挡计算创建一个几何体对象，用于模拟场景中物理物体对声音的遮挡

    ``max_polygons`` 参数指定几何体中允许的最大多边形数量

    ``max_vertices`` 参数指定几何体中允许的最大顶点数量
  
  FmodGeometry load_geometry(data: PackedByteArray) const
    从提供的字节数组加载几何数据并创建一个 **FmodGeometry** 对象，对于从磁盘加载复杂几何形状非常有用

    .. warning:: 数据格式必须符合 FMOD 的几何数据规范，通常包含顶点和多边形信息
  
  `Dictionary`_ get_geometry_occlusion(listener: Vector3, source: Vector3) const
    计算听者与声源位置之间的遮挡情况

    返回的字典包含：

    .. list-table::

      * - direct
        - 直接声音的遮挡值（0.0-1.0）
      * - reverb
        - 混响声音的遮挡值（0.0-1.0）
    
    .. note:: 如果已经创建了单面多边形，重要的是要正确获取源和监听器的位置，因为从点A到点B的遮挡可能与从点B到点A的遮挡不同

其它
^^^^

.. glossary::

  void lock_dsp()
    锁住 DSP 引擎互斥锁

    在需要原子操作的多次DSP调用时使用，这对于确保在执行这些调用时 DSP 处理不会被中断非常有用

    始终与 ``unlock_dsp()`` 配对使用
  
  void unlock_dsp()
    解锁 DSP 引擎互斥锁

    必须在 ``lock_dsp()`` 之后调用