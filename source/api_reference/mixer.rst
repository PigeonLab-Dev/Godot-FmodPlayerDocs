混合器 API
==========

.. _FmodAudioBus:

FmodAudioBus
------------

继承自： `RefCounted`_

**表示一个用于混音的音频总线，支持效果处理**

描述
~~~~

**FmodAudioBus** 表示 FMOD 音频系统中的音频混音总线。每个总线都有自己的 :ref:`FmodChannelGroup<FmodChannelGroup>` 用于音频路由，并且可以应用多个 :ref:`FmodAudioEffect<FmodAudioEffect>`

总线由 :ref:`FmodAudioBusLayout<FmodAudioBusLayout>` 管理的层级结构组织。主总线是该层级的根，所有其他总线最终通过它进行路由

使用总线可以：

- 将音频组织成逻辑分类（音乐、音效、对话等）
- 对一组声音应用效果
- 控制整个音频类别的音量和路由
- 实现混音的独奏/静音功能

属性
~~~~

.. list-table::
  :header-rows: 1

  * - 类型
    - 名称
    - 初始值
    - 说明
  * - `bool`_
    - bypass
    - false
    - 是否绕过总线上的效果链
  * - `bool`_
    - mute
    - false
    - 用户设置的静音状态
  * - `bool`_
    - solo
    - false
    - 是否启用独奏状态
  * - `float`_
    - volume
    - 0.0
    - 总线音量，单位为分贝

方法
~~~~

.. _FmodAudioBus-init_bus:

void init_bus(name: `String`_, parent: :ref:`FmodChannelGroup<FmodChannelGroup>` = null)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用指定名称和可选父通道组初始化总线

如果名称为 ``"Master"``，会直接使用 FMOD 主通道组作为总线；否则会创建新的 :ref:`FmodChannelGroup<FmodChannelGroup>` 并连接到父通道组

.. _FmodAudioBus-set_parent:

