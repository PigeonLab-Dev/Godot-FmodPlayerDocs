空间音频 API
============

.. _FmodGeometry:

FmodGeometry
------------

继承自： `RefCounted`_

**用于 3D 声音遮挡计算的 FMOD 几何体对象**

描述
~~~~

**FmodGeometry** 封装 FMOD Geometry，用多边形描述场景中的墙体、地形、门板等遮挡物。FMOD 会根据声源与监听器之间的几何体计算直达声遮挡和混响遮挡，常用于让 3D 声音在墙后变闷、变小，或减少混响发送。

几何体通常通过 :ref:`FmodSystem.create_geometry()<FmodSystem-create_geometry>` 创建，也可以通过 :ref:`FmodSystem.load_geometry()<FmodSystem-load_geometry>` 从保存后的字节数据加载。

.. note:: 几何遮挡通常需要在初始化 FMOD 系统时启用 ``FMOD_INIT_FLAG_CHANNEL_LOWPASS``，否则低通遮挡效果不会按预期工作。

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
    - true
    - 几何体是否参与遮挡计算
  * - `Vector3`_
    - position
    - Vector3()
    - 几何体在世界空间中的位置
  * - `Vector3`_
    - rotation
    - Vector3()
    - 几何体在世界空间中的旋转，编辑器中按角度显示
  * - `Vector3`_
    - scale
    - Vector3(1, 1, 1)
    - 几何体缩放

方法
~~~~

有效性检查
^^^^^^^^^^

.. _FmodGeometry-geometry_is_valid:

`bool`_ geometry_is_valid() const
+++++++++++++++++++++++++++++++++

如果底层 FMOD Geometry 句柄有效，则返回 ``true``。

.. _FmodGeometry-geometry_is_null:

`bool`_ geometry_is_null() const
++++++++++++++++++++++++++++++++

如果底层 FMOD Geometry 句柄为空或不可用，则返回 ``true``。

多边形
^^^^^^

.. _FmodGeometry-add_polygon:

`int`_ add_polygon(direct_occlusion: `float`_, reverb_occlusion: `float`_, double_sided: `bool`_, vertices: `PackedVector3Array`_)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

向几何体添加一个遮挡多边形，并返回新多边形索引。``direct_occlusion`` 控制直达声遮挡，``reverb_occlusion`` 控制混响路径遮挡，范围通常为 ``0.0`` 到 ``1.0``。

.. _FmodGeometry-set_polygon_attributes:

void set_polygon_attributes(index: `int`_, direct_occlusion: `float`_, reverb_occlusion: `float`_, double_sided: `bool`_)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

修改指定多边形的遮挡属性。

.. _FmodGeometry-get_polygon_attributes:

`Dictionary`_ get_polygon_attributes(index: `int`_) const
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回多边形属性字典，包含 ``direct_occlusion``、``reverb_occlusion`` 和 ``double_sided``。

.. _FmodGeometry-get_polygon_num_vertices:

