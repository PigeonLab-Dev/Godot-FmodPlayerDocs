节点 API
========

.. _FmodAudioStreamPlayer:

FmodAudioStreamPlayer
---------------------

继承自： `Node`_

**用于播放 2D 非空间化音频流的节点**

描述
~~~~

**FmodAudioStreamPlayer** 用于播放 :ref:`FmodAudioStream<FmodAudioStream>` 资源，适合背景音乐、UI 音效和不需要空间定位的音频

播放时节点会从 :ref:`FmodServer<FmodServer>` 获取指定总线对应的 :ref:`FmodChannelGroup<FmodChannelGroup>`。如果找不到指定总线，则回退到 Master 总线

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - :ref:`FmodAudioStream<FmodAudioStream>`
    - stream
    - null
    - 要播放的音频流资源
  * - `bool`_
    - playing
    - false
    - 设置为 ``true`` 开始播放，设置为 ``false`` 停止播放
  * - `bool`_
    - stream_paused
    - false
    - 是否暂停当前播放流
  * - `float`_
    - volume_db
    - 0.0
    - 播放音量，单位为分贝
  * - `float`_
    - pitch_scale
    - 1.0
    - 播放速度和音高缩放
  * - `bool`_
    - auto_play
    - false
    - 进入场景树后自动播放
  * - `StringName`_
    - bus
    - "Master"
    - 输出到的音频总线名称

信号
~~~~

.. list-table::
  :header-rows: 1

  * - 信号
    - 说明
  * - finished()
    - 播放自然结束时发出

方法
~~~~

.. _FmodAudioStreamPlayer-set_stream:

