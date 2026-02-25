混音系统
========

Godot-FmodPlayer 提供专业级的混音系统，支持音频总线、通道组和实时参数调整。

核心概念
--------

音频总线（Audio Bus）
~~~~~~~~~~~~~~~~~~~~~

音频总线是混音系统的基本单元，用于组织和控制一组音频通道。每个总线都有自己的音量、效果和路由设置。

通道组（Channel Group）
~~~~~~~~~~~~~~~~~~~~~~~~

通道组是 FMOD 底层的混音概念，``FmodAudioBus`` 对其进行了包装，提供更友好的接口。

总线布局（Bus Layout）
~~~~~~~~~~~~~~~~~~~~~~

总线布局定义了项目中所有音频总线的结构，与 Godot 的 AudioServer 同步。

使用音频总线
------------

默认总线结构
~~~~~~~~~~~~

插件初始化时会创建与 Godot AudioServer 同步的总线结构::

    Master
    ├── Music
    ├── SFX
    ├── Voice
    └── Ambient

将声音路由到总线
~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    extends Node

    @onready var player = $FmodAudioStreamPlayer

    func _ready():
        # 方式 1：通过节点属性
        player.bus = "Music"

    func play_on_bus():
        # 方式 2：代码播放时指定
        var system = FmodServer.main_system
        var sfx_bus = system.get_channel_group_by_name("SFX")
        
        var sound = system.create_sound_from_file("res://sfx/hit.wav")
        var channel = system.play_sound(sound, sfx_bus, false)

控制总线参数
~~~~~~~~~~~~

.. code-block:: gdscript

    func control_bus():
        var system = FmodServer.main_system
        var music_bus = system.get_channel_group_by_name("Music")
        
        # 设置音量（分贝）
        music_bus.set_volume_db(-12.0)
        
        # 静音
        music_bus.set_mute(true)
        
        # 独奏（静音其他总线）
        music_bus.set_solo(true)
        
        # 暂停该总线下所有通道
        music_bus.set_paused(true)

自定义总线布局
--------------

创建总线
~~~~~~~~

.. code-block:: gdscript

    func create_custom_bus():
        var layout = FmodServer.get_audio_bus_layout()
        
        # 在 Master 下创建新总线
        var ui_bus = layout.create_audio_bus("UI", "Master")
        
        # 设置初始音量
        ui_bus.set_volume_db(-6.0)

嵌套总线
~~~~~~~~

.. code-block:: gdscript

    func create_nested_buses():
        var layout = FmodServer.get_audio_bus_layout()
        
        # 创建 SFX 子总线
        var weapon_bus = layout.create_audio_bus("Weapons", "SFX")
        var footstep_bus = layout.create_audio_bus("Footsteps", "SFX")
        
        # 创建层级结构
        # Master -> SFX -> Weapons
        #            -> Footsteps

程序化总线管理
~~~~~~~~~~~~~~

.. code-block:: gdscript

    extends Node

    var bus_volumes: Dictionary = {}

    func _ready():
        # 保存原始音量
        save_bus_volumes()

    func save_bus_volumes():
        var system = FmodServer.main_system
        var master = system.get_master_channel_group()
        
        # 遍历所有子总线
        var num_buses = master.get_num_groups()
        for i in range(num_buses):
            var bus = master.get_group(i)
            bus_volumes[bus.get_name()] = bus.get_volume_db()

    func mute_all_except(bus_name: String):
        var system = FmodServer.main_system
        var master = system.get_master_channel_group()
        
        var num_buses = master.get_num_groups()
        for i in range(num_buses):
            var bus = master.get_group(i)
            bus.set_mute(bus.get_name() != bus_name)

    func restore_all_buses():
        var system = FmodServer.main_system
        var master = system.get_master_channel_group()
        
        var num_buses = master.get_num_groups()
        for i in range(num_buses):
            var bus = master.get_group(i)
            var name = bus.get_name()
            if bus_volumes.has(name):
                bus.set_volume_db(bus_volumes[name])
            bus.set_mute(false)

混音技术
--------

淡入淡出
~~~~~~~~

.. code-block:: gdscript

    func fade_bus(bus_name: String, target_db: float, duration: float):
        var system = FmodServer.main_system
        var bus = system.get_channel_group_by_name(bus_name)
        
        var tween = create_tween()
        tween.set_trans(Tween.TRANS_LINEAR)
        tween.set_ease(Tween.EASE_IN_OUT)
        
        # 注意：这里需要使用自定义的音量插值方法
        # 因为 ChannelGroup 不支持直接 tween
        var start_db = bus.get_volume_db()
        var elapsed = 0.0
        
        while elapsed < duration:
            await get_tree().process_frame
            elapsed += get_process_delta_time()
            var t = elapsed / duration
            var current_db = lerp(start_db, target_db, t)
            bus.set_volume_db(current_db)

