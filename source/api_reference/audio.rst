音频资源 API
============

.. _FmodAudioStream:

FmodAudioStream
---------------

继承自： `Resource`_

**表示用于 FMOD 播放的音频流的资源**

描述
~~~~

FmodAudioStream 是一个资源，用于通过 FMOD 音频引擎播放音频数据。它支持从文件（包括 ``res://`` 路径）加载音频，并提供可配置的创建模式以进行流式或基于样本的播放

可以使用 :ref:`FmodAudioStreamPlayer<FmodAudioStreamPlayer>` 播放该流，也可以直接使用 FMOD 的通道系统。底层的 :ref:`FmodSound<FmodSound>` 对象会在首次通过 :ref:`get_sound()<FmodAudioStream-get_sound>` 请求时惰性创建

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `PackedByteArray`_
    - audio_data
    - PackedByteArray()
    - 从文件加载的原始音频数据。通常由音频导入器或通过 :ref:`load_from_file()<FmodAudioStream-load_from_file>` 设置。数据存储在内存中，并在调用 :ref:`get_sound()<FmodAudioStream-get_sound>` 时用于创建 FMOD 声音对象
  * - `int`_
    - mode_flags
    - 1
    - 创建模式标志，用于确定音频的加载和播放方式。这是 :ref:`CreateMode<FmodAudioStream-CreateMode>` 值的位掩码。当这些标志被更改时，内部的 :ref:`FmodSound<FmodSound>` 会被释放，并将在下一次调用 :ref:`get_sound()<FmodAudioStream-get_sound>` 时使用新的标志重新创建

方法
~~~~

.. _FmodAudioStream-set_audio_data:

