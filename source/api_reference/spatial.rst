空间音频 API
============

本节介绍用于 3D 音频空间化的类，包括几何遮挡、3D 混响区域和声音分组。

FmodGeometry
------------

继承自：RefCounted

用于 3D 音频遮挡计算的几何体对象。

FmodGeometry 用于创建影响 3D 音频传播的几何形状。你可以定义多边形作为遮挡物，根据属性阻挡或衰减声音。

.. note::
   几何遮挡需要在系统初始化时设置 ``FMOD_INIT_FLAG_CHANNEL_LOWPASS`` 标志。

主要功能
~~~~~~~~

- 创建多边形形状阻挡声源和听者之间的路径
- 配置遮挡属性（直达声和混响路径衰减）
- 支持双面多边形
- 在 3D 空间中定位、旋转和缩放几何体
- 序列化几何体数据以高效加载/保存

属性
~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``active``
     - bool
     - 几何体是否参与遮挡计算
   * - ``position``
     - Vector3
     - 几何体在世界空间中的位置
   * - ``rotation``
     - Vector3
     - 几何体在世界空间中的旋转（度）
   * - ``scale``
     - Vector3
     - 几何体的缩放

方法
~~~~

添加多边形
^^^^^^^^^^

.. code-block:: gdscript

    add_polygon(direct_occlusion: float, reverb_occlusion: float, double_sided: bool, num_vertices: int, vertices: Array[Vector3]) -> int

添加多边形到几何体：

- ``direct_occlusion``: 直达声遮挡因子（0.0 = 无遮挡，1.0 = 完全遮挡）
- ``reverb_occlusion``: 混响路径遮挡因子
- ``double_sided``: 是否双面遮挡
- ``num_vertices``: 顶点数量（至少 3 个）
- ``vertices``: 顶点位置数组

返回多边形索引，失败返回 -1。

变换方法
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_position(position)``
     - void
     - 设置几何体位置
   * - ``set_rotation(rotation)``
     - void
     - 设置几何体旋转（度）
   * - ``set_scale(scale)``
     - void
     - 设置几何体缩放
   * - ``get_position()``
     - Vector3
     - 获取位置
   * - ``get_rotation()``
     - Vector3
     - 获取旋转
   * - ``get_scale()``
     - Vector3
     - 获取缩放

多边形操作
^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``get_num_polygons()``
     - int
     - 获取多边形数量
   * - ``get_polygon_attributes(index)``
     - Dictionary
     - 获取多边形属性
   * - ``set_polygon_attributes(index, direct_occlusion, reverb_occlusion, double_sided)``
     - void
     - 设置多边形属性
   * - ``get_polygon_num_vertices(index)``
     - int
     - 获取多边形顶点数
   * - ``get_polygon_vertex(index, vertex_index)``
     - Vector3
     - 获取多边形顶点位置
   * - ``set_polygon_vertex(index, vertex_index, vertex)``
     - void
     - 设置多边形顶点位置

序列化
^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``get_save_size()``
     - int
     - 获取序列化所需字节数
   * - ``save()``
     - PackedByteArray
     - 序列化几何体到字节数组
   * - ``release()``
     - void
     - 释放几何体资源

状态检查
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``geometry_is_valid()``
     - bool
     - 几何体是否有效
   * - ``geometry_is_null()``
     - bool
     - 几何体句柄是否为空
   * - ``get_active()``
     - bool
     - 几何体是否激活
   * - ``set_active(active)``
     - void
     - 设置激活状态

使用示例
~~~~~~~~

**创建墙体遮挡：**

.. code-block:: gdscript

    extends Node3D

    var wall_geometry: FmodGeometry

    func _ready():
        var system = FmodServer.main_system
        
        # 创建几何体（最大 10 个多边形，100 个顶点）
        wall_geometry = system.create_geometry(10, 100)
        
        # 定义墙体矩形（4 个顶点）
        var vertices = [
            Vector3(-5, 0, 0),
            Vector3(5, 0, 0),
            Vector3(5, 3, 0),
            Vector3(-5, 3, 0)
        ]
        
        # 添加双面遮挡多边形
        wall_geometry.add_polygon(
            1.0,    # 完全遮挡直达声
            0.8,    # 强混响遮挡
            true,   # 双面遮挡
            4,      # 4 个顶点
            vertices
        )
        
        # 设置位置
        wall_geometry.position = Vector3(0, 0, 10)

    func _exit_tree():
        if wall_geometry:
            wall_geometry.release()

**动态启用/禁用遮挡：**

.. code-block:: gdscript

    func toggle_door(is_open: bool):
        # 门打开时禁用遮挡，关闭时启用
        wall_geometry.set_active(not is_open)

FmodReverb3D
------------

继承自：RefCounted

3D 混响区域，用于空间音频混响效果。

FmodReverb3D 在 3D 空间中创建球形混响区域，根据与混响中心的距离为声音应用环境混响。这允许你创建真实的空间音频环境，声音进入特定区域（如洞穴、大厅或房间）时变得更加混响。