void set_stream(stream: :ref:`FmodAudioStream<FmodAudioStream>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置要播放的音频流

如果当前正在播放，会先停止当前通道并清除播放状态

.. _FmodAudioStreamPlayer-get_stream:

:ref:`FmodAudioStream<FmodAudioStream>` get_stream() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前设置的音频流

.. _FmodAudioStreamPlayer-play:

void play(from_position: `float`_ = 0.0)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从指定位置开始播放，单位为秒

如果内部通道仍然有效，会复用该通道并跳转到指定位置；否则会从当前 ``stream`` 创建新的 FMOD 通道

.. _FmodAudioStreamPlayer-seek:

void seek(to_position: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

跳转到指定播放位置，单位为秒

.. _FmodAudioStreamPlayer-stop:

void stop()
^^^^^^^^^^^

停止播放并清除暂停状态

.. _FmodAudioStreamPlayer-set_playing:

void set_playing(playing: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置播放状态

传入 ``true`` 等同于调用 :ref:`play()<FmodAudioStreamPlayer-play>`，传入 ``false`` 等同于调用 :ref:`stop()<FmodAudioStreamPlayer-stop>`

.. _FmodAudioStreamPlayer-is_playing:

`bool`_ is_playing() const
^^^^^^^^^^^^^^^^^^^^^^^^^^

如果内部通道有效且正在播放，则返回 ``true``

.. _FmodAudioStreamPlayer-set_stream_paused:

void set_stream_paused(paused: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

暂停或恢复当前播放流

.. _FmodAudioStreamPlayer-get_stream_paused:

`bool`_ get_stream_paused() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前播放流的暂停状态

.. _FmodAudioStreamPlayer-get_playback_position:

`float`_ get_playback_position() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前播放位置，单位为秒

如果内部通道无效，则返回 ``0.0``

.. _FmodAudioStreamPlayer-set_volume_db:

void set_volume_db(volume_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置音量，单位为分贝

如果正在播放，会立即同步到底层通道

.. _FmodAudioStreamPlayer-get_volume_db:

`float`_ get_volume_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前音量，单位为分贝

.. _FmodAudioStreamPlayer-set_pitch_scale:

void set_pitch_scale(pitch_scale: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置播放速度和音高缩放

``1.0`` 表示原始速度，``2.0`` 表示两倍速度，``0.5`` 表示半速

.. _FmodAudioStreamPlayer-get_pitch_scale:

`float`_ get_pitch_scale() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前播放速度和音高缩放

.. _FmodAudioStreamPlayer-set_auto_play:

void set_auto_play(enable: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置是否在进入场景树后自动播放

编辑器预览状态下不会自动播放

.. _FmodAudioStreamPlayer-is_autoplay_enabled:

`bool`_ is_autoplay_enabled() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果启用了自动播放，则返回 ``true``

.. _FmodAudioStreamPlayer-set_bus:

void set_bus(bus: `StringName`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置输出总线名称

.. _FmodAudioStreamPlayer-get_bus:

`StringName`_ get_bus() const_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前输出总线名称

如果设置的总线不存在，则返回 ``"Master"``

示例
~~~~

.. code-block:: gdscript

    @onready var music: FmodAudioStreamPlayer = $FmodAudioStreamPlayer

    func _ready() -> void:
        music.stream = FmodAudioStream.load_from_file("res://music/bgm.ogg", FmodAudioStream.MODE_STREAM)
        music.bus = "Music"
        music.volume_db = -6.0
        music.play()

    func fade_out() -> void:
        var tween = create_tween()
        tween.tween_property(music, "volume_db", -40.0, 1.5)
        tween.tween_callback(music.stop)

.. _FmodAudioStreamPlayer2D:

FmodAudioStreamPlayer2D
-----------------------

继承自： ``Node2D``

**用于在 2D 场景中播放带距离衰减和声像的音频流**

描述
~~~~

**FmodAudioStreamPlayer2D** 基于节点在 2D 世界中的位置计算音量衰减和左右声像。它会将音频流强制为 2D 模式，距离衰减由节点逻辑手动控制

监听位置优先使用 :ref:`FmodServer<FmodServer>` 中记录的 2D 摄像机信息；如果没有记录，则尝试使用当前视口的 `Camera2D`_

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - :ref:`FmodAudioStream<FmodAudioStream>`
    - stream
    - null
    - 要播放的音频流资源
  * - `bool`_
    - playing
    - false
    - 设置为 ``true`` 开始播放，设置为 ``false`` 停止播放
  * - `bool`_
    - stream_paused
    - false
    - 是否暂停当前播放流
  * - `float`_
    - volume_db
    - 0.0
    - 基础音量，单位为分贝
  * - `float`_
    - pitch_scale
    - 1.0
    - 播放速度和音高缩放
  * - `bool`_
    - autoplay
    - false
    - 进入场景树后自动播放
  * - `float`_
    - max_distance
    - 2000.0
    - 超过该像素距离后静音
  * - `float`_
    - attenuation
    - 1.0
    - 距离衰减曲线强度
  * - `float`_
    - panning_strength
    - 1.0
    - 左右声像强度
  * - `StringName`_
    - bus
    - "Master"
    - 输出到的音频总线名称
  * - `int`_
    - area_mask
    - 1
    - 2D 物理区域遮罩
  * - `int`_
    - max_polyphony
    - 1
    - 最大复音数量

信号
~~~~

.. list-table::
  :header-rows: 1

  * - 信号
    - 说明
  * - finished()
    - 播放自然结束时发出

方法
~~~~

.. _FmodAudioStreamPlayer2D-set_stream:

void set_stream(stream: :ref:`FmodAudioStream<FmodAudioStream>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置要播放的音频流

如果当前正在播放，会先停止当前通道并清除播放状态

.. _FmodAudioStreamPlayer2D-get_stream:

:ref:`FmodAudioStream<FmodAudioStream>` get_stream() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前设置的音频流

.. _FmodAudioStreamPlayer2D-play:

void play(from_position: `float`_ = 0.0)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从指定位置开始播放，单位为秒

播放前会为音频流添加 :ref:`FmodMode<FmodMode>` 里的 ``FMOD_MODE_2D`` 标志并重新创建缓存声音

.. _FmodAudioStreamPlayer2D-seek:

void seek(to_position: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

跳转到指定播放位置，单位为秒

.. _FmodAudioStreamPlayer2D-stop:

void stop()
^^^^^^^^^^^

停止播放并清除暂停状态

.. _FmodAudioStreamPlayer2D-set_playing:

void set_playing(playing: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置播放状态

.. _FmodAudioStreamPlayer2D-is_playing:

`bool`_ is_playing() const
^^^^^^^^^^^^^^^^^^^^^^^^^^

如果内部通道有效且正在播放，则返回 ``true``

.. _FmodAudioStreamPlayer2D-set_stream_paused:

void set_stream_paused(paused: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

暂停或恢复当前播放流

.. _FmodAudioStreamPlayer2D-get_stream_paused:

`bool`_ get_stream_paused() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前播放流的暂停状态

.. _FmodAudioStreamPlayer2D-get_playback_position:

`float`_ get_playback_position() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前播放位置，单位为秒

.. _FmodAudioStreamPlayer2D-set_volume_db:

void set_volume_db(volume_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置基础音量，单位为分贝

实际播放音量还会受到距离衰减影响

.. _FmodAudioStreamPlayer2D-get_volume_db:

`float`_ get_volume_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回基础音量，单位为分贝

.. _FmodAudioStreamPlayer2D-set_volume_linear:

void set_volume_linear(volume_linear: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用线性音量设置基础音量

.. _FmodAudioStreamPlayer2D-get_volume_linear:

`float`_ get_volume_linear() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

以线性音量返回基础音量

.. _FmodAudioStreamPlayer2D-set_pitch_scale:

void set_pitch_scale(pitch_scale: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置播放速度和音高缩放

.. _FmodAudioStreamPlayer2D-get_pitch_scale:

`float`_ get_pitch_scale() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前播放速度和音高缩放

.. _FmodAudioStreamPlayer2D-set_autoplay:

void set_autoplay(enable: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置是否在进入场景树后自动播放

.. _FmodAudioStreamPlayer2D-is_autoplay_enabled:

`bool`_ is_autoplay_enabled() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果启用了自动播放，则返回 ``true``

.. _FmodAudioStreamPlayer2D-set_max_distance:

void set_max_distance(pixels: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置最大可听距离，单位为像素

小于等于 ``0.0`` 的值会被限制为 ``1.0``

.. _FmodAudioStreamPlayer2D-get_max_distance:

`float`_ get_max_distance() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回最大可听距离，单位为像素

.. _FmodAudioStreamPlayer2D-set_attenuation:

void set_attenuation(curve: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置距离衰减曲线强度

数值越大，随距离衰减越快

.. _FmodAudioStreamPlayer2D-get_attenuation:

`float`_ get_attenuation() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回距离衰减曲线强度

.. _FmodAudioStreamPlayer2D-set_panning_strength:

void set_panning_strength(panning_strength: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置左右声像强度

小于 ``0.0`` 的值会被限制为 ``0.0``

.. _FmodAudioStreamPlayer2D-get_panning_strength:

`float`_ get_panning_strength() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回左右声像强度

.. _FmodAudioStreamPlayer2D-set_bus:

void set_bus(bus: `StringName`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置输出总线名称

.. _FmodAudioStreamPlayer2D-get_bus:

`StringName`_ get_bus() const_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前输出总线名称

如果没有设置，则返回 ``"Master"``

.. _FmodAudioStreamPlayer2D-set_area_mask:

void set_area_mask(mask: `int`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置 2D 物理区域遮罩

.. _FmodAudioStreamPlayer2D-get_area_mask:

`int`_ get_area_mask() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回 2D 物理区域遮罩

.. _FmodAudioStreamPlayer2D-set_max_polyphony:

void set_max_polyphony(max_polyphony: `int`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置最大复音数量

小于 ``1`` 的值会被限制为 ``1``

.. _FmodAudioStreamPlayer2D-get_max_polyphony:

`int`_ get_max_polyphony() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回最大复音数量

.. _FmodAudioStreamPlayer2D-has_stream_playback:

`bool`_ has_stream_playback() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果内部通道对象有效，则返回 ``true``

.. _FmodAudioStreamPlayer2D-get_stream_playback:

:ref:`FmodChannel<FmodChannel>` get_stream_playback() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回内部播放通道，可用于高级控制

示例
~~~~

.. code-block:: gdscript

    @onready var ambience: FmodAudioStreamPlayer2D = $FmodAudioStreamPlayer2D

    func _ready() -> void:
        ambience.stream = FmodAudioStream.load_from_file("res://audio/river.ogg", FmodAudioStream.MODE_STREAM)
        ambience.bus = "Ambience"
        ambience.max_distance = 1200.0
        ambience.attenuation = 1.5
        ambience.panning_strength = 1.0
        ambience.play()

.. _FmodAudioStreamPlayer3D:

FmodAudioStreamPlayer3D
-----------------------

继承自： `Node3D`_

**用于在 3D 空间中播放音频流的节点**

描述
~~~~

**FmodAudioStreamPlayer3D** 会将声音作为 FMOD 3D 通道播放，并持续同步节点的全局位置、速度、距离衰减、距离滤波器和发射角度设置

它适合环境声源、角色语音、机器声、移动物体声源等需要空间定位的音频

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - :ref:`FmodAudioStream<FmodAudioStream>`
    - stream
    - null
    - 要播放的音频流资源
  * - `int`_
    - attenuation_model
    - 2
    - 3D 距离衰减模型
  * - `float`_
    - volume_db
    - 0.0
    - 基础音量，单位为分贝
  * - `float`_
    - unit_size
    - 1.0
    - FMOD 最小衰减距离
  * - `float`_
    - pitch_scale
    - 1.0
    - 播放速度和音高缩放
  * - `bool`_
    - playing
    - false
    - 设置为 ``true`` 开始播放，设置为 ``false`` 停止播放
  * - `bool`_
    - auto_play
    - false
    - 进入场景树后自动播放
  * - `bool`_
    - stream_paused
    - false
    - 是否暂停当前播放流
  * - `float`_
    - max_distance
    - 10.0
    - 最大衰减距离倍数，实际最大距离为 ``max_distance * unit_size``
  * - `StringName`_
    - bus
    - "Master"
    - 输出到的音频总线名称
  * - `int`_
    - area_mask
    - 1
    - 物理区域遮罩
  * - `bool`_
    - emission_angle_enabled
    - false
    - 是否启用方向性发射锥
  * - `float`_
    - emission_angle
    - 45.0
    - 发射内锥角，单位为度
  * - `float`_
    - emission_angle_filter_attenuation_db
    - -12.0
    - 发射锥外的音量衰减，单位为分贝
  * - `float`_
    - attenuation_filter_cutoff_hz
    - 5000.0
    - 距离滤波器截止频率，单位为 Hz
  * - `float`_
    - attenuation_filter_db
    - 0.0
    - 距离滤波器衰减，单位为分贝
  * - `int`_
    - doppler_tracking
    - 0
    - 多普勒速度追踪模式

信号
~~~~

.. list-table::
  :header-rows: 1

  * - 信号
    - 说明
  * - finished()
    - 播放自然结束时发出

方法
~~~~

.. _FmodAudioStreamPlayer3D-set_stream:

void set_stream(stream: :ref:`FmodAudioStream<FmodAudioStream>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置要播放的音频流

如果当前正在播放，会先停止当前通道并清除播放状态

.. _FmodAudioStreamPlayer3D-get_stream:

:ref:`FmodAudioStream<FmodAudioStream>` get_stream() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前设置的音频流

.. _FmodAudioStreamPlayer3D-play:

void play(from_position: `float`_ = 0.0)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从指定位置开始播放，单位为秒

播放时会创建 FMOD 3D 通道，并应用当前 3D 衰减、滤波、发射角度和多普勒设置

.. _FmodAudioStreamPlayer3D-seek:

void seek(to_position: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

跳转到指定播放位置，单位为秒

.. _FmodAudioStreamPlayer3D-stop:

void stop()
^^^^^^^^^^^

停止播放并清除暂停状态

.. _FmodAudioStreamPlayer3D-set_playing:

void set_playing(playing: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置播放状态

.. _FmodAudioStreamPlayer3D-is_playing:

`bool`_ is_playing() const
^^^^^^^^^^^^^^^^^^^^^^^^^^

如果内部通道有效且正在播放，则返回 ``true``

.. _FmodAudioStreamPlayer3D-set_stream_paused:

void set_stream_paused(paused: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

暂停或恢复当前播放流

.. _FmodAudioStreamPlayer3D-get_stream_paused:

`bool`_ get_stream_paused() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前播放流的暂停状态

.. _FmodAudioStreamPlayer3D-get_playback_position:

`float`_ get_playback_position() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前播放位置，单位为秒

.. _FmodAudioStreamPlayer3D-set_volume_db:

void set_volume_db(volume_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置基础音量，单位为分贝

.. _FmodAudioStreamPlayer3D-get_volume_db:

`float`_ get_volume_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回基础音量，单位为分贝

.. _FmodAudioStreamPlayer3D-set_pitch_scale:

void set_pitch_scale(pitch_scale: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置播放速度和音高缩放

.. _FmodAudioStreamPlayer3D-get_pitch_scale:

`float`_ get_pitch_scale() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前播放速度和音高缩放

.. _FmodAudioStreamPlayer3D-set_auto_play:

void set_auto_play(enable: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置是否在进入场景树后自动播放

.. _FmodAudioStreamPlayer3D-is_autoplay_enabled:

`bool`_ is_autoplay_enabled() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果启用了自动播放，则返回 ``true``

.. _FmodAudioStreamPlayer3D-set_bus:

void set_bus(bus: `StringName`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置输出总线名称

.. _FmodAudioStreamPlayer3D-get_bus:

`StringName`_ get_bus() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前输出总线名称

如果没有设置，则返回 ``"Master"``

.. _FmodAudioStreamPlayer3D-set_max_distance:

void set_max_distance(distance: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置最大衰减距离倍数

实际 FMOD 最大距离为 ``max_distance * unit_size``，小于 ``0.01`` 的值会被限制为 ``0.01``

.. _FmodAudioStreamPlayer3D-get_max_distance:

`float`_ get_max_distance() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回最大衰减距离倍数

.. _FmodAudioStreamPlayer3D-set_unit_size:

void set_unit_size(size: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置 FMOD 最小衰减距离

小于 ``0.001`` 的值会被限制为 ``0.001``

.. _FmodAudioStreamPlayer3D-get_unit_size:

`float`_ get_unit_size() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回 FMOD 最小衰减距离

.. _FmodAudioStreamPlayer3D-set_attenuation_model:

void set_attenuation_model(model: :ref:`AttenuationModel<FmodAudioStreamPlayer3D-AttenuationModel>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置距离衰减模型

如果当前通道有效，会立即重新应用 3D 衰减设置

.. _FmodAudioStreamPlayer3D-get_attenuation_model:

:ref:`AttenuationModel<FmodAudioStreamPlayer3D-AttenuationModel>` get_attenuation_model() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前距离衰减模型

.. _FmodAudioStreamPlayer3D-set_emission_angle_enabled:

void set_emission_angle_enabled(enabled: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

启用或禁用方向性发射锥

.. _FmodAudioStreamPlayer3D-is_emission_angle_enabled:

`bool`_ is_emission_angle_enabled() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果启用了方向性发射锥，则返回 ``true``

.. _FmodAudioStreamPlayer3D-set_emission_angle:

void set_emission_angle(angle: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置发射内锥角，单位为度

值会被限制在 ``0.0`` 到 ``90.0`` 之间

.. _FmodAudioStreamPlayer3D-get_emission_angle:

`float`_ get_emission_angle() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回发射内锥角，单位为度

.. _FmodAudioStreamPlayer3D-set_emission_angle_filter_attenuation_db:

void set_emission_angle_filter_attenuation_db(db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置发射锥外的音量衰减，单位为分贝

值会被限制在 ``-80.0`` 到 ``0.0`` 之间

.. _FmodAudioStreamPlayer3D-get_emission_angle_filter_attenuation_db:

`float`_ get_emission_angle_filter_attenuation_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回发射锥外的音量衰减，单位为分贝

.. _FmodAudioStreamPlayer3D-set_attenuation_filter_cutoff_hz:

void set_attenuation_filter_cutoff_hz(freq: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置距离滤波器截止频率，单位为 Hz

值会被限制在 ``10.0`` 到 ``22050.0`` 之间

.. _FmodAudioStreamPlayer3D-get_attenuation_filter_cutoff_hz:

`float`_ get_attenuation_filter_cutoff_hz() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回距离滤波器截止频率，单位为 Hz

.. _FmodAudioStreamPlayer3D-set_attenuation_filter_db:

void set_attenuation_filter_db(db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置距离滤波器衰减，单位为分贝

值会被限制在 ``-80.0`` 到 ``0.0`` 之间

.. _FmodAudioStreamPlayer3D-get_attenuation_filter_db:

`float`_ get_attenuation_filter_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回距离滤波器衰减，单位为分贝

.. _FmodAudioStreamPlayer3D-set_doppler_tracking:

void set_doppler_tracking(tracking: :ref:`DopplerTracking<FmodAudioStreamPlayer3D-DopplerTracking>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置多普勒速度追踪模式

禁用时底层通道的多普勒级别为 ``0.0``；启用时根据节点位移计算速度

.. _FmodAudioStreamPlayer3D-get_doppler_tracking:

:ref:`DopplerTracking<FmodAudioStreamPlayer3D-DopplerTracking>` get_doppler_tracking() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回当前多普勒速度追踪模式

.. _FmodAudioStreamPlayer3D-set_area_mask:

void set_area_mask(mask: `int`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置物理区域遮罩

.. _FmodAudioStreamPlayer3D-get_area_mask:

`int`_ get_area_mask() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回物理区域遮罩

枚举
~~~~

.. _FmodAudioStreamPlayer3D-AttenuationModel:

AttenuationModel
^^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - ATTENUATION_INVERSE_DISTANCE
    - 0
    - 反距离衰减
  * - ATTENUATION_INVERSE_SQUARE_DISTANCE
    - 1
    - 平方反距离衰减
  * - ATTENUATION_LOGARITHMIC
    - 2
    - 线性滚降，最大距离处静音
  * - ATTENUATION_DISABLED
    - 3
    - 禁用距离衰减

.. _FmodAudioStreamPlayer3D-DopplerTracking:

DopplerTracking
^^^^^^^^^^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - DOPPLER_TRACKING_DISABLED
    - 0
    - 禁用多普勒追踪
  * - DOPPLER_TRACKING_IDLE_STEP
    - 1
    - 在普通处理帧中计算速度
  * - DOPPLER_TRACKING_PHYSICS_STEP
    - 2
    - 在物理处理帧中计算速度

示例
~~~~

.. code-block:: gdscript

    @onready var engine_sound: FmodAudioStreamPlayer3D = $FmodAudioStreamPlayer3D

    func _ready() -> void:
        engine_sound.stream = FmodAudioStream.load_from_file("res://audio/engine.ogg", FmodAudioStream.MODE_STREAM)
        engine_sound.bus = "SFX"
        engine_sound.max_distance = 40.0
        engine_sound.unit_size = 1.5
        engine_sound.attenuation_model = FmodAudioStreamPlayer3D.ATTENUATION_INVERSE_SQUARE_DISTANCE
        engine_sound.doppler_tracking = FmodAudioStreamPlayer3D.DOPPLER_TRACKING_PHYSICS_STEP
        engine_sound.play()

.. code-block:: gdscript

    @onready var speaker: FmodAudioStreamPlayer3D = $Speaker

    func _ready() -> void:
        speaker.emission_angle_enabled = true
        speaker.emission_angle = 30.0
        speaker.emission_angle_filter_attenuation_db = -18.0

.. _FmodGeometryInstance3D:

FmodGeometryInstance3D
----------------------

继承自： `Node3D`_

**从 3D 网格生成 FMOD 遮挡几何体的节点**

描述
~~~~

**FmodGeometryInstance3D** 用于将场景中的几何体注册到 FMOD Geometry 系统，让 3D 声音可以根据场景遮挡产生直达声和混响遮挡

此节点应作为 `MeshInstance3D`_ 或 `CollisionShape3D`_ 的子节点使用。当前源码已完整支持从 `MeshInstance3D`_ 构建三角形几何体；从 `CollisionShape3D`_ 构建仍未完整实现

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `float`_
    - direct_occlusion
    - 0.5
    - 直达声遮挡强度
  * - `float`_
    - reverb_occlusion
    - 0.5
    - 混响声遮挡强度
  * - `bool`_
    - double_sided
    - true
    - 多边形是否双面遮挡
  * - `bool`_
    - active
    - true
    - 几何体是否参与遮挡计算
  * - `bool`_
    - auto_rebuild
    - true
    - 进入场景或属性变化时自动重建几何体
  * - `bool`_
    - show_debug_gizmo
    - true
    - 是否显示编辑器调试 Gizmo

信号
~~~~

.. list-table::
  :header-rows: 1

  * - 信号
    - 说明
  * - geometry_created()
    - 几何体创建成功后发出
  * - geometry_cleared()
    - 几何体被清空后发出
  * - geometry_rebuilt()
    - 几何体重建成功后发出

方法
~~~~

.. _FmodGeometryInstance3D-set_direct_occlusion:

void set_direct_occlusion(value: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置直达声遮挡强度

值会被限制在 ``0.0`` 到 ``1.0`` 之间。启用 ``auto_rebuild`` 且几何体有效时会重建几何体

.. _FmodGeometryInstance3D-get_direct_occlusion:

`float`_ get_direct_occlusion() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回直达声遮挡强度

.. _FmodGeometryInstance3D-set_reverb_occlusion:

void set_reverb_occlusion(value: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置混响声遮挡强度

值会被限制在 ``0.0`` 到 ``1.0`` 之间。启用 ``auto_rebuild`` 且几何体有效时会重建几何体

.. _FmodGeometryInstance3D-get_reverb_occlusion:

`float`_ get_reverb_occlusion() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回混响声遮挡强度

.. _FmodGeometryInstance3D-set_double_sided:

void set_double_sided(value: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置多边形是否双面遮挡

.. _FmodGeometryInstance3D-get_double_sided:

`bool`_ get_double_sided() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果多边形为双面遮挡，则返回 ``true``

.. _FmodGeometryInstance3D-set_active:

void set_active(value: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置几何体是否参与遮挡计算

如果几何体已创建，会立即同步到底层 :ref:`FmodGeometry<FmodGeometry>`

.. _FmodGeometryInstance3D-get_active:

`bool`_ get_active() const
^^^^^^^^^^^^^^^^^^^^^^^^^^

如果几何体处于激活状态，则返回 ``true``

.. _FmodGeometryInstance3D-set_auto_rebuild:

void set_auto_rebuild(value: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置是否自动重建几何体

启用后节点会开启处理，用于编辑器中的网格变化检测

.. _FmodGeometryInstance3D-get_auto_rebuild:

`bool`_ get_auto_rebuild() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果启用了自动重建，则返回 ``true``

.. _FmodGeometryInstance3D-set_show_debug_gizmo:

void set_show_debug_gizmo(value: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置是否显示编辑器调试 Gizmo

.. _FmodGeometryInstance3D-get_show_debug_gizmo:

`bool`_ get_show_debug_gizmo() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果启用了调试 Gizmo，则返回 ``true``

.. _FmodGeometryInstance3D-rebuild_geometry:

void rebuild_geometry()
^^^^^^^^^^^^^^^^^^^^^^^

重新检测源节点并重建 FMOD 几何体

成功后会发出 ``geometry_rebuilt`` 和 ``geometry_created`` 信号

.. _FmodGeometryInstance3D-clear_geometry:

void clear_geometry()
^^^^^^^^^^^^^^^^^^^^^

释放当前 FMOD 几何体并清空引用

成功清空时会发出 ``geometry_cleared`` 信号

.. _FmodGeometryInstance3D-has_valid_geometry:

`bool`_ has_valid_geometry() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果内部几何体存在且有效，则返回 ``true``

.. _FmodGeometryInstance3D-get_geometry:

:ref:`FmodGeometry<FmodGeometry>` get_geometry() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回内部 :ref:`FmodGeometry<FmodGeometry>` 对象

示例
~~~~

.. code-block:: gdscript

    # 节点结构：
    # WallMesh (MeshInstance3D)
    #   FmodGeometryInstance3D

    @onready var occluder: FmodGeometryInstance3D = $WallMesh/FmodGeometryInstance3D

    func _ready() -> void:
        occluder.direct_occlusion = 0.8
        occluder.reverb_occlusion = 0.4
        occluder.double_sided = true
        occluder.rebuild_geometry()

节点对比
--------

.. list-table::
  :header-rows: 1

  * - 特性
    - FmodAudioStreamPlayer
    - FmodAudioStreamPlayer2D
    - FmodAudioStreamPlayer3D
    - FmodGeometryInstance3D
  * - 继承自
    - Node
    - Node2D
    - Node3D
    - Node3D
  * - 主要用途
    - 非空间化播放
    - 2D 空间播放
    - 3D 空间播放
    - 3D 遮挡几何体
  * - 播放音频
    - 是
    - 是
    - 是
    - 否
  * - 距离衰减
    - 否
    - 是
    - 是
    - 不适用
  * - 声像/空间定位
    - 否
    - 2D 声像
    - 3D 定位
    - 不适用
  * - 多普勒
    - 否
    - 否
    - 是
    - 不适用
  * - 适合场景
    - 背景音乐、UI 音效
    - 2D 环境声、地图音源
    - 3D 声源、角色语音
    - 墙体、障碍物、遮挡体