侧链压缩（Ducking）
~~~~~~~~~~~~~~~~~~~~

当语音播放时自动降低音乐音量：

.. code-block:: gdscript

    extends Node

    @onready var voice_player = $VoicePlayer
    var music_bus: FmodChannelGroup
    var normal_music_db: float = 0.0
    var ducked_music_db: float = -12.0

    func _ready():
        var system = FmodServer.main_system
        music_bus = system.get_channel_group_by_name("Music")
        normal_music_db = music_bus.get_volume_db()

    func play_voice(path: String):
        # 降低音乐
        duck_music(true)
        
        # 播放语音
        var system = FmodServer.main_system
        var voice_bus = system.get_channel_group_by_name("Voice")
        var sound = system.create_sound_from_file(path)
        var channel = system.play_sound(sound, voice_bus, false)
        
        # 监听语音结束
        while channel.is_playing():
            await get_tree().process_frame
        
        # 恢复音乐
        duck_music(false)

    func duck_music(duck: bool):
        var target_db = ducked_music_db if duck else normal_music_db
        fade_bus("Music", target_db, 0.3)

快照系统（Mix Snapshots）
~~~~~~~~~~~~~~~~~~~~~~~~~

保存和恢复混音状态：

.. code-block:: gdscript

    class_name MixSnapshot
    extends RefCounted

    var bus_volumes: Dictionary = {}
    var bus_effects: Dictionary = {}

    static func capture() -> MixSnapshot:
        var snapshot = MixSnapshot.new()
        var system = FmodServer.main_system
        var master = system.get_master_channel_group()
        
        var num_buses = master.get_num_groups()
        for i in range(num_buses):
            var bus = master.get_group(i)
            var name = bus.get_name()
            snapshot.bus_volumes[name] = bus.get_volume_db()
        
        return snapshot

    func apply(duration: float = 0.0):
        var system = FmodServer.main_system
        
        for bus_name in bus_volumes:
            var bus = system.get_channel_group_by_name(bus_name)
            if bus:
                if duration > 0:
                    # 使用 tween 过渡
                    pass  # 实现淡入淡出
                else:
                    bus.set_volume_db(bus_volumes[bus_name])

# 使用示例
var gameplay_snapshot: MixSnapshot
var pause_snapshot: MixSnapshot

func _ready():
    gameplay_snapshot = MixSnapshot.capture()
    
    # 创建暂停时的混音状态
    var system = FmodServer.main_system
    var music = system.get_channel_group_by_name("Music")
    var sfx = system.get_channel_group_by_name("SFX")
    
    music.set_volume_db(-6.0)
    sfx.set_mute(true)
    
    pause_snapshot = MixSnapshot.capture()
    
    # 恢复游戏状态
    gameplay_snapshot.apply()

func on_game_paused():
    pause_snapshot.apply(0.5)  # 0.5秒过渡

func on_game_resumed():
    gameplay_snapshot.apply(0.5)

性能监控
--------

使用 Godot Performance 监视器查看混音性能：

.. code-block:: gdscript

    func _process(delta):
        # 获取 CPU 使用率
        var dsp_usage = Performance.get_monitor("FmodCPUUsage/DSP")
        var stream_usage = Performance.get_monitor("FmodCPUUsage/Stream")
        
        # 获取通道统计
        var system = FmodServer.main_system
        var channels = system.get_channels_playing()
        
        print("DSP: %.2f%% | Real channels: %d | Virtual: %d" % [
            dsp_usage,
            channels["real"],
            channels["virtual"]
        ])

最佳实践
--------

#. **规划总线结构** - 在项目早期设计好总线层级
#. **标准化命名** - 使用统一的命名规范（如 "Music", "SFX", "Voice"）
#. **默认音量归一化** - 所有总线默认 0 dB，通过调整音频文件本身来平衡
#. **使用快照管理状态** - 为不同游戏状态（游戏、暂停、菜单）创建混音快照
#. **避免过多总线** - 总线过多会增加 CPU 开销，保持简洁的层级结构

注意事项
--------

- 总线布局与 Godot AudioServer 同步，修改一个会影响另一个
- 通道组可以嵌套，但建议保持层级不要太深
- 静音和独奏是独立的状态，可以同时设置
- 3D 衰减在通道级别计算，在总线级别混合