.. note::
   使用 ``FmodSystem.create_reverb_3d()`` 创建此类的实例。

3D 属性
~~~~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_3d_attributes(position, min_distance, max_distance)``
     - void
     - 设置 3D 属性
   * - ``get_3d_attributes()``
     - Dictionary
     - 获取 3D 属性（position, min_distance, max_distance）

- 当声源在 ``min_distance`` 内时，获得完整混响
- 在 ``min_distance`` 和 ``max_distance`` 之间，混响逐渐衰减
- 超过 ``max_distance``，无混响效果

混响参数
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 默认值
     - 说明
   * - ``decay_time``
     - float
     - 1500.0
     - 混响衰减时间（毫秒）
   * - ``early_delay``
     - float
     - 7.0
     - 早期反射延迟（毫秒）
   * - ``late_delay``
     - float
     - 11.0
     - 后期混响延迟（毫秒）
   * - ``early_late_mix``
     - float
     - 50.0
     - 早期/后期混响混合比例
   * - ``wet_level``
     - float
     - -6.0
     - 湿信号电平（dB）

频率控制
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 默认值
     - 说明
   * - ``hf_decay_ratio``
     - float
     - 50.0
     - 高频衰减比例（%）
   * - ``hf_reference``
     - float
     - 5000.0
     - 高频参考频率（Hz）
   * - ``high_cut``
     - float
     - 0.0
     - 高频截止（dB）
   * - ``low_shelf_frequency``
     - float
     - 250.0
     - 低频参考频率（Hz）
   * - ``low_shelf_gain``
     - float
     - 0.0
     - 低频增益（dB）

密度控制
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 默认值
     - 范围
     - 说明
   * - ``density``
     - float
     - 100.0
     - 0.0-100.0
     - 模态密度
   * - ``diffusion``
     - float
     - 50.0
     - 0.0-100.0
     - 扩散度（回声密度）

状态管理
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_active(active)``
     - void
     - 启用/禁用混响区域
   * - ``get_active()``
     - bool
     - 是否激活
   * - ``reverb_3d_is_valid()``
     - bool
     - 混响是否有效
   * - ``reverb_3d_is_null()``
     - bool
     - 句柄是否为空
   * - ``release()``
     - void
     - 释放资源

使用示例
~~~~~~~~

**创建洞穴混响效果：**

.. code-block:: gdscript

    extends Node3D

    @export var cave_position: Vector3 = Vector3(50, 0, 50)
    var cave_reverb: FmodReverb3D

    func _ready():
        var system = FmodServer.main_system
        
        # 创建 3D 混响区域
        cave_reverb = system.create_reverb_3d()
        
        # 设置位置和影响范围
        cave_reverb.set_3d_attributes(
            cave_position,  # 中心位置
            5.0,            # 5米内完全混响
            20.0            # 20米外无混响
        )
        
        # 配置洞穴混响参数
        cave_reverb.decay_time = 2500.0      # 长衰减（大洞穴）
        cave_reverb.density = 80.0           # 高密度
        cave_reverb.diffusion = 70.0         # 高扩散
        cave_reverb.early_delay = 20.0       # 长早期延迟
        cave_reverb.late_delay = 40.0        # 长后期延迟
        cave_reverb.hf_decay_ratio = 40.0    # 高频快速衰减
        cave_reverb.wet_level = -3.0         # 较强的混响

    func _exit_tree():
        if cave_reverb:
            cave_reverb.release()

**预设配置：**

.. code-block:: gdscript

    func apply_room_preset(reverb: FmodReverb3D, room_type: String):
        match room_type:
            "small_room":
                reverb.decay_time = 500.0
                reverb.early_delay = 5.0
                reverb.density = 70.0
            "hall":
                reverb.decay_time = 2000.0
                reverb.early_delay = 15.0
                reverb.density = 90.0
            "cave":
                reverb.decay_time = 3000.0
                reverb.early_delay = 30.0
                reverb.hf_decay_ratio = 30.0

FmodSoundGroup
--------------

继承自：RefCounted

声音分组，用于控制播放限制和集体行为。

FmodSoundGroup 用于管理具有共享播放约束的声音集合。它允许你限制同时可听到的声音数量，并定义当超过该限制时的行为。

适用场景
~~~~~~~~

- **武器声音** - 限制同时播放数量，防止音频混乱
- **环境音效** - 平滑淡入淡出
- **语音/对话** - 优先播放重要台词

属性
~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 默认值
     - 说明
   * - ``max_audible``
     - int
     - 0
     - 最大同时可听声音数（0 = 无限制）
   * - ``behavior``
     - Behavior
     - FAIL
     - 超过限制时的行为
   * - ``mute_fade_speed``
     - float
     - 0.0
     - 静音淡入淡出速度
   * - ``volume_db``
     - float
     - 0.0
     - 分组音量（dB）

