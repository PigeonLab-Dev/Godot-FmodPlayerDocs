混合器 API
==========

.. _FmodAudioBus:

FmodAudioBus
------------

继承自： `RefCounted`_

**表示一个用于混音的音频总线，支持效果处理**

描述
~~~~

FmodAudioBus 表示 FMOD 音频系统中的音频混音总线。每个总线都有自己的通道组用于音频路由，并且可以应用多个音频效果

总线由 **FmodAudioBusLayout** 管理的层级结构组织。主总线是该层级的根，所有其他总线最终通过它进行路由

使用总线可以：

- 将音频组织成逻辑分类（音乐、音效、对话等）
- 对一组声音应用效果
- 控制整个音频类别的音量和路由
- 实现混音的独奏/静音功能

属性
~~~~

.. list-table::

   * - `bool`_
     - bypass
     - false
   * - `bool`_
     - mute
     - false
   * - `bool`_
     - solo
     - false
   * - `float`_
     - volume
     - 0.0

方法
~~~~

.. list-table::

   * - void
     - add_effect(effect: FmodAudioEffect, index: `int`_ = 0)
   * - void
     - apply_mute()
   * - FmodChannelGroup
     - get_bus() const
   * - `String`_
     - get_bus_name() const
   * - :ref:`FmodAudioEffect<FmodAudioEffect>`
     - get_effect(index: `int`_) const
   * - FmodChannelGroup
     - get_parent() const
   * - void
     - init_bus(name: String, parent: FmodChannelGroup = null)
   * - void
     - remove_effect(index: `int`_)
   * - void
     - remove_effect(index: `int`_)
   * - void
     - set_parent(parent: FmodChannelGroup)
   * - void
     - sync_bypass()

方法说明
~~~~~~~~

.. glossary::

  void add_effect(effect: FmodAudioEffect, index: int = 0)
    在效果链中指定的索引位置向此总线添加一个音频效果

    如果索引为负数或超过当前效果数量，效果将追加到末尾

    效果链按顺序处理，每个效果传递到下一个效果
  
  `float`_ apply_mute(mute: `bool`_)
    根据传入的 ``mute`` 参数设置总线的静音状态，并返回更新后的音量值

  FmodChannelGroup get_bus() const
    返回此总线用于音频路由的 **FmodChannelGroup**

    如果总线尚未初始化，则返回 ``null``
  
  `String`_ get_bus_name() const
    返回此音频总线的名称
  
  FmodAudioEffect get_effect(index: `int`_) const
    返回效果链中指定索引处的 **FmodAudioEffect**

    如果索引超出范围，则返回 ``null``
  
  FmodChannelGroup get_parent() const
    返回此总线输出到的父 **FmodChannelGroup**

    对于主总线返回 ``null``
  
  void init_bus(name: `String`_, parent: FmodChannelGroup = null)
    使用指定的名称和可选的父通道组初始化此总线

    这将为音频路由创建内部 FMOD 通道组
  
  void remove_effect(index: `int`_)
    从此总线中移除指定索引处的音频效果
  
  void set_parent(parent: FmodChannelGroup)
    设置此总线输出到的父通道组
  
  void sync_bypass()
    将此总线的旁路状态同步到 FMOD 系统。这对于在更改旁路属性后确保效果链正确更新很有用

.. _FmodAudioBusLayout:

FmodAudioBusLayout
------------------

继承自：Resource

**管理音频总线的布局和层级**

描述
~~~~

**FmodAudioBusLayout** 管理 FMOD 音频系统中音频总线的完整层级结构。它维护了 **FmodAudioBus** 实例及其相互关系的集合

该布局会自动与 Godot 的 **AudioServer** 总线布局同步，实现与 Godot 内置音频系统的无缝集成

主要特性：

- 总线层级管理（主总线及子总线）
- 每个总线的音量、独奏和静音状态控制
- 每个总线的效果链管理
- 与 Godot **AudioServer** 的同步

方法
~~~~

.. list-table::

   * - void
     - add_bus_effect(bus_name: `String`_, effect: FmodAudioEffect, index: `int`_ = 0)
   * - `bool`_
     - bus_is_bypass(name: `String`_) const
   * - `bool`_
     - bus_is_mute(name: `String`_) const
   * - `bool`_
     - bus_is_solo(name: `String`_) const
   * - void
     - create_audio_bus(name: `String`_, parent: FmodAudioBus = null)
   * - :ref:`FmodAudioBus<FmodAudioBus>`
     - get_audio_bus(name: `String`_) const
   * - :ref:`FmodAudioEffect<FmodAudioEffect>`
     - get_bus_effect(bus_name: `String`_, index: `int`_) const
   * - `float`_
     - get_bus_volume(name: `String`_) const
   * - `bool`_
     - has_audio_bus(name: `String`_) const
   * - void
     - remove_audio_effect(bus_name: `String`_, index: `int`_)
   * - void
     - remove_bus_effect(bus_name: `String`_, index: `int`_)
   * - void
     - set_bus_bypass(name: `String`_, mute: `bool`_)
   * - void
     - set_bus_mute(name: `String`_, mute: `bool`_)
   * - void
     - set_bus_volume(name: `String`_, volume_db: `float`_)
   * - void
     - sync_from_audio_server()

方法说明
~~~~~~~~

.. glossary::

  void add_bus_effect(bus_name: `String`_, effect: FmodAudioEffect, index: `int`_ = 0)
    在效果链中指定索引处向指定的总线添加 **FmodAudioEffect**

  `bool`_ bus_is_bypass(name: `String`_) const
    如果为指定的总线启用了效果绕过，则返回 **true**
  
  `bool`_ bus_is_mute(name: `String`_) const
    如果指定的总线被静音，则返回 **true**
  
  `bool`_ bus_is_solo(name: `String`_) const
    如果指定的总线处于独奏模式，则返回 **true**
  
  void create_audio_bus(name: `String`_, parent: FmodAudioBus = null)
    使用指定的名称和可选的父级创建一个新的音频总线

    主总线会自动创建，不应手动创建
  
  :ref:`FmodAudioBus<FmodAudioBus>` get_audio_bus(name: `String`_) const
    返回具有指定名称的 **FmodAudioBus**

    如果不存在具有该名称的总线，则返回 **null**
  
  :ref:`FmodAudioEffect<FmodAudioEffect>` get_bus_effect(bus_name: `String`_, index: `int`_) const
    返回指定总线上的指定索引处的 **FmodAudioEffect**

    如果总线或效果不存在，则返回 **null**
  
  `float`_ get_bus_volume(name: `String`_) const
    返回指定总线的音量（以分贝为单位）
  
  `bool`_ has_audio_bus(name: `String`_) const
    如果布局中存在具有指定名称的总线，则返回 **true**
  
  void remove_audio_bus(name: `String`_)
    从布局中移除指定名称的音频总线

    .. note:: 主总线无法被移除
  
  void remove_bus_effect(bus_name: `String`_, index: `int`_)
    从指定总线中移除指定索引处的音频效果
  
  void set_bus_bypass(name: `String`_, bypass: `bool`_)
    启用或禁用指定总线上的效果绕过
  
  void set_bus_mute(name: `String`_, mute: `bool`_)
    静音或取消静音指定的总线
  
  void set_bus_volume(name: `String`_, volume_db: `float`_)
    设置指定总线的音量（以分贝为单位）
  
  void sync_from_audio_server()
    将此布局与 Godot **AudioServer** 的当前总线布局同步。这将创建任何缺失的总线并更新现有总线以匹配 **AudioServer** 的状态