void set_parent(parent: :ref:`FmodChannelGroup<FmodChannelGroup>`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置此总线输出到的父通道组

如果未提供父通道组，则连接到 FMOD 主通道组

.. _FmodAudioBus-get_bus:

:ref:`FmodChannelGroup<FmodChannelGroup>` get_bus() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回此总线用于音频路由的 :ref:`FmodChannelGroup<FmodChannelGroup>`

如果总线尚未初始化，则返回 ``null``

.. _FmodAudioBus-get_parent:

:ref:`FmodChannelGroup<FmodChannelGroup>` get_parent() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回此总线输出到的父 :ref:`FmodChannelGroup<FmodChannelGroup>`

对于主总线返回 ``null``

.. _FmodAudioBus-get_bus_name:

`String`_ get_bus_name() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回此音频总线的名称

.. _FmodAudioBus-add_effect:

void add_effect(effect: :ref:`FmodAudioEffect<FmodAudioEffect>`, index: `int`_ = 0)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

向此总线添加一个音频效果，并将效果应用到内部通道组

当前实现会将效果追加到效果列表中；如果总线已启用 ``bypass``，添加后会立即同步旁路状态

.. _FmodAudioBus-remove_effect:

void remove_effect(index: `int`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从此总线中移除指定索引处的音频效果

移除时会先将效果从内部通道组上解除

.. _FmodAudioBus-get_effect:

:ref:`FmodAudioEffect<FmodAudioEffect>` get_effect(index: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回效果链中指定索引处的 :ref:`FmodAudioEffect<FmodAudioEffect>`

如果索引超出范围，则返回 ``null``

.. _FmodAudioBus-set_volume_db:

void set_volume_db(volume_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置总线音量，单位为分贝

.. _FmodAudioBus-get_volume_db:

`float`_ get_volume_db() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回总线音量，单位为分贝

如果总线尚未初始化，则返回 ``0.0``

.. _FmodAudioBus-set_solo:

void set_solo(solo: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置总线的独奏状态

独奏状态需要由 :ref:`FmodAudioBusLayout<FmodAudioBusLayout>` 统一计算并应用到各总线的静音状态

.. _FmodAudioBus-is_solo:

`bool`_ is_solo() const
^^^^^^^^^^^^^^^^^^^^^^^

如果此总线处于独奏状态，则返回 ``true``

.. _FmodAudioBus-set_mute:

void set_mute(mute: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置用户静音状态

此方法只记录用户设置，实际 FMOD 静音状态由 :ref:`apply_mute()<FmodAudioBus-apply_mute>` 应用

.. _FmodAudioBus-is_mute:

`bool`_ is_mute() const
^^^^^^^^^^^^^^^^^^^^^^^

如果此总线被用户设置为静音，则返回 ``true``

.. _FmodAudioBus-apply_mute:

void apply_mute(mute: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

根据用户静音状态和布局中的独奏状态，将最终静音状态应用到内部通道组

当任意总线处于独奏状态时，未独奏的总线会被静音

.. _FmodAudioBus-set_bypass:

void set_bypass(bypass: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置总线的效果旁路状态

此方法只记录旁路状态，调用 :ref:`sync_bypass()<FmodAudioBus-sync_bypass>` 后才会同步到现有效果

.. _FmodAudioBus-is_bypass:

`bool`_ is_bypass() const
^^^^^^^^^^^^^^^^^^^^^^^^^

如果此总线启用了效果旁路，则返回 ``true``

.. _FmodAudioBus-sync_bypass:

void sync_bypass()
^^^^^^^^^^^^^^^^^^

将此总线的旁路状态同步到内部通道组上的所有 DSP

这用于在更改 ``bypass`` 或新增效果后确保效果链状态一致

.. _FmodAudioBusLayout:

FmodAudioBusLayout
------------------

继承自： `Resource`_

**管理音频总线的布局和层级**

描述
~~~~

**FmodAudioBusLayout** 管理 FMOD 音频系统中音频总线的完整层级结构。它维护了 :ref:`FmodAudioBus<FmodAudioBus>` 实例及其相互关系的集合

该布局会自动与 Godot 的 `AudioServer`_ 总线布局同步，实现与 Godot 内置音频系统的集成

主要特性：

- 总线层级管理（主总线及子总线）
- 每个总线的音量、独奏、静音和旁路状态控制
- 每个总线的效果链管理
- 与 Godot `AudioServer`_ 的同步

方法
~~~~

.. _FmodAudioBusLayout-create_audio_bus:

void create_audio_bus(name: `String`_, parent: :ref:`FmodAudioBus<FmodAudioBus>` = null)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用指定名称和可选父级创建新的音频总线

总线名称必须唯一。 ``Master`` 总线由布局自动确保存在，不应手动移除

.. _FmodAudioBusLayout-get_audio_bus:

:ref:`FmodAudioBus<FmodAudioBus>` get_audio_bus(name: `String`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回具有指定名称的 :ref:`FmodAudioBus<FmodAudioBus>`

如果不存在具有该名称的总线，则返回 ``null``

.. _FmodAudioBusLayout-has_audio_bus:

`bool`_ has_audio_bus(name: `String`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果布局中存在具有指定名称的总线，则返回 ``true``

.. _FmodAudioBusLayout-remove_audio_bus:

void remove_audio_bus(name: `String`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从布局中移除指定名称的音频总线

.. warning:: ``Master`` 总线无法被移除

.. _FmodAudioBusLayout-set_bus_volume:

void set_bus_volume(name: `String`_, volume_db: `float`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定总线的音量，单位为分贝

.. _FmodAudioBusLayout-get_bus_volume:

`float`_ get_bus_volume(name: `String`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定总线的音量，单位为分贝

如果总线不存在或无效，则返回 ``0.0``

.. _FmodAudioBusLayout-set_bus_solo:

void set_bus_solo(name: `String`_, solo: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定总线的独奏状态，并更新所有总线的最终静音状态

.. _FmodAudioBusLayout-bus_is_solo:

`bool`_ bus_is_solo(name: `String`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果指定总线处于独奏状态，则返回 ``true``

.. _FmodAudioBusLayout-set_bus_mute:

void set_bus_mute(name: `String`_, mute: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定总线的用户静音状态，并更新所有总线的最终静音状态

.. _FmodAudioBusLayout-bus_is_mute:

`bool`_ bus_is_mute(name: `String`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果指定总线被用户设置为静音，则返回 ``true``

.. _FmodAudioBusLayout-set_bus_bypass:

void set_bus_bypass(name: `String`_, bypass: `bool`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置指定总线的效果旁路状态，并立即同步到总线上的 DSP

.. _FmodAudioBusLayout-bus_is_bypass:

`bool`_ bus_is_bypass(name: `String`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果指定总线启用了效果旁路，则返回 ``true``

.. _FmodAudioBusLayout-add_bus_effect:

void add_bus_effect(bus_name: `String`_, effect: :ref:`FmodAudioEffect<FmodAudioEffect>`, index: `int`_ = 0)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

向指定总线添加 :ref:`FmodAudioEffect<FmodAudioEffect>`

效果会应用到该总线的内部通道组

.. _FmodAudioBusLayout-remove_bus_effect:

void remove_bus_effect(bus_name: `String`_, index: `int`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

从指定总线中移除指定索引处的音频效果

.. _FmodAudioBusLayout-get_bus_effect:

:ref:`FmodAudioEffect<FmodAudioEffect>` get_bus_effect(bus_name: `String`_, index: `int`_) const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回指定总线上的指定索引处的 :ref:`FmodAudioEffect<FmodAudioEffect>`

如果总线或效果不存在，则返回 ``null``

.. _FmodAudioBusLayout-sync_from_audio_server:

void sync_from_audio_server()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

将此布局与 Godot `AudioServer`_ 的当前总线布局同步

同步会保留或创建 ``Master`` 总线，重建其他总线，连接父子关系，并同步音量、静音、独奏、旁路状态和支持的 Godot 音频效果