行为枚举
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 常量
     - 值
     - 说明
   * - ``BEHAVIOR_FAIL``
     - 0
     - 超过限制时播放失败
   * - ``BEHAVIOR_MUTE``
     - 1
     - 新声音静音，其他停止后恢复
   * - ``BEHAVIOR_STEAL_LOWEST``
     - 2
     - 抢夺音量最低的声音

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_max_audible(max_audible)``
     - void
     - 设置最大可听数量
   * - ``get_max_audible()``
     - int
     - 获取最大可听数量
   * - ``set_max_audible_behavior(behavior)``
     - void
     - 设置行为模式
   * - ``get_max_audible_behavior()``
     - Behavior
     - 获取行为模式
   * - ``set_mute_fade_speed(speed)``
     - void
     - 设置淡入淡出速度
   * - ``get_mute_fade_speed()``
     - float
     - 获取淡入淡出速度
   * - ``set_volume_db(volume_db)``
     - void
     - 设置分组音量
   * - ``get_volume_db()``
     - float
     - 获取分组音量
   * - ``get_name()``
     - String
     - 获取分组名称
   * - ``get_num_sounds()``
     - int
     - 获取声音数量
   * - ``get_num_playing()``
     - int
     - 获取正在播放的通道数
   * - ``get_sound(index)``
     - FmodSound
     - 获取指定索引的声音
   * - ``stop()``
     - void
     - 停止组内所有声音
   * - ``release()``
     - void
     - 释放分组
   * - ``sound_group_is_valid()``
     - bool
     - 分组是否有效
   * - ``sound_group_is_null()``
     - bool
     - 句柄是否为空

使用示例
~~~~~~~~

**限制武器音效数量：**

.. code-block:: gdscript

    extends Node

    var weapon_sound_group: FmodSoundGroup

    func _ready():
        var system = FmodServer.main_system
        
        # 创建武器声音组
        weapon_sound_group = system.create_sound_group("Weapons")
        
        # 最多同时播放 4 个武器声音
        weapon_sound_group.max_audible = 4
        
        # 超过限制时抢夺音量最低的声音
        weapon_sound_group.behavior = FmodSoundGroup.BEHAVIOR_STEAL_LOWEST
        
        # 设置淡入淡出速度
        weapon_sound_group.mute_fade_speed = 5.0

    func play_weapon_sound(weapon_type: String):
        var system = FmodServer.main_system
        
        # 创建声音并分配到组
        var sound = system.create_sound_from_file(
            "res://sfx/weapons/%s.wav" % weapon_type
        )
        
        # 将声音添加到组（通过 FMOD API）
        # 然后播放
        var channel = system.play_sound(sound, null, false)

    func _exit_tree():
        if weapon_sound_group:
            weapon_sound_group.release()

**环境音效分组控制：**

.. code-block:: gdscript

    extends Node

    var ambient_group: FmodSoundGroup

    func _ready():
        var system = FmodServer.main_system
        ambient_group = system.create_sound_group("Ambience")
        
        # 允许同时播放多个环境音
        ambient_group.max_audible = 10
        
        # 新声音静音等待
        ambient_group.behavior = FmodSoundGroup.BEHAVIOR_MUTE
        
        // 缓慢淡入
        ambient_group.mute_fade_speed = 2.0

    func fade_out_ambience():
        # 降低整个环境音组的音量
        var tween = create_tween()
        tween.tween_method(
            func(vol): ambient_group.volume_db = vol,
            ambient_group.volume_db,
            -80.0,
            3.0
        )

综合示例
--------

**完整的 3D 音频场景：**

.. code-block:: gdscript

    extends Node3D

    var room_geometry: FmodGeometry
    var room_reverb: FmodReverb3D
    var fx_group: FmodSoundGroup

    func _ready():
        setup_room_occlusion()
        setup_room_reverb()
        setup_sound_groups()

    func setup_room_occlusion():
        var system = FmodServer.main_system
        room_geometry = system.create_geometry(100, 1000)
        
        # 创建四面墙体
        var walls = [
            [Vector3(-10, 0, -10), Vector3(10, 0, -10), Vector3(10, 5, -10), Vector3(-10, 5, -10)],  # 后墙
            [Vector3(-10, 0, 10), Vector3(-10, 0, -10), Vector3(-10, 5, -10), Vector3(-10, 5, 10)],   # 左墙
            # ... 其他墙体
        ]
        
        for wall in walls:
            room_geometry.add_polygon(1.0, 0.9, true, wall.size(), wall)

    func setup_room_reverb():
        var system = FmodServer.main_system
        room_reverb = system.create_reverb_3d()
        room_reverb.set_3d_attributes(Vector3.ZERO, 8.0, 15.0)
        room_reverb.decay_time = 1200.0
        room_reverb.diffusion = 60.0

    func setup_sound_groups():
        var system = FmodServer.main_system
        fx_group = system.create_sound_group("Effects")
        fx_group.max_audible = 8
        fx_group.behavior = FmodSoundGroup.BEHAVIOR_STEAL_LOWEST

    func _exit_tree():
        if room_geometry:
            room_geometry.release()
        if room_reverb:
            room_reverb.release()
        if fx_group:
            fx_group.release()