`int`_ get_polygon_num_vertices(index: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++

返回指定多边形的顶点数量。

.. _FmodGeometry-set_polygon_vertex:

void set_polygon_vertex(index: `int`_, vertex_index: `int`_, vertex: `Vector3`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置指定多边形中的单个顶点位置。

.. _FmodGeometry-get_polygon_vertex:

`Vector3`_ get_polygon_vertex(index: `int`_, vertex_index: `int`_) const
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

返回指定多边形中的单个顶点位置。

.. _FmodGeometry-get_max_polygons:

`Dictionary`_ get_max_polygons() const
++++++++++++++++++++++++++++++++++++++

返回几何体容量信息，通常包含 ``max_polygons`` 和 ``max_vertices``。

变换
^^^^

.. _FmodGeometry-set_position:

void set_position(position: `Vector3`_)
+++++++++++++++++++++++++++++++++++++++

设置几何体位置。

.. _FmodGeometry-get_position:

`Vector3`_ get_position() const
+++++++++++++++++++++++++++++++

返回几何体位置。

.. _FmodGeometry-set_rotation:

void set_rotation(rotation: `Vector3`_)
+++++++++++++++++++++++++++++++++++++++

设置几何体旋转。

.. _FmodGeometry-get_rotation:

`Vector3`_ get_rotation() const
+++++++++++++++++++++++++++++++

返回几何体旋转。

.. _FmodGeometry-set_scale:

void set_scale(scale: `Vector3`_)
+++++++++++++++++++++++++++++++++

设置几何体缩放。

.. _FmodGeometry-get_scale:

`Vector3`_ get_scale() const
++++++++++++++++++++++++++++

返回几何体缩放。

.. _FmodGeometry-set_transform:

void set_transform(transform: `Transform3D`_)
++++++++++++++++++++++++++++++++++++++++++++++

一次性同步几何体的 3D 变换。

状态与资源
^^^^^^^^^^

.. _FmodGeometry-set_active:

void set_active(active: `bool`_)
++++++++++++++++++++++++++++++++

启用或禁用几何体遮挡计算。

.. _FmodGeometry-get_active:

`bool`_ get_active() const
++++++++++++++++++++++++++

如果几何体处于激活状态，则返回 ``true``。

.. _FmodGeometry-get_save_size:

`int`_ get_save_size() const
++++++++++++++++++++++++++++

返回序列化当前几何体所需的字节数。

.. _FmodGeometry-save:

`PackedByteArray`_ save() const
+++++++++++++++++++++++++++++++

将几何体序列化为字节数组，可之后通过 :ref:`FmodSystem.load_geometry()<FmodSystem-load_geometry>` 加载。

.. _FmodGeometry-release:

void release()
++++++++++++++

释放底层 FMOD Geometry。释放后该对象不应继续用于遮挡计算。

.. _FmodReverb3D:

FmodReverb3D
------------

继承自： `RefCounted`_

**FMOD 3D 混响对象，用于在空间中创建球形混响区域**

描述
~~~~

**FmodReverb3D** 表示一个低层级 3D 混响区域。它通过中心位置、最小距离和最大距离定义影响范围：声源在最小距离内获得完整混响，在最小距离到最大距离之间逐渐衰减，超过最大距离则基本不受影响。

通常使用 :ref:`FmodSystem.create_reverb_3d()<FmodSystem-create_reverb_3d>` 创建此对象；如果希望直接放在场景树中并跟随节点位置，请使用 :ref:`FmodReverbZone3D<FmodReverbZone3D>`。

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
    - true
    - 混响是否参与输出
  * - `float`_
    - decay_time
    - 1500.0
    - 混响衰减时间，单位为毫秒
  * - `float`_
    - density
    - 100.0
    - 后期混响密度，范围通常为 ``0.0`` 到 ``100.0``
  * - `float`_
    - diffusion
    - 50.0
    - 回声扩散度，范围通常为 ``0.0`` 到 ``100.0``
  * - `float`_
    - early_delay
    - 7.0
    - 早期反射延迟，单位为毫秒
  * - `float`_
    - early_late_mix
    - 50.0
    - 早期反射与后期混响的混合比例
  * - `float`_
    - hf_decay_ratio
    - 50.0
    - 高频衰减比例
  * - `float`_
    - hf_reference
    - 5000.0
    - 高频参考频率，单位为 Hz
  * - `float`_
    - high_cut
    - 0.0
    - 高频截止或衰减参数
  * - `float`_
    - late_delay
    - 11.0
    - 后期混响延迟，单位为毫秒
  * - `float`_
    - low_shelf_frequency
    - 250.0
    - 低频搁架参考频率，单位为 Hz
  * - `float`_
    - low_shelf_gain
    - 0.0
    - 低频搁架增益，单位为分贝
  * - `float`_
    - wet_level
    - -6.0
    - 混响湿声电平，单位为分贝

方法
~~~~

空间范围
^^^^^^^^

.. _FmodReverb3D-set_3d_attributes:

void set_3d_attributes(position: `Vector3`_, min_distance: `float`_, max_distance: `float`_)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

设置混响区域中心位置、完整混响半径和淡出结束半径。

.. _FmodReverb3D-get_3d_attributes:

`Dictionary`_ get_3d_attributes() const
+++++++++++++++++++++++++++++++++++++++

返回 3D 属性字典，包含 ``position``、``min_distance`` 和 ``max_distance``。

.. _FmodReverb3D-set_properties:

void set_properties(properties: `Dictionary`_)
++++++++++++++++++++++++++++++++++++++++++++++

从字典批量设置混响参数。适合保存和恢复预设。

.. _FmodReverb3D-get_properties:

`Dictionary`_ get_properties() const
++++++++++++++++++++++++++++++++++++

返回当前混响参数字典。

参数
^^^^

.. list-table::
  :header-rows: 1

  * - 方法
    - 说明
  * - ``set_decay_time(decay_time)`` / ``get_decay_time()``
    - 设置或返回混响衰减时间
  * - ``set_early_delay(early_delay)`` / ``get_early_delay()``
    - 设置或返回早期反射延迟
  * - ``set_late_delay(late_delay)`` / ``get_late_delay()``
    - 设置或返回后期混响延迟
  * - ``set_hf_reference(hf_reference)`` / ``get_hf_reference()``
    - 设置或返回高频参考频率
  * - ``set_hf_decay_ratio(hf_decay_ratio)`` / ``get_hf_decay_ratio()``
    - 设置或返回高频衰减比例
  * - ``set_diffusion(diffusion)`` / ``get_diffusion()``
    - 设置或返回混响扩散度
  * - ``set_density(density)`` / ``get_density()``
    - 设置或返回混响密度
  * - ``set_low_shelf_frequency(low_shelf_frequency)`` / ``get_low_shelf_frequency()``
    - 设置或返回低频搁架参考频率
  * - ``set_low_shelf_gain(low_shelf_gain)`` / ``get_low_shelf_gain()``
    - 设置或返回低频搁架增益
  * - ``set_high_cut(high_cut)`` / ``get_high_cut()``
    - 设置或返回高频截止参数
  * - ``set_early_late_mix(early_late_mix)`` / ``get_early_late_mix()``
    - 设置或返回早期/后期混响混合比例
  * - ``set_wet_level(wet_level)`` / ``get_wet_level()``
    - 设置或返回混响湿声电平

状态与资源
^^^^^^^^^^

.. _FmodReverb3D-set_active:

void set_active(active: `bool`_)
++++++++++++++++++++++++++++++++

启用或禁用该混响区域。

.. _FmodReverb3D-get_active:

`bool`_ get_active() const
++++++++++++++++++++++++++

如果混响区域处于激活状态，则返回 ``true``。

.. _FmodReverb3D-reverb_3d_is_valid:

`bool`_ reverb_3d_is_valid() const
++++++++++++++++++++++++++++++++++

如果底层 FMOD Reverb3D 句柄有效，则返回 ``true``。

.. _FmodReverb3D-reverb_3d_is_null:

`bool`_ reverb_3d_is_null() const
+++++++++++++++++++++++++++++++++

如果底层 FMOD Reverb3D 句柄为空或不可用，则返回 ``true``。

.. _FmodReverb3D-release:

void release()
++++++++++++++

释放底层 FMOD Reverb3D。

.. _FmodReverbZone3D:

FmodReverbZone3D
----------------

继承自： `Node3D`_

**场景树中的 3D 混响区域节点**

描述
~~~~

**FmodReverbZone3D** 是 :ref:`FmodReverb3D<FmodReverb3D>` 的节点封装。节点进入场景树后会创建内部混响对象，并使用节点的全局位置作为球形混响区域中心。启用 ``sync_transform`` 时，节点移动会同步到 FMOD 混响区域。

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
    - true
    - 该混响区域是否参与输出
  * - `bool`_
    - sync_transform
    - true
    - 是否每帧同步节点位置到内部混响对象
  * - `float`_
    - min_distance
    - 5.0
    - 完整混响半径
  * - `float`_
    - max_distance
    - 20.0
    - 混响淡出结束半径
  * - :ref:`Preset<FmodReverbZone3D-Preset>`
    - preset
    - PRESET_GENERIC
    - 混响预设；手动修改参数后会切换为 ``PRESET_CUSTOM``
  * - `float`_
    - decay_time
    - 1500.0
    - 混响衰减时间，单位为毫秒
  * - `float`_
    - early_delay
    - 7.0
    - 早期反射延迟，单位为毫秒
  * - `float`_
    - late_delay
    - 11.0
    - 后期混响延迟，单位为毫秒
  * - `float`_
    - hf_reference
    - 5000.0
    - 高频参考频率，单位为 Hz
  * - `float`_
    - hf_decay_ratio
    - 83.0
    - 高频衰减比例
  * - `float`_
    - diffusion
    - 100.0
    - 扩散度
  * - `float`_
    - density
    - 100.0
    - 密度
  * - `float`_
    - low_shelf_frequency
    - 250.0
    - 低频搁架参考频率
  * - `float`_
    - low_shelf_gain
    - 0.0
    - 低频搁架增益
  * - `float`_
    - high_cut
    - 14500.0
    - 高频截止频率
  * - `float`_
    - early_late_mix
    - 96.0
    - 早期/后期混响混合比例
  * - `float`_
    - wet_level
    - -8.0
    - 混响湿声电平，单位为分贝

方法
~~~~

.. _FmodReverbZone3D-get_reverb:

:ref:`FmodReverb3D<FmodReverb3D>` get_reverb() const
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

返回该节点内部创建并管理的 :ref:`FmodReverb3D<FmodReverb3D>`。如果节点尚未进入场景树或创建失败，则返回 ``null``。

.. note:: 其它属性均通过同名 getter / setter 暴露，例如 ``set_min_distance()`` / ``get_min_distance()``、``set_preset()`` / ``get_preset()`` 和 ``set_wet_level()`` / ``get_wet_level()``。

枚举
~~~~

.. _FmodReverbZone3D-Preset:

Preset
^^^^^^

.. list-table::
  :header-rows: 1

  * - 成员
    - 值
    - 说明
  * - PRESET_CUSTOM
    - 0
    - 自定义参数
  * - PRESET_OFF
    - 1
    - 关闭混响
  * - PRESET_GENERIC
    - 2
    - 通用混响
  * - PRESET_PADDED_CELL
    - 3
    - 软包小房间
  * - PRESET_ROOM
    - 4
    - 普通房间
  * - PRESET_BATHROOM
    - 5
    - 浴室
  * - PRESET_LIVING_ROOM
    - 6
    - 客厅
  * - PRESET_STONE_ROOM
    - 7
    - 石室
  * - PRESET_AUDITORIUM
    - 8
    - 礼堂
  * - PRESET_CONCERT_HALL
    - 9
    - 音乐厅
  * - PRESET_CAVE
    - 10
    - 洞穴
  * - PRESET_ARENA
    - 11
    - 竞技场
  * - PRESET_HANGAR
    - 12
    - 机库
  * - PRESET_HALLWAY
    - 13
    - 走廊
  * - PRESET_STONE_CORRIDOR
    - 14
    - 石质走廊
  * - PRESET_ALLEY
    - 15
    - 小巷
  * - PRESET_FOREST
    - 16
    - 森林
  * - PRESET_CITY
    - 17
    - 城市
  * - PRESET_MOUNTAINS
    - 18
    - 山地
  * - PRESET_UNDERWATER
    - 19
    - 水下