void set_audio_data(data: `PackedByteArray`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置音频原始数据。数据通常来自导入器、文件读取或运行时加载；设置后会更新数据加载状态。

.. _FmodAudioStream-get_audio_data:

`PackedByteArray`_ get_audio_data() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前保存的音频原始数据。

.. _FmodAudioStream-set_mode_flags:

void set_mode_flags(flags: `int`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置创建 :ref:`FmodSound<FmodSound>` 时使用的模式标志。修改后会使已缓存的声音失效，下次 :ref:`get_sound()<FmodAudioStream-get_sound>` 会使用新标志重新创建。

.. _FmodAudioStream-get_mode_flags:

`int`_ get_mode_flags() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前创建模式标志。

.. _FmodAudioStream-get_sound:

:ref:`FmodSound<FmodSound>` get_sound()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回此流的 **FmodSound** 对象，如有必要则创建它（懒创建）。声音会使用当前 ``mode_flags`` 创建。如果未加载音频数据或 FMOD 系统不可用，则返回空引用。

.. _FmodAudioStream-preload:

`bool`_ preload()
^^^^^^^^^^^^^^^^^

立即创建并缓存内部 :ref:`FmodSound<FmodSound>`，用于减少首次播放时的延迟。创建成功返回 ``true``。

.. _FmodAudioStream-is_preloaded:

`bool`_ is_preloaded() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果内部 :ref:`FmodSound<FmodSound>` 已经创建并缓存，则返回 ``true``。

.. _FmodAudioStream-get_length:

`float`_ get_length() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回音频的长度（以秒为单位）。如果声音未创建或未加载任何数据，则返回 ``0.0``。

.. _FmodAudioStream-is_data_loaded:

`bool`_ is_data_loaded() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果音频数据已加载到此流中，则返回 ``true``，否则返回 ``false``。

.. _FmodAudioStream-load_from_file:

:ref:`FmodAudioStream<FmodAudioStream>` load_from_file(path: `String`_, flags: `int`_ = 1) static
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从文件路径加载音频流。路径可以是 Godot 资源路径（例如 ``"res://audio/music.mp3"``）或绝对文件路径。

``flags`` 参数指定创建模式标志（ :ref:`CreateMode<FmodAudioStream-CreateMode>` 的位掩码）。默认为 ``MODE_STREAM``。

如果文件无法打开或读取，则返回一个空引用。

.. _FmodAudioStream-clear:

void clear()
^^^^^^^^^^^^

清除音频数据并释放内部 :ref:`FmodSound<FmodSound>` 资源。这将释放内存并将流重置为空状态。

枚举
~~~~

.. _FmodAudioStream-CreateMode:

CreateMode
^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - MODE_DEFAULT
    - 0
    - 默认创建模式。没有设置特殊标志
  * - MODE_STREAM
    - 1
    - 从内存中流式传输音频。音频数据是逐步读取的，而不是一次性完全解码。这可以减少大文件的内存使用，但在播放时可能会增加 CPU 开销
  * - MODE_SAMPLE
    - 2
    - 将整个音频文件作为样本加载到内存中。这可以实现更快的播放和更低的 CPU 使用率，但会消耗更多内存。最适合短音效使用
  * - MODE_LOOP
    - 4
    - 启用正常循环播放。当音频播放到末尾时，它会回到开头重新播放
  * - MODE_LOOP_BIDI
    - 8
    - 启用双向（乒乓）循环播放。当音频播放到末尾时，它会向后播放到开始位置，然后再次向前播放，创建一个无缝的来回循环

示例
~~~~

从文件加载
^^^^^^^^^^

.. code-block:: gdscript

    var stream: FmodAudioStream = FmodAudioStream.load_from_file("res://music/background.ogg", FmodAudioStream.MODE_STREAM)
    
    var player: FmodAudioStreamPlayer = $FmodAudioStreamPlayer
    player.stream = stream
    player.play()

从文件加载
^^^^^^^^^^

.. code-block:: gdscript

    var sfx: FmodAudioStream = FmodAudioStream.load_from_file("res://sfx/explosion.wav", FmodAudioStream.MODE_SAMPLE)
    
    var player: FmodAudioStreamPlayer = $FmodAudioStreamPlayer
    player.stream = sfx
    player.play()

从内存加载
^^^^^^^^^^

.. code-block:: gdscript

    var stream: FmodAudioStream = FmodAudioStream.new()
    stream.audio_data = loaded_bytes
    stream.mode_flags = FmodAudioStream.MODE_SAMPLE

.. _FmodSound:

FmodSound
---------

继承自： `RefCounted`_

**FMOD::Sound 的引用计数包装器，表示已加载的音频资源**

描述
~~~~

**FmodSound** 是 `FMOD::Sound <https://www.fmod.com/docs/2.02/api/core-api-sound.html>`_ 的一个 `RefCounted`_ 包装器，表示已加载的音频资源。它提供对音频元数据、格式信息、原始音频数据、追踪器格式（MOD/S3M/XM/IT/MIDI）的音乐专用控制以及元数据标签的访问

使用 :ref:`load_from_file()<FmodSound-load_from_file>` 从磁盘加载音频，或通过 :ref:`FmodSystem<FmodSystem>` 方法创建音频。加载后，你可以查询音频信息、读取原始音频数据，或将其与 :ref:`FmodChannel<FmodChannel>` 一起用于播放

方法
~~~~

有效性检查
^^^^^^^^^^

.. _FmodSound-sound_is_null:

`bool`_ sound_is_null() const
*****************************

如果声音实例未初始化或无效，则返回 ``true``。这表示声音尚未准备好使用

.. _FmodSound-sound_is_valid:

`bool`_ sound_is_valid() const
******************************

如果声音实例已成功初始化并且音效可用，则返回 ``true``。这表示声音已准备好处理音频操作

格式信息
^^^^^^^^

.. _FmodSound-get_format:

`Dictionary`_ get_format() const
********************************

返回一个包含声音格式信息的字典，包含以下键：

.. list-table::
  :header-rows: 1
  
  * - 键名
    - 类型
    - 说明
  * - type
    - :ref:`FmodSoundType<FmodSoundType>`
    - 音频格式类型
  * - format
    - :ref:`FmodSoundFormat<FmodSoundFormat>`
    - 采样格式
  * - channels
    - `int`_
    - 声道数量
  * - bits
    - `int`_
    - 每个采样的位数

.. _FmodSound-get_name:

`String`_ get_name() const
**************************

返回声音的名称。这通常是文件名或嵌入在音频文件中的名称

.. _FmodSound-get_length:

`float`_ get_length(time_unit: :ref:`FmodSystem.FmodTimeUnit<FmodTimeUnit>` = 1) const
**************************************************************************************

返回指定时间单位的声音长度。当使用毫秒（ **FMOD_TIME_UNIT_MS** ）时，结果以秒为单位返回。对于其他单位如字节或 PCM 样本，则返回原始值

.. seealso:: :ref:`FmodSystem.FmodTimeUnit<FmodTimeUnit>` 获取可用的时间单位选项

.. _FmodSound-get_num_tags:

`Dictionary`_ get_num_tags() const
**********************************

返回一个包含元数据标签计数的字典：

.. list-table::
  :header-rows: 1
  
  * - 键名
    - 类型
    - 说明
  * - num_tags
    - `int`_
    - 声音中的总标签数量
  * - num_tags_updated
    - `int`_
    - 已更新的标签数量（针对流媒体来源）

.. seealso:: 使用 :ref:`get_tag()<FmodSound-get_tag>` 来获取单个标签信息

.. _FmodSound-get_tag:

`Dictionary`_ get_tag(index: `int`_, name: `String`_ = "") const
****************************************************************

从声音中检索元数据标签。可以通过索引或名称检索标签。如果名称非空，它将搜索具有该名称的标签；否则，它将检索指定索引处的标签

返回一个字典，包括：

.. list-table::
  :header-rows: 1
  
  * - 键名
    - 类型
    - 说明
  * - type
    - :ref:`FmodTagType<FmodTagType>`
    - 标签类型
  * - datatype
    - :ref:`FmodTagDataType<FmodTagDataType>`
    - 标签值的数据类型
  * - name
    - `String`_
    - 标签名称
  * - data
    - `Variant`_
    - 标签值（类型根据 ``datatype`` 而异）
  * - data_len
    - `int`_
    - 数据的字节长度
  * - updated
    - `bool`_
    - 如果标签已更新（用于流式来源），则为 ``true``

数据读取
^^^^^^^^

.. _FmodSound-get_open_state:

`Dictionary`_ get_open_state() const
************************************

返回声音的当前打开状态。这对于使用非阻塞标志打开的声音或监控流缓冲区状态非常有用。返回一个字典，包括：

.. list-table::
  :header-rows: 1
  
  * - 键名
    - 类型
    - 说明
  * - open_state:
    - :ref:`FmodOpenState<FmodOpenState>`
    - 当前打开状态
  * - percent_buffered
    - `int`_
    - 流式声音缓冲区填充的百分比
  * - starving
    - `bool`_
    - 如果流正在因数据不足而饥饿（缓冲区下溢），则为 ``true``
  * - disk_busy
    - `bool`_
    - 如果磁盘当前正在读取，则为 ``true``

.. _FmodSound-read_data:

`PackedByteArray`_ read_data(length: `int`_) const
**************************************************

使用 FMOD 的内部编解码器将声音中的原始音频数据读取到 **PackedByteArray** 中。这对于提取解码后的 PCM 数据或进行自定义处理非常有用

.. note:: 在读取之前使用 ``seek_data()`` 定位读取光标。
  
.. _FmodSound-seek_data:

void seek_data(pcm: `int`_)
***************************

在声音中定位到特定的 PCM 位置以进行数据读取操作。该位置以 PCM 采样为单位指定

.. note:: 这会影响 ``read_data()`` 使用的位置，而不会影响播放位置

.. _FmodSound-lock:

:ref:`FmodSoundLock<FmodSoundLock>` lock(offset: `int`_, length: `int`_) const
******************************************************************************

锁定声音的样本数据区域以进行直接访问。这允许读取或修改原始 PCM 数据。返回一个 **FmodSoundLock** 对象，该对象提供对锁定内存区域的访问

.. note:: 始终确保 FmodSoundLock 被释放（超出作用域）以解锁数据
    
.. code-block:: gdscript

  var lock = sound.lock(0, sound.get_length(FmodSystem.FMOD_TIME_UNIT_PCM))
  # Access data through lock object
  
音乐
^^^^

.. _FmodSound-get_music_num_channels:

`int`_ get_music_num_channels() const
*************************************

返回 MOD/S3M/XM/IT/MIDI 文件中的通道数量。每个通道对应模块文件中的一个轨道/乐器

.. note:: 这仅适用于模块音乐格式（跟踪器格式）

.. _FmodSound-set_music_channel_volume:

void set_music_channel_volume(channel: `int`_, volume_db: `float`_) const
*************************************************************************

设置 MOD/S3M/XM/IT/MIDI 文件中某个特定通道的音量，以分贝为单位。这允许对模块音乐中的每个音轨/乐器进行单独控制

.. note:: 这仅适用于模块音乐格式。有效的通道索引范围为 0 到 ``get_music_num_channels()`` - 1

.. _FmodSound-get_music_channel_volume:

`float`_ get_music_channel_volume(channel: `int`_) const
********************************************************

返回 MOD/S3M/XM/IT/MIDI 文件中某个特定通道的音量，单位为分贝

.. note:: 这仅适用于模块音乐格式。使用 ``get_music_num_channels()`` 来获取可用通道的数量

.. _FmodSound-set_music_speed:

void set_music_speed(speed: `float`_)
*************************************

设置 MOD/S3M/XM/IT/MIDI 音乐的相对播放速度。数值 1.0 为正常速度，0.5 为半速，2.0 为双倍速度，依此类推

.. note:: 这仅适用于模块音乐格式（跟踪器格式）

.. _FmodSound-get_music_speed:

`float`_ get_music_speed() const
********************************

返回 MOD/S3M/XM/IT/MIDI 音乐的相对播放速度。数值 1.0 表示正常速度，小于 1.0 的数值表示较慢，大于 1.0 的数值表示较快

.. note:: 这仅适用于模块音乐格式

同步/标记
^^^^^^^^^

.. _FmodSound-get_sync_point:

`int`_ get_sync_point(index: `int`_) const
******************************************

返回指定索引处的同步点句柄。同步点是音频文件中的嵌入标记（例如，WAV 文件中的循环点或提示点）

.. note:: 使用 ``get_sync_point_info()`` 获取返回的同步点句柄的信息

.. _FmodSound-get_sync_point_info:

`Dictionary`_ get_sync_point_info(point: `int`_, time_unit: :ref:`FmodSystem.FmodTimeUnit<FmodTimeUnit>` = 1) const
*******************************************************************************************************************

返回有关同步点的信息。point 参数应为从 ``get_sync_point()`` 获取的句柄。返回一个字典，其中包含：

.. list-table::
  :header-rows: 1
  
  * - 键名
    - 类型
    - 说明
  * - name
    - `String`_
    - 同步点的名称
  * - offset
    - `int`_
    - 同步点在指定时间单位中的位置
  * - time_unit
    - :ref:`FmodSystem.FmodTimeUnit<FmodTimeUnit>`
    - 用于偏移的时间单位
  * - pointer
    - `int`_
    - 同步点句柄

.. _FmodSound-get_num_sub_sounds:

`int`_ get_num_sub_sounds() const
*********************************

返回多声音文件中的子声音数量。这对于像 FSB（FMOD 声音库）或 DLS（可下载声音）之类包含多个音频样本的格式非常有用

.. note:: 像 MP3 或 WAV 这样的常规音频文件通常返回该值为 0

回调
^^^^

.. _FmodSound-set_pcmread_callback:

void set_pcmread_callback(callback: `Callable`_)
************************************************

设置 PCM 读取回调函数。当 FMOD 需要更多音频数据进行解码和播放时，会调用此回调

回调函数签名： ``func callback(data: PackedByteArray, data_len: int) -> int``

- ``data`` —— FMOD 提供的用于填充音频数据的缓冲区
- ``data_len`` —— 需要填充的数据长度（字节）
- 返回值应为 ``0`` 表示成功，或其他错误码

这允许你提供自定义音频数据源，例如程序化生成音频或从网络流接收数据

.. important:: 回调在音频线程中执行，必须快速返回以避免音频中断。不要在回调中执行阻塞操作

.. _FmodSound-get_pcmread_callback:

`Callable`_ get_pcmread_callback() const
****************************************

返回当前设置的 PCM 读取回调函数。如果未设置回调，则返回空的 ``Callable``

.. _FmodSound-set_pcmsetpos_callback:

void set_pcmsetpos_callback(callback: `Callable`_)
**************************************************

设置 PCM 定位回调函数。当 FMOD 需要改变声音的内部读取位置时（例如循环或跳转），会调用此回调

回调函数签名： ``func callback(position: int, time_unit: int) -> int``

- ``position`` —— 请求的新位置
- ``time_unit`` —— 位置的时间单位（参见 ``FmodSystem.FmodTimeUnit`` ）
- 返回值应为 ``0`` 表示成功，或其他错误码

这对于自定义数据源需要知道何时发生位置跳转的情况非常有用

.. _FmodSound-get_pcmsetpos_callback:

`Callable`_ get_pcmsetpos_callback() const
******************************************

返回当前设置的 PCM 定位回调函数。如果未设置回调，则返回空的 ``Callable``

.. _FmodSound-set_nonblock_callback:

void set_nonblock_callback(callback: `Callable`_)
*************************************************

设置非阻塞加载完成回调函数。当使用非阻塞标志（ ``FMOD_NONBLOCKING`` ）打开声音且加载完成时，会调用此回调

回调函数签名： ``func callback(sound: FmodSound, result: int) -> int``

- ``sound`` —— 加载完成的声音对象
- ``result`` —— 加载结果， ``0`` 表示成功，或其他错误码
- 返回值应为 ``0``

这允许你在声音异步加载完成后立即收到通知，无需轮询 ``get_open_state()``

.. code-block:: gdscript

    sound.set_nonblock_callback(func(s: FmodSound, result: int) -> void:
        if result == 0:
            print("Sound loading complete!")
            channel = system.play_sound(s, master_group, false)
    )

.. seealso:: :ref:`get_open_state()<FmodSound>` 用于手动轮询加载状态

.. _FmodSound-get_nonblock_callback:

`Callable`_ get_nonblock_callback() const
*****************************************

返回当前设置的非阻塞加载完成回调函数。如果未设置回调，则返回空的 ``Callable``

其它
^^^^

.. _FmodSound-load_from_file:

:ref:`FmodSound<FmodSound>` load_from_file(path: `String`_) static
******************************************************************

用于从文件路径加载声音的静态方法。该路径应是有效的文件系统路径或 Godot 资源路径（ ``res://`` ）

.. code-block:: gdscript

  var sound = FmodSound.load_from_file("res://music.mp3")

枚举
~~~~

.. _FmodSoundType:

FmodSoundType
^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_SOUND_TYPE_UNKNOWN
    - 0
    - 未知或不支持的音频格式
  * - FMOD_SOUND_TYPE_AIFF
    - 1
    - 音频交换文件格式（.aif，.aiff）。仅限无压缩整数格式
  * - FMOD_SOUND_TYPE_ASF
    - 2
    - Microsoft 高级系统格式（.asf、.wma、.wmv）。平台提供解码器，仅在 Windows 上可用
  * - FMOD_SOUND_TYPE_DLS
    - 3
    - 可下载音频（.dls）。MIDI（.mid）使用的多声音库格式
  * - FMOD_SOUND_TYPE_FLAC
    - 4
    - 无损音频编解码器（.flac）
  * - FMOD_SOUND_TYPE_FSB
    - 5
    - FMOD 采样库（.fsb）。专有多声音库格式。支持编码：PCM16、FADPCM、Vorbis、AT9、XMA、Opus
  * - FMOD_SOUND_TYPE_IT
    - 6
    - Impulse Tracker 模块格式
  * - FMOD_SOUND_TYPE_MIDI
    - 7
    - 乐器数字接口
  * - FMOD_SOUND_TYPE_MOD
    - 8
    - Protracker / Fasttracker 模块文件
  * - FMOD_SOUND_TYPE_MPEG
    - 9
    - 动态影像专家组（.mp2，.mp3）。还支持.wav（RIFF）容器格式
  * - FMOD_SOUND_TYPE_OGGVORBIS
    - 10
    - Ogg Vorbis（.ogg）
  * - FMOD_SOUND_TYPE_PLAYLIST
    - 11
    - 播放列表信息容器（.asx、.pls、.m3u、.wax）。无音频，仅有标签
  * - FMOD_SOUND_TYPE_RAW
    - 12
    - 原始未压缩PCM数据（.raw）
  * - FMOD_SOUND_TYPE_S3M
    - 13
    - ScreamTracker 3 模块（.s3m）
  * - FMOD_SOUND_TYPE_USER
    - 14
    - 用户自制的声音
  * - FMOD_SOUND_TYPE_WAV
    - 15
    - Microsoft 波形音频文件格式（.wav）。支持的编码：无压缩PCM，IMA ADPCM。平台提供仅在Windows上可用的ACM解码扩展
  * - FMOD_SOUND_TYPE_XM
    - 16
    - FastTracker 2 扩展模块（.xm）
  * - FMOD_SOUND_TYPE_XMA
    - 17
    - Microsoft XMA 位流支持，支持FSB（.fsb）容器格式。平台提供解码器，仅在Xbox上可用
  * - FMOD_SOUND_TYPE_AUDIOQUEUE
    - 18
    - Apple 音频队列解码器（.mp4、.m4a、.mp3）。支持的编码：AAC、ALAC、MP3。平台提供解码器，仅在 iOS/tvOS 设备上使用
  * - FMOD_SOUND_TYPE_AT9
    - 19
    - 索尼ATRAC9位流支持FSB（.fsb）容器格式。平台提供解码器，仅在PlayStation上可用
  * - FMOD_SOUND_TYPE_VORBIS
    - 20
    - Vorbis 比特流支持 FSB（.fsb）容器格式
  * - FMOD_SOUND_TYPE_MEDIA_FOUNDATION
    - 21
    - Microsoft Media Foundation 解码器（.asf、.wma、.wmv、.mp4、.m4a）。平台提供的解码器，仅在 UWP 上可用
  * - FMOD_SOUND_TYPE_MEDIACODEC
    - 22
    - Google Media 编解码器（.m4a，.mp4）。平台提供的解码器，仅在安卓上提供
  * - FMOD_SOUND_TYPE_FADPCM
    - 23
    - FMOD 自适应差分脉冲码调制比特流，支持FSB（.fsb）容器格式
  * - FMOD_SOUND_TYPE_OPUS
    - 24
    - Opus 比特流支持，支持 FSB（.fsb）容器格式。平台提供解码器，仅支持 Xbox Series X|S、PS5 和 Switch
  * - FMOD_SOUND_TYPE_MAX
    - 25
    - 支持的最大声音类型

.. _FmodSoundFormat:

FmodSoundFormat
^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_SOUND_FORMAT_NONE
    - 0
    - 未知
  * - FMOD_SOUND_FORMAT_PCM8
    - 1
    - 8位整数PCM数据
  * - FMOD_SOUND_FORMAT_PCM16
    - 2
    - 16位整数PCM数据
  * - FMOD_SOUND_FORMAT_PCM24
    - 3
    - 24位整数PCM数据
  * - FMOD_SOUND_FORMAT_PCM32
    - 4
    - 32位整数PCM数据
  * - FMOD_SOUND_FORMAT_PCMFLOAT
    - 5
    - 32位浮点PCM数据
  * - FMOD_SOUND_FORMAT_BITSTREAM
    - 6
    - 声音数据为其原生压缩格式
  * - FMOD_SOUND_FORMAT_MAX
    - 7
    - 支持的最大声音格式

.. _FmodTagType:

FmodTagType
^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_TAG_TYPE_UNKNOWN
    - 0
    - FMOD不识别的标签类型
  * - FMOD_TAG_TYPE_ID3V1
    - 1
    - MP3 ID3 标签 1.0。通常 1 个标签存储在 MP3 文件末尾 128 字节处
  * - FMOD_TAG_TYPE_ID3V2
    - 2
    - MP3 ID3标签2.0。可变长度标签，可能超过1个
  * - FMOD_TAG_TYPE_VORBISCOMMENT
    - 3
    - 元数据容器，适用于 Vorbis、FLAC、Theora、Speex 和 Opus 文件格式
  * - FMOD_TAG_TYPE_SHOUTCAST
    - 4
    - SHOUTcast 互联网流元数据
  * - FMOD_TAG_TYPE_ICECAST
    - 5
    - 可在播放过程中发布的Icecast互联网流元数据
  * - FMOD_TAG_TYPE_ASF
    - 6
    - 高级系统格式元数据通常与Windows Media格式（如WMA）相关
  * - FMOD_TAG_TYPE_MIDI
    - 7
    - 存储在MIDI文件中的元数据
  * - FMOD_TAG_TYPE_PLAYLIST
    - 8
    - 播放列表文件如PLS、M3U、ASX和WAX会通过该标签类型填充播放列表信息
  * - FMOD_TAG_TYPE_FMOD
    - 9
    - FMOD 的 MIDI、MOD、S3M、XM、IT 格式支持以及网络流用于通知互联网流事件（如采样率变化）的标签类型
  * - FMOD_TAG_TYPE_USER
    - 10
    - 对于编解码器开发者来说，这种标签类型可以配合 `FMOD_CODEC_METADATA_FUNC <https://www.fmod.com/docs/2.02/api/plugin-api-codec.html#fmod_codec_metadata_func>`_ 生成自定义元数据
  * - FMOD_TAG_TYPE_MAX
    - 11
    - 支持的最大标签类型数量

.. _FmodTagDataType:

FmodTagDataType
^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_TAG_DATA_TYPE_BINARY
    - 0
    - 原始二进制数据
  * - FMOD_TAG_DATA_TYPE_INT
    - 1
    - 整数
  * - FMOD_TAG_DATA_TYPE_FLOAT
    - 2
    - 浮点数
  * - FMOD_TAG_DATA_TYPE_STRING
    - 3
    - 8位ASCII字元字符串
  * - FMOD_TAG_DATA_TYPE_STRING_UTF16
    - 4
    - 16位UTF字符串
  * - FMOD_TAG_DATA_TYPE_STRING_UTF16BE
    - 5
    - 16位UTF字符串大端序字节序
  * - FMOD_TAG_DATA_TYPE_STRING_UTF8
    - 6
    - 8位UTF字符串
  * - FMOD_TAG_DATA_TYPE_MAX
    - 7
    - 支持的最大标签数据类型数量

.. _FmodOpenState:

FmodOpenState
^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - FMOD_OPEN_STATE_READY
    - 0
    - 准备就绪
  * - FMOD_OPEN_STATE_LOADING
    - 1
    - 正在加载中
  * - FMOD_OPEN_STATE_ERROR
    - 2
    - 无法打开，通常是找不到文件、内存不足等
  * - FMOD_OPEN_STATE_CONNECTING
    - 3
    - 连接到远程主机（仅在互联网播放声音时）
  * - FMOD_OPEN_STATE_BUFFERING
    - 4
    - 缓冲数据
  * - FMOD_OPEN_STATE_SEEKING
    - 5
    - 正在定位子声道并强制刷新流缓冲区
  * - FMOD_OPEN_STATE_PLAYING
    - 6
    - 已经准备好并可以播放，但目前无法释放，否则主线会停滞
  * - FMOD_OPEN_STATE_SETPOSITION
    - 7
    - 在流中寻找不同的位置
  * - FMOD_OPEN_STATE_MAX
    - 8
    - 开放状态类型的最大数量

.. _FmodSoundLock:

FmodSoundLock
-------------

继承自： `RefCounted`_

**提供对声音样本数据的直接访问，以进行读取或修改**

描述
~~~~

FmodSoundLock 用于锁定声音数据的区域以进行直接访问。这允许读取或修改声音的原始采样数据

当声音被锁定时，FMOD 会提供一个或两个指向数据的指针（如果锁定的区域绕过了声音缓冲区的末尾，则使用两个指针）

.. important:: 在完成数据访问后，务必调用 ``unlock()``，或者使用 RAII 模式（让对象超出作用域）自动解锁

.. note:: 锁定声音可能代价较大，因为它会阻塞混音线程。请尽量少用且仅用于短时间

方法
~~~~

.. _FmodSoundLock-get_data1:

`PackedByteArray`_ get_data1() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

以 ``PackedByteArray`` 的形式返回锁定数据的前一部分，在大多数情况下，这包含锁定区域的大部分内容

.. _FmodSoundLock-get_data2:

`PackedByteArray`_ get_data2() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回锁定数据的第二部分作为 ``PackedByteArray``，只有当锁定区域绕过声音缓冲区的末端时，这部分才非空

.. _FmodSoundLock-is_locked:

`bool`_ is_locked() const
^^^^^^^^^^^^^^^^^^^^^^^^^

如果声音数据当前被锁定并且可访问，则返回 ``true``

.. _FmodSoundLock-unlock:

void unlock()
^^^^^^^^^^^^^

解锁声音数据，允许 FMOD 恢复正常处理，在访问数据完成后应立即调用此函数

.. note:: 如果数据仍然被锁定，析构函数会自动调用此函数
