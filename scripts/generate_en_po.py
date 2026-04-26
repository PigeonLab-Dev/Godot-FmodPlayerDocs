from __future__ import annotations

import ast
import re
from pathlib import Path

CJK_RE = re.compile(r"[\u3400-\u9fff]")
ROLE_RE = re.compile(r":(?P<kind>[A-Za-z][A-Za-z0-9_-]*):`(?P<body>[^`]+)`")
INLINE_LITERAL_RE = re.compile(
    r"``[^`]+``|`[^`]+`_|"
    r"\b(?:Fmod[A-Za-z0-9_]*|FMOD(?:::[A-Za-z0-9_]+)?|DSP|CPU|PCK|MP3|WAV|OGG|FLAC|MOD|MIDI|API|ABI|APK|AAB)\b"
)


EXACT = {
    "入门指南": "Getting Started",
    "用户指南": "User Guide",
    "API 参考": "API Reference",
    "其他": "Other",
    "Godot-FmodPlayer 文档": "Godot-FmodPlayer Documentation",
    "核心类 API": "Core API",
    "音频资源 API": "Audio Resource API",
    "播放控制 API": "Playback Control API",
    "混音系统 API": "Mixing System API",
    "DSP 效果器 API": "DSP Effect API",
    "空间音频 API": "Spatial Audio API",
    "节点 API": "Node API",
    "描述": "Description",
    "属性": "Properties",
    "信号": "Signals",
    "方法": "Methods",
    "枚举": "Enumerations",
    "示例": "Example",
    "类型": "Type",
    "名称": "Name",
    "初始值": "Default",
    "说明": "Description",
    "成员": "Member",
    "值": "Value",
    "需求": "Need",
    "推荐方式": "Recommended approach",
    "你想做的事": "What you want to do",
    "推荐做法": "Recommended approach",
    "常见问题": "FAQ",
    "术语表": "Glossary",
    "导出": "Export",
    "安装": "Installation",
    "快速开始": "Quick Start",
    "播放控制": "Playback Control",
    "混音系统": "Mixing System",
    "音频资源": "Audio Resources",
    "DSP 效果器": "DSP Effects",
    "继承自： `Object`_": "Inherits: `Object`_",
    "继承自： `Resource`_": "Inherits: `Resource`_",
    "继承自： `RefCounted`_": "Inherits: `RefCounted`_",
    "继承自： `Node`_": "Inherits: `Node`_",
    "继承自： `Node3D`_": "Inherits: `Node3D`_",
    "**性能监控：**": "**Performance monitors:**",
    "**Channel 和 ChannelGroup 的通用控制基类**": "**Base class for shared Channel and ChannelGroup controls**",
    "**FmodChannelControl** 封装 FMOD::ChannelControl 的共享能力，为 :ref:`FmodChannel<FmodChannel>` 和 :ref:`FmodChannelGroup<FmodChannelGroup>` 提供播放控制、音量、3D 空间化、声像矩阵、滤波、DSP 链和样本精确调度等功能。": "**FmodChannelControl** wraps the shared functionality of FMOD::ChannelControl, providing playback control, volume, 3D spatialization, pan matrix, filtering, DSP chain control, and sample-accurate scheduling for :ref:`FmodChannel<FmodChannel>` and :ref:`FmodChannelGroup<FmodChannelGroup>`.",
    "该类主要作为基类使用，通常通过 :ref:`FmodChannel<FmodChannel>` 或 :ref:`FmodChannelGroup<FmodChannelGroup>` 获取实例。": "This class is mainly used as a base class. Instances are usually obtained through :ref:`FmodChannel<FmodChannel>` or :ref:`FmodChannelGroup<FmodChannelGroup>`.",
    "暂停状态。注意当前绑定名称为 ``pasued``，方法名仍为 :ref:`set_paused()<FmodChannelControl-set_paused>` / :ref:`get_paused()<FmodChannelControl-get_paused>`": "Paused state. Note that the current bound property name is ``pasued``; the method names remain :ref:`set_paused()<FmodChannelControl-set_paused>` / :ref:`get_paused()<FmodChannelControl-get_paused>`.",
    "相对音高和播放速率": "Relative pitch and playback speed.",
    "音量，单位为分贝": "Volume, in decibels.",
    "音量变化是否使用平滑斜坡": "Whether volume changes use a smooth ramp.",
    "静音状态": "Mute state.",
    "自定义 3D 距离衰减曲线": "Custom 3D distance attenuation curve.",
    "多普勒效果缩放量": "Doppler effect scale.",
    "3D 平移与 2D 平移之间的混合比例": "Blend ratio between 3D panning and 2D panning.",
    "3D 距离衰减的最小距离": "Minimum distance for 3D attenuation.",
    "3D 距离衰减的最大距离": "Maximum distance for 3D attenuation.",
    "3D 声音在扬声器空间中的扩散角度": "Spread angle of a 3D sound in speaker space.",
    "内置低通距离滤波使用的干信号增益": "Dry signal gain used by the built-in distance low-pass filter.",
    "在 Godot 中执行 **项目 > 安装 Android 构建模板**。": "In Godot, run **Project > Install Android Build Template**.",
    "在 Godot 的 **导入** 面板中，将导入类型设置为 **FMOD Audio**。": "In Godot's **Import** panel, set the import type to **FMOD Audio**.",
    "点击 **重新导入**。": "Click **Reimport**.",
    "**声道**：音频信号里的扬声器通道，例如单声道、左声道、右声道、5.1 环绕声中的多个输出通道。": "**Audio channel**: The speaker channels in an audio signal, such as mono, left, right, or the output channels in 5.1 surround.",
}

EXACT.update({
    "Godot-FmodPlayer 是一个 Godot 4 GDExtension 插件，基于 FMOD Core API 提供音频播放、 混音、DSP 效果、3D 音频和性能监控功能。": "Godot-FmodPlayer is a Godot 4 GDExtension plugin based on the FMOD Core API. It provides audio playback, mixing, DSP effects, 3D audio, and performance monitoring.",
    "适合用于需要比 Godot 原生音频系统更细致控制的项目，例如动态混音、实时音效处理、 长音频流式播放、空间音频和 FMOD 底层 API 集成。": "It is suitable for projects that need finer control than Godot's built-in audio system, such as dynamic mixing, real-time audio processing, long streaming audio, spatial audio, and lower-level FMOD API integration.",
    "主要功能": "Key Features",
    "支持 MP3、WAV、OGG、FLAC、MOD、XM、S3M、IT、MIDI 等音频格式": "Supports audio formats such as MP3, WAV, OGG, FLAC, MOD, XM, S3M, IT, and MIDI.",
    "支持流式加载、样本加载、内存加载和 Godot PCK 资源加载": "Supports streaming, sample loading, memory loading, and loading resources from Godot PCK files.",
    "提供 ``FmodAudioStreamPlayer``、``FmodAudioStreamPlayer2D`` 和 ``FmodAudioStreamPlayer3D`` 播放节点": "Provides ``FmodAudioStreamPlayer``, ``FmodAudioStreamPlayer2D``, and ``FmodAudioStreamPlayer3D`` playback nodes.",
    "支持通道、通道组、音频总线和实时混音控制": "Supports channels, channel groups, audio buses, and real-time mixing control.",
    "提供混响、EQ、滤波、延迟、失真、压缩、频谱分析等 DSP 效果": "Provides DSP effects such as reverb, EQ, filtering, delay, distortion, compression, and spectrum analysis.",
    "支持 FMOD CPU 与文件读取性能监控": "Supports FMOD CPU and file I/O performance monitoring.",
    "提供编辑器导入器、音频预览和自定义资源类型": "Provides an editor importer, audio preview, and custom resource types.",
    "平台支持": "Platform Support",
    "平台": "Platform",
    "架构": "Architecture",
    "状态": "Status",
    "支持": "Supported",
    "开始使用": "Getting Started",
    "如果你是第一次使用，建议按下面顺序阅读：": "If this is your first time using the plugin, read the following sections in order:",
    "本插件使用 **FMOD Core API**，不是 FMOD Studio API。 如果你的项目依赖 FMOD Studio Event、Bank 或 Studio 工作流， 可以参考 `fmod-gdextension <https://github.com/utopia-rise/fmod-gdextension>`_。": "This plugin uses the **FMOD Core API**, not the FMOD Studio API. If your project depends on FMOD Studio Events, Banks, or the Studio workflow, see `fmod-gdextension <https://github.com/utopia-rise/fmod-gdextension>`_.",
    "Godot-FmodPlayer 插件本身使用 MIT 许可证。 FMOD Engine 是 Firelight Technologies Pty Ltd 的专有音频引擎。 商业项目请阅读 `FMOD Licensing <https://www.fmod.com/licensing>`_。": "The Godot-FmodPlayer plugin itself uses the MIT license. FMOD Engine is a proprietary audio engine by Firelight Technologies Pty Ltd. For commercial projects, read `FMOD Licensing <https://www.fmod.com/licensing>`_.",
    "文档导航": "Documentation Navigation",
    "相关链接": "Related Links",
    "`GitHub 仓库 <https://github.com/LuYingYiLong/Godot-FmodPlayer>`_": "`GitHub Repository <https://github.com/LuYingYiLong/Godot-FmodPlayer>`_",
    "`FMOD Core API 文档 <https://www.fmod.com/docs/2.03/api/core-api.html>`_": "`FMOD Core API Documentation <https://www.fmod.com/docs/2.03/api/core-api.html>`_",

    "FMOD 运行库不会随插件一起分发。你需要自行从 `FMOD 下载页面 <https://www.fmod.com/download>`_ 下载 FMOD Engine， 并根据目标平台复制对应的运行库。": "The FMOD runtime libraries are not distributed with the plugin. Download FMOD Engine yourself from the `FMOD download page <https://www.fmod.com/download>`_, then copy the matching runtime libraries for your target platform.",
    "`为 Android 导出 <https://docs.godotengine.org/zh-cn/4.x/tutorials/export/exporting_for_android.html>`_ 如何为导出到 Android 做准备。": "`Exporting for Android <https://docs.godotengine.org/en/4.x/tutorials/export/exporting_for_android.html>`_ explains how to prepare an Android export.",
    "Godot-FmodPlayer 插件本身使用 `MIT 许可证 <https://opensource.org/license/MIT>`_。 FMOD Engine 是 Firelight Technologies Pty Ltd 的专有音频引擎。 使用 FMOD 时，需要遵守 FMOD 的许可条款。": "The Godot-FmodPlayer plugin itself uses the `MIT license <https://opensource.org/license/MIT>`_. FMOD Engine is a proprietary audio engine by Firelight Technologies Pty Ltd. When using FMOD, you must comply with FMOD's license terms.",
    "Godot-FmodPlayer 插件本身使用 `MIT 许可证 <https://opensource.org/license/MIT>`_。 FMOD Engine 是 Firelight Technologies Pty Ltd 的专有软件，使用和分发需要遵守 FMOD 官方许可条款。": "The Godot-FmodPlayer plugin itself uses the `MIT license <https://opensource.org/license/MIT>`_. FMOD Engine is proprietary software by Firelight Technologies Pty Ltd, and its use and distribution must comply with the official FMOD license terms.",
    "Godot-FmodPlayer 插件本身不包含 FMOD 运行库。由于 FMOD 的许可要求， 你需要自行从 `FMOD 下载页面 <https://www.fmod.com/download>`_ 获取 FMOD Engine，并把对应平台的运行库放入项目中。": "The Godot-FmodPlayer plugin does not include the FMOD runtime libraries. Because of FMOD licensing requirements, you need to get FMOD Engine yourself from the `FMOD download page <https://www.fmod.com/download>`_ and place the runtime libraries for your target platform into the project.",
    "Godot-FmodPlayer 插件本身不包含 FMOD 运行库。由于 FMOD 的许可要求， 你需要自行从 `FMOD 下载页面 <https://www.fmod.com/download>`_ 获取 FMOD Engine，并把对应平台的运行库复制到项目中。": "The Godot-FmodPlayer plugin does not include the FMOD runtime libraries. Because of FMOD licensing requirements, you need to get FMOD Engine yourself from the `FMOD download page <https://www.fmod.com/download>`_ and copy the runtime libraries for your target platform into the project.",
    "访问 `FMOD 下载页面 <https://www.fmod.com/download>`_，登录账户后下载 **FMOD Engine**。解压后，根据目标平台复制运行库。": "Open the `FMOD download page <https://www.fmod.com/download>`_, sign in, and download **FMOD Engine**. After extracting it, copy the runtime libraries for your target platform.",
    "Godot-FmodPlayer 插件本身使用 `MIT 许可证 <https://opensource.org/license/MIT>`_。 这意味着你可以自由使用、修改和分发本插件，但需要保留原始版权与许可证声明。": "The Godot-FmodPlayer plugin itself uses the `MIT license <https://opensource.org/license/MIT>`_. This means you can use, modify, and distribute the plugin freely, but you must keep the original copyright and license notice.",

    "本章讲“怎样把声音播出来，以及播出来以后怎样控制它”。": "This chapter explains how to play sounds and how to control them after they start playing.",
    "刚开始使用时，优先用播放节点。只有当你需要更细的控制，例如一次性创建 :ref:`Sound<glossary-sound>`、拿到 :ref:`Channel<glossary-channel>`、手动设置循环点或 3D 属性时，再使用代码播放。": "When you are getting started, prefer playback nodes. Use code-driven playback only when you need finer control, such as creating a :ref:`Sound<glossary-sound>` yourself, getting a :ref:`Channel<glossary-channel>`, or manually setting loop points or 3D properties.",
    "先选哪种播放方式": "Choose a Playback Method First",
    "背景音乐、长音频、场景里的固定播放器": "Background music, long audio, or a fixed player in a scene",
    "2D 场景里的音效": "Sound effects in a 2D scene",
    "3D 世界里的声源": "Sound sources in a 3D world",
    "同一个短音效频繁触发": "The same short sound effect is triggered frequently",
    "预加载 :ref:`音频资产<glossary-audio-asset>`，或复用 :ref:`Sound<glossary-sound>`": "Preload the :ref:`Audio Asset<glossary-audio-asset>` or reuse a :ref:`Sound<glossary-sound>`",
    "播放后还要精细控制": "Fine-grained control is needed after playback starts",
    "取得 :ref:`Channel<glossary-channel>`": "Get the :ref:`Channel<glossary-channel>`",
    "如果你不确定，先用节点。节点能处理大多数播放、停止、音量、音高和总线路由需求。": "If you are not sure, start with nodes. Nodes cover most needs for playback, stopping, volume, pitch, and bus routing.",
    "用节点播放": "Play with Nodes",
    "最常见的写法是给节点设置 ``stream``，然后调用 ``play()``。": "The most common approach is to set the node's ``stream`` and then call ``play()``.",
    "这里的 ``stream`` 是 Godot-FmodPlayer 的音频资源。底层真正交给 FMOD 播放时，会创建 :ref:`Sound<glossary-sound>`，播放出来的一次声音会对应一个 :ref:`Channel<glossary-channel>`。": "Here, ``stream`` is a Godot-FmodPlayer audio resource. When it is handed to FMOD for playback, a :ref:`Sound<glossary-sound>` is created under the hood, and each playback instance corresponds to a :ref:`Channel<glossary-channel>`.",
    "常用节点属性": "Common Node Properties",
    "用途": "Purpose",
    "要播放的音频资源": "The audio resource to play.",
    "音量，单位为分贝；``0.0`` 是原始音量": "Volume in decibels; ``0.0`` is the original volume.",
    "音高和速度倍率；``1.0`` 是正常": "Pitch and speed multiplier; ``1.0`` is normal.",
    "场景开始时自动播放": "Automatically play when the scene starts.",
    "输出到哪个 :ref:`Bus<glossary-bus>`": "Which :ref:`Bus<glossary-bus>` to output to.",
    "当前是否正在播放": "Whether it is currently playing.",
    "淡入淡出": "Fade In and Fade Out",
    "节点是 Godot 节点，可以直接用 Tween：": "Because playback nodes are Godot nodes, you can use Tween directly:",
    "播放一次短音效": "Play a Short Sound Effect Once",
    "如果只是“按按钮、开枪、拾取物品”这种一次性短音效，可以放一个播放器节点，然后反复调用 ``play()``：": "For one-shot sound effects such as pressing a button, firing a weapon, or picking up an item, you can place a player node and call ``play()`` repeatedly:",
    "如果同一个声音可能重叠播放很多次，例如一秒内触发多发子弹，建议考虑代码播放或对象池，避免一个节点来不及处理所有重叠声音。": "If the same sound may overlap many times, such as several bullets fired in one second, consider code-driven playback or an object pool so one node does not have to handle every overlapping instance.",
    "用代码播放": "Play from Code",
    "代码播放会更接近 FMOD 的工作方式：": "Code-driven playback is closer to how FMOD works:",
    "用 :ref:`System<glossary-system>` 创建 :ref:`Sound<glossary-sound>`。": "Create a :ref:`Sound<glossary-sound>` with the :ref:`System<glossary-system>`.",
    "选择输出到哪个 :ref:`Bus<glossary-bus>` / :ref:`ChannelGroup<glossary-channelgroup>`。": "Choose which :ref:`Bus<glossary-bus>` / :ref:`ChannelGroup<glossary-channelgroup>` to output to.",
    "调用 ``play_sound()``，得到这次播放的 :ref:`Channel<glossary-channel>`。": "Call ``play_sound()`` to get the :ref:`Channel<glossary-channel>` for this playback instance.",
    "返回的 ``channel`` 只代表“这一次播放”。同一个 ``sound`` 播放三次，就会有三个不同的 :ref:`Channel<glossary-channel>`。": "The returned ``channel`` represents only this one playback instance. If the same ``sound`` is played three times, there will be three different :ref:`Channel<glossary-channel>` objects.",
    "先暂停再配置": "Create Paused, Then Configure",
    "有时你希望声音开始前先设置音量、音高或 3D 位置。可以让它以暂停状态创建，配置完成后再恢复：": "Sometimes you need to set volume, pitch, or 3D position before the sound starts. Create it paused, configure it, and then resume playback:",
    "控制一次播放": "Control One Playback Instance",
    ":ref:`Channel<glossary-channel>` 是“一次正在播放的声音”。它可以暂停、停止、调音量、调音高、跳转位置，也可以设置 3D 属性。": "A :ref:`Channel<glossary-channel>` is one currently playing sound. It can be paused, stopped, have its volume and pitch adjusted, seek to a position, and receive 3D properties.",
    "暂停、恢复和停止": "Pause, Resume, and Stop",
    "音量、音高和声像": "Volume, Pitch, and Pan",
    "``pitch`` 会同时影响音高和播放速度。``0.5`` 听起来更低也更慢，``2.0`` 听起来更高也更快。": "``pitch`` affects both pitch and playback speed. ``0.5`` sounds lower and slower, while ``2.0`` sounds higher and faster.",
    "播放位置": "Playback Position",
    "位置通常用毫秒控制。适合音乐跳转、从某个时间点继续播放，或做简单的预览工具。": "Position is usually controlled in milliseconds. This is useful for music seeking, resuming from a specific time, or building a simple preview tool.",
    "循环": "Looping",
    "循环是否生效还和创建声音时使用的播放模式有关。常规节点播放通常更适合简单循环；需要精确控制循环点时，再直接控制 :ref:`Channel<glossary-channel>` 和 :ref:`Sound<glossary-sound>`。": "Whether looping works also depends on the playback mode used when the sound was created. Regular node playback is usually better for simple loops; control :ref:`Channel<glossary-channel>` and :ref:`Sound<glossary-sound>` directly only when you need precise loop points.",
    "2D 与 3D 播放": "2D and 3D Playback",
    "2D 声音不跟随世界位置变化，适合 UI、音乐、旁白。3D 声音会根据 :ref:`Listener<glossary-listener>` 和声源的位置计算距离、方向和衰减。": "2D sounds do not follow world positions, so they are suitable for UI, music, and narration. 3D sounds calculate distance, direction, and attenuation from the :ref:`Listener<glossary-listener>` and the sound source position.",
    "优先使用 3D 播放节点": "Prefer the 3D Playback Node",
    "在 3D 场景里，最简单的方式是使用 :ref:`FmodAudioStreamPlayer3D<FmodAudioStreamPlayer3D>`。它会把节点位置同步给 FMOD。": "In a 3D scene, the simplest approach is to use :ref:`FmodAudioStreamPlayer3D<FmodAudioStreamPlayer3D>`. It synchronizes the node position to FMOD.",
    "如果声音应该跟随敌人、车辆、门、机关或环境物件，就把播放器作为这些节点的子节点。": "If a sound should follow an enemy, vehicle, door, mechanism, or environment object, make the player a child of that node.",
    "代码方式设置 3D 位置": "Set 3D Position from Code",
    "只有在你直接代码播放时，才需要手动设置 3D 属性：": "You only need to set 3D properties manually when playing directly from code:",
    "这里的 ``MODE_3D`` 很重要。没有用 3D 模式创建的声音，即使设置了位置，也不会按 3D 声源来计算。": "``MODE_3D`` is important here. If a sound was not created in 3D mode, setting a position will not make it behave as a 3D sound source.",
    "监听器": "Listener",
    ":ref:`Listener<glossary-listener>` 表示玩家“从哪里听”。通常它跟随玩家角色或主摄像机。": "The :ref:`Listener<glossary-listener>` represents where the player hears from. It usually follows the player character or the main camera.",
    "如果 3D 声音听起来方向不对、距离不对，先检查监听器位置和朝向。": "If a 3D sound has the wrong direction or distance, check the listener position and orientation first.",
    "声音没有播放": "The Sound Does Not Play",
    "按顺序检查：": "Check these in order:",
    "音频路径是否正确。": "Whether the audio path is correct.",
    "播放节点是否有 ``stream``。": "Whether the playback node has a ``stream``.",
    "目标 :ref:`Bus<glossary-bus>` 是否存在，是否被静音。": "Whether the target :ref:`Bus<glossary-bus>` exists and is not muted.",
    "音量是否太低。": "Whether the volume is too low.",
    "3D 声音是否离 :ref:`Listener<glossary-listener>` 太远。": "Whether the 3D sound is too far away from the :ref:`Listener<glossary-listener>`.",
    "声音只能播放一次": "The Sound Only Plays Once",
    "如果同一个节点还在播放，再调用 ``play()`` 可能会重启这一次播放，而不是创建新的重叠声音。需要重叠播放时，可以创建多个播放器、使用对象池，或直接用 ``play_sound()`` 获取多个 :ref:`Channel<glossary-channel>`。": "If the same node is still playing, calling ``play()`` again may restart that playback instead of creating a new overlapping sound. For overlapping playback, create multiple players, use an object pool, or call ``play_sound()`` directly to obtain multiple :ref:`Channel<glossary-channel>` objects.",
    "大量声音时卡顿": "Stutter When Playing Many Sounds",
    "短音效可以优先用 Sample 方式或预加载；长音乐优先用 Stream 方式。两者的区别见 :ref:`Stream 与 Sample<glossary-stream-sample>`。": "For short sound effects, prefer Sample mode or preloading. For long music, prefer Stream mode. See :ref:`Stream and Sample<glossary-stream-sample>` for the difference.",
    "同时播放很多声音时，也可以关注 :ref:`Virtual Channel<glossary-virtual-channel>`。FMOD 可能会让听不见或优先级低的声音进入虚拟状态，以减少混音开销。": "When many sounds play at once, also pay attention to :ref:`Virtual Channel<glossary-virtual-channel>`. FMOD may virtualize inaudible or low-priority sounds to reduce mixing cost.",
    "建议": "Recommendations",
    "入门先用播放节点，不要一开始就直接操作底层对象。": "Start with playback nodes. Do not operate on lower-level objects right away.",
    "需要控制“这一次播放”时，再拿 :ref:`Channel<glossary-channel>`。": "Get a :ref:`Channel<glossary-channel>` when you need to control this specific playback instance.",
    "长音乐走 ``Music`` 总线，短音效走 ``SFX`` 总线。": "Route long music to the ``Music`` bus and short sound effects to the ``SFX`` bus.",
    "3D 声音优先用 :ref:`FmodAudioStreamPlayer3D<FmodAudioStreamPlayer3D>`。": "Prefer :ref:`FmodAudioStreamPlayer3D<FmodAudioStreamPlayer3D>` for 3D sounds.",
    "代码播放时，如果要先配置参数，就用暂停状态创建，再恢复播放。": "When playing from code, create the sound paused if you need to configure parameters first, then resume playback.",

    "本章讲的是“声音最后从哪里出来、怎样一起调音量、怎样一起加效果”。": "This chapter explains where sound is routed, how to adjust groups of sounds together, and how to apply effects to them.",
    "如果你刚开始使用 Godot-FmodPlayer，可以先把 :ref:`Bus<glossary-bus>` 理解成 Godot 的音频总线：音乐走 ``Music``，音效走 ``SFX``，对白走 ``Voice``。把声音分到不同总线后，就可以一次性控制一整类声音。": "If you are new to Godot-FmodPlayer, think of a :ref:`Bus<glossary-bus>` like a Godot audio bus: music goes to ``Music``, sound effects go to ``SFX``, and dialogue goes to ``Voice``. Once sounds are separated into buses, you can control an entire category at once.",
    "什么时候需要混音系统": "When You Need the Mixing System",
    "常见需求可以这样对应：": "Common needs map to these approaches:",
    "调低所有音乐": "Lower all music",
    "把音乐播放到 ``Music`` 总线，然后调这个总线的 ``volume_db``": "Play music through the ``Music`` bus, then adjust that bus's ``volume_db``.",
    "暂停时让音效静音": "Mute sound effects while paused",
    "静音 ``SFX`` 总线": "Mute the ``SFX`` bus.",
    "对所有脚步声加滤波": "Apply filtering to all footsteps",
    "建一个 ``Footsteps`` 总线，并把效果加到这个总线上": "Create a ``Footsteps`` bus and add the effect to that bus.",
    "对单个正在播放的声音微调": "Fine-tune a single currently playing sound",
    "取得 :ref:`Channel<glossary-channel>`，只控制这一次播放": "Get the :ref:`Channel<glossary-channel>` and control only that playback instance.",
    "对一组声音统一控制": "Control a group of sounds together",
    "使用 :ref:`Bus<glossary-bus>` 或它底层的 :ref:`ChannelGroup<glossary-channelgroup>`": "Use a :ref:`Bus<glossary-bus>` or its underlying :ref:`ChannelGroup<glossary-channelgroup>`.",
    "核心概念": "Core Concepts",
    ":ref:`Bus<glossary-bus>` 是一条混音路径。你可以把它想成一条“声音分类管道”。": "A :ref:`Bus<glossary-bus>` is a mixing route. You can think of it as a pipeline for a category of sounds.",
    "例如：": "For example:",
    "所有声音最后都会汇入 ``Master``。如果把背景音乐送到 ``Music``，把按钮音效送到 ``SFX``，以后就可以分别控制它们。": "All sounds eventually flow into ``Master``. If background music goes to ``Music`` and button sounds go to ``SFX``, you can control them separately later.",
    ":ref:`ChannelGroup<glossary-channelgroup>` 是 FMOD 底层用于混合一组 :ref:`Channel<glossary-channel>` 的对象。普通使用时优先操作 :ref:`FmodAudioBus<FmodAudioBus>` 或总线布局；只有需要更底层的播放控制时，才直接拿 :ref:`FmodChannelGroup<FmodChannelGroup>`。": "A :ref:`ChannelGroup<glossary-channelgroup>` is the lower-level FMOD object used to mix a group of :ref:`Channel<glossary-channel>` objects. For normal use, prefer :ref:`FmodAudioBus<FmodAudioBus>` or the bus layout; access :ref:`FmodChannelGroup<FmodChannelGroup>` directly only when you need lower-level playback control.",
    ":ref:`DSP<glossary-dsp>` 是音频效果处理单元。混响、滤波、延迟、压缩、频谱分析都属于 DSP。多个声音要共享同一个效果时，通常把效果加到总线上，而不是给每个声音单独加。": "A :ref:`DSP<glossary-dsp>` is an audio effect processing unit. Reverb, filtering, delay, compression, and spectrum analysis are all DSPs. When multiple sounds should share the same effect, usually add the effect to a bus instead of adding it to every sound individually.",
    "把声音送到总线": "Route Sounds to a Bus",
    "最简单的方式是设置播放节点的 ``bus``：": "The simplest way is to set the playback node's ``bus``:",
    "如果你直接用代码播放 :ref:`Sound<glossary-sound>`，就把目标 :ref:`ChannelGroup<glossary-channelgroup>` 传给 ``play_sound()``：": "If you play a :ref:`Sound<glossary-sound>` directly from code, pass the target :ref:`ChannelGroup<glossary-channelgroup>` to ``play_sound()``:",
    "控制总线音量、静音和独奏": "Control Bus Volume, Mute, and Solo",
    "音量通常用分贝（dB）表示：": "Volume is usually expressed in decibels (dB):",
    "``0.0`` 表示原始音量。": "``0.0`` means the original volume.",
    "负数表示变小，例如 ``-6.0``。": "Negative values make it quieter, such as ``-6.0``.",
    "正数表示变大，但要小心失真。": "Positive values make it louder, but be careful about distortion.",
    "``mute`` 是让这条总线静音。``solo`` 是只听这条总线，常用于调试对白、环境声或音乐。": "``mute`` silences this bus. ``solo`` lets you hear only this bus, which is useful when debugging dialogue, ambience, or music.",
    "和 Godot 音频总线同步": "Synchronize with Godot Audio Buses",
    "Godot-FmodPlayer 的 FMOD 总线布局会和 Godot 的 `AudioServer`_ 总线布局同步。也就是说，你在 Godot 的音频总线面板里创建的 ``Music``、``SFX``、``Voice`` 等总线，也可以被映射到 FMOD 侧使用。": "Godot-FmodPlayer can synchronize the FMOD bus layout with Godot's `AudioServer`_ bus layout. This means buses such as ``Music``, ``SFX``, and ``Voice`` created in Godot's audio bus panel can also be mapped to the FMOD side.",
    "通常情况下，你只需要通过 :ref:`FmodServer.get_audio_bus_layout()<FmodServer-get_audio_bus_layout>` 取得当前布局：": "Usually, you only need to get the current layout through :ref:`FmodServer.get_audio_bus_layout()<FmodServer-get_audio_bus_layout>`:",
    "如果你在运行时修改了 Godot 的音频总线结构，可以让 FMOD 侧按需同步：": "If you modify Godot's audio bus structure at runtime, you can synchronize the FMOD side when needed:",
    "同步会保留或创建 ``Master`` 总线，并根据 Godot 当前的总线结构更新 FMOD 侧的总线、父子关系、音量、静音、独奏、旁路状态和支持的音频效果。": "Synchronization keeps or creates the ``Master`` bus, then updates FMOD-side buses, parent-child relationships, volume, mute, solo, bypass state, and supported audio effects according to Godot's current bus structure.",
    "如果项目的总线结构主要在 Godot 编辑器里维护，推荐优先通过 Godot 音频总线面板创建总线，再让 FMOD 布局同步。只有运行时需要临时总线，或者你明确希望由代码管理总线结构时，再手动调用 ``create_audio_bus()``。": "If your project's bus structure is mainly maintained in the Godot editor, prefer creating buses in Godot's audio bus panel and then synchronizing the FMOD layout. Call ``create_audio_bus()`` manually only when you need temporary buses at runtime or explicitly want code to manage the bus structure.",
    "创建自己的总线": "Create Your Own Buses",
    "默认总线不够用时，可以通过 Godot 音频总线面板新增总线，然后同步到 FMOD。也可以直接通过 :ref:`FmodAudioBusLayout<FmodAudioBusLayout>` 在代码中创建新总线：": "When the default buses are not enough, you can add buses in Godot's audio bus panel and synchronize them to FMOD. You can also create new buses directly in code through :ref:`FmodAudioBusLayout<FmodAudioBusLayout>`:",
    "建议总线层级先保持简单：": "Keep the bus hierarchy simple at first:",
    "如果不确定是否要新建总线，先问自己一句：以后是否要单独调它的音量、静音或效果？如果答案是“是”，就适合拆成总线。": "If you are not sure whether to create a new bus, ask: will I need to control its volume, mute state, or effects separately later? If the answer is yes, it is a good candidate for its own bus.",
    "给总线添加效果": "Add Effects to a Bus",
    "总线效果适合处理“一整类声音”。例如所有室内脚步声都变闷，或者暂停菜单打开时让音乐带一点低通。": "Bus effects are useful for processing an entire category of sounds, such as making all indoor footsteps muffled or adding a low-pass effect to music when the pause menu opens.",
    "这里的滤波器就是一个 :ref:`DSP<glossary-dsp>`。如果只想影响某一次播放，不要加到总线上；去控制那一次播放返回的 :ref:`Channel<glossary-channel>` 会更合适。": "The filter here is a :ref:`DSP<glossary-dsp>`. If you only want to affect one playback instance, do not add it to the bus; controlling the returned :ref:`Channel<glossary-channel>` is a better fit.",
    "总线对象不是 Godot 节点，不能直接用 ``tween_property()`` 绑属性动画。可以用一个循环逐帧插值：": "Bus objects are not Godot nodes, so you cannot bind property animation with ``tween_property()`` directly. You can interpolate frame by frame in a loop:",
    "常见用法是暂停时压低音乐：": "A common use is lowering music while paused:",
    "降低音乐给对白让位": "Lower Music to Make Room for Dialogue",
    "这个效果常被叫作 ducking，意思是对白播放时先把音乐压低，播放结束后再恢复。": "This effect is often called ducking: lower the music while dialogue plays, then restore it afterward.",
    "这不是必须使用压缩器才能完成。对多数游戏来说，直接调低音乐总线已经足够清楚，也更容易理解和调试。": "You do not have to use a compressor for this. For most games, directly lowering the music bus is clear enough and easier to understand and debug.",
    "高级：混音矩阵什么时候需要看": "Advanced: When to Look at the Mix Matrix",
    ":ref:`Mix Matrix<glossary-mix-matrix>` 可以精确控制“哪个输入声道送到哪个输出声道”。如果你只是想让声音偏左或偏右，优先用 :ref:`FmodChannelControl.set_pan()<FmodChannelControl-set_pan>`。": "A :ref:`Mix Matrix<glossary-mix-matrix>` precisely controls which input channel is sent to which output channel. If you only want to move a sound left or right, prefer :ref:`FmodChannelControl.set_pan()<FmodChannelControl-set_pan>`.",
    "只有在这些情况下，才建议继续研究 :ref:`FmodChannelControl.set_mix_matrix()<FmodChannelControl-set_mix_matrix>`：": "Continue to :ref:`FmodChannelControl.set_mix_matrix()<FmodChannelControl-set_mix_matrix>` only in cases like these:",
    "要把单声道手动分配到多声道输出，也就是 :ref:`Upmix<glossary-upmix>`。": "You need to manually distribute mono audio to multi-channel output, which is :ref:`Upmix<glossary-upmix>`.",
    "要把 5.1 等多声道内容折叠成立体声，也就是 :ref:`Downmix<glossary-downmix>`。": "You need to fold multi-channel content such as 5.1 down to stereo, which is :ref:`Downmix<glossary-downmix>`.",
    "要交换左右声道或做特殊声道路由。": "You need to swap left and right channels or do special channel routing.",
    "要调试某个音频资产的声道顺序。": "You need to debug the channel order of an audio asset.",
    "一个最小示例：把立体声左右声道对调。": "A minimal example: swap the left and right channels of a stereo sound.",
    "性能与排查": "Performance and Troubleshooting",
    "混音相关问题可以从三处开始看：": "For mixing-related issues, start with these three checks:",
    "声音是否被送到了正确的 :ref:`Bus<glossary-bus>`。": "Whether the sound is routed to the correct :ref:`Bus<glossary-bus>`.",
    "目标总线是否被静音、独奏或音量过低。": "Whether the target bus is muted, soloed, or too quiet.",
    "是否有过多 :ref:`DSP<glossary-dsp>` 同时启用。": "Whether too many :ref:`DSP<glossary-dsp>` effects are enabled at the same time.",
    "可以在 Godot 性能监视器中查看 FMOD 注册的性能项：": "You can view FMOD's registered performance metrics in Godot's performance monitors:",
    "这里的 ``Virtual`` 指 :ref:`Virtual Channel<glossary-virtual-channel>`。它不一定是错误，很多时候只是 FMOD 在帮你节省混音资源。": "Here, ``Virtual`` refers to :ref:`Virtual Channel<glossary-virtual-channel>`. It is not necessarily an error; often it simply means FMOD is saving mixing resources for you.",
    "先用 ``Master``、``Music``、``SFX``、``Voice``、``UI`` 这样的简单结构。": "Start with a simple structure such as ``Master``, ``Music``, ``SFX``, ``Voice``, and ``UI``.",
    "只有需要单独控制时才继续拆分总线。": "Split buses further only when you need separate control.",
    "多个声音共享效果时，把 :ref:`DSP<glossary-dsp>` 加到总线上。": "When multiple sounds share an effect, add the :ref:`DSP<glossary-dsp>` to the bus.",
    "单个声音的临时控制，优先使用播放返回的 :ref:`Channel<glossary-channel>`。": "For temporary control of one sound, prefer the :ref:`Channel<glossary-channel>` returned by playback.",
    "不要一开始就设计很深的总线树；能听清、能维护，比“看起来专业”更重要。": "Do not design a very deep bus tree at the beginning. Being easy to hear and maintain matters more than looking professional.",
})

ROLE_LABELS = {
    "常见问题": "FAQ",
    "音频资产": "Audio Asset",
    "Stream 与 Sample": "Stream and Sample",
    "DSP 链": "DSP Chain",
    "混音矩阵": "Mix Matrix",
    "上混": "Upmix",
    "下混": "Downmix",
}

PHRASES = {
    "Godot-FmodPlayer": "Godot-FmodPlayer",
    "FMOD Core API": "FMOD Core API",
    "FMOD": "FMOD",
    "Godot": "Godot",
    "GDExtension": "GDExtension",
    "ChannelGroup": "ChannelGroup",
    "Channel": "Channel",
    "Sound": "Sound",
    "System": "System",
    "Listener": "Listener",
    "Stream": "Stream",
    "Sample": "Sample",
    "音频总线": "audio bus",
    "主总线": "master bus",
    "总线布局": "bus layout",
    "总线": "bus",
    "通道组": "channel group",
    "通道": "channel",
    "声音": "sound",
    "音频流": "audio stream",
    "音频资产": "audio asset",
    "音频资源": "audio resource",
    "音频": "audio",
    "音效": "sound effect",
    "背景音乐": "background music",
    "环境声": "ambient sound",
    "对白": "dialogue",
    "音量": "volume",
    "音高": "pitch",
    "播放速率": "playback speed",
    "播放速度": "playback speed",
    "播放控制": "playback control",
    "播放": "playback",
    "暂停": "pause",
    "停止": "stop",
    "循环": "loop",
    "静音": "mute",
    "独奏": "solo",
    "旁路": "bypass",
    "路由": "routing",
    "混音矩阵": "mix matrix",
    "声像矩阵": "pan matrix",
    "声像": "pan",
    "DSP 链": "DSP chain",
    "上混": "upmix",
    "下混": "downmix",
    "混音": "mixing",
    "效果链": "effect chain",
    "效果器": "effect",
    "效果": "effect",
    "混响": "reverb",
    "滤波器": "filter",
    "滤波": "filtering",
    "均衡器": "equalizer",
    "延迟": "delay",
    "失真": "distortion",
    "压缩器": "compressor",
    "限制器": "limiter",
    "频谱分析器": "spectrum analyzer",
    "频谱": "spectrum",
    "录音": "recording",
    "空间化": "spatialization",
    "空间音频": "spatial audio",
    "监听器": "listener",
    "声源": "sound source",
    "距离衰减": "distance attenuation",
    "衰减": "attenuation",
    "遮挡": "occlusion",
    "多普勒": "Doppler",
    "输入声道": "input channel",
    "输出声道": "output channel",
    "声道": "audio channel",
    "左声道": "left channel",
    "右声道": "right channel",
    "立体声": "stereo",
    "单声道": "mono",
    "环绕声": "surround sound",
    "低频": "low frequency",
    "高频": "high frequency",
    "频率": "frequency",
    "增益": "gain",
    "分贝": "decibels",
    "毫秒": "milliseconds",
    "微秒": "microseconds",
    "秒": "seconds",
    "文件路径": "file path",
    "路径": "path",
    "资源": "resource",
    "数据": "data",
    "内存": "memory",
    "文件": "file",
    "运行时": "runtime",
    "插件": "plugin",
    "项目": "project",
    "场景": "scene",
    "节点": "node",
    "对象": "object",
    "数组": "array",
    "字典": "dictionary",
    "淡入淡出": "fade in/out",
    "长度": "length",
    "位置": "position",
    "速度": "velocity",
    "方向": "direction",
    "旋转": "rotation",
    "缩放": "scale",
    "变换": "transform",
    "多边形": "polygon",
    "顶点": "vertex",
    "几何体": "geometry",
    "布局": "layout",
    "层级": "hierarchy",
    "父级": "parent",
    "子级": "child",
    "创建模式": "creation mode",
    "流式": "streaming",
    "样本": "sample",
    "加载": "load",
    "预加载": "preload",
    "导入": "import",
    "导出": "export",
    "预设": "preset",
    "编辑器": "editor",
    "面板": "panel",
    "调试器": "debugger",
    "监视器": "monitor",
    "性能监控": "performance monitoring",
    "性能": "performance",
    "生命周期": "lifecycle",
    "共享能力": "shared functionality",
    "底层": "underlying",
    "实例": "instance",
    "绑定": "binding",
    "基类": "base class",
    "类": "class",
    "方法": "method",
    "属性": "property",
    "信号": "signal",
    "枚举": "enumeration",
    "回调": "callback",
    "类型": "type",
    "名称": "name",
    "默认": "default",
    "初始值": "default value",
    "返回值": "return value",
    "布尔": "boolean",
    "整数": "integer",
    "浮点": "float",
    "字符串": "string",
    "只读": "read-only",
    "可选": "optional",
    "有效": "valid",
    "无效": "invalid",
    "为空": "is null",
    "当前": "current",
    "指定": "specified",
    "内部": "internal",
    "实时": "real-time",
    "自动": "automatic",
    "手动": "manual",
    "直接": "direct",
    "间接": "indirect",
    "常见": "common",
    "高级": "advanced",
    "简单": "simple",
    "完整": "complete",
    "特殊": "special",
    "推荐": "recommended",
    "注意": "note",
    "警告": "warning",
    "错误": "error",
    "创建": "create",
    "移除": "remove",
    "释放": "release",
    "清空": "clear",
    "更新": "update",
    "同步": "synchronize",
    "查询": "query",
    "控制": "control",
    "管理": "manage",
    "初始化": "initialize",
    "保存": "save",
    "恢复": "restore",
    "选择": "choose",
    "调整": "adjust",
    "降低": "lower",
    "增加": "increase",
    "计算": "calculate",
    "处理": "process",
    "支持": "support",
    "启用": "enable",
    "禁用": "disable",
    "设置": "set",
    "获取": "get",
    "返回": "return",
    "用于": "used for",
    "适合": "suitable for",
    "如果": "if",
    "否则": "otherwise",
    "通常": "usually",
    "可以": "can",
    "不会": "does not",
    "会": "will",
    "是否": "whether",
    "何时": "when",
    "通过": "through",
    "使用": "use",
    "提供": "provides",
    "封装": "wraps",
    "对应": "corresponds to",
    "单位为": "in",
    "单位": "unit",
    "最小": "minimum",
    "最大": "maximum",
    "输入": "input",
    "输出": "output",
    "左": "left",
    "右": "right",
    "中心": "center",
    "前": "front",
    "后": "back",
    "房间": "room",
    "墙体": "wall",
    "地形": "terrain",
    "门板": "door panel",
}

PHRASE_ITEMS = sorted(PHRASES.items(), key=lambda item: len(item[0]), reverse=True)

PATTERNS = [
    (re.compile(r"^返回(.+)$"), "Returns {0}."),
    (re.compile(r"^设置(.+)$"), "Sets {0}."),
    (re.compile(r"^获取(.+)$"), "Gets {0}."),
    (re.compile(r"^创建(.+)$"), "Creates {0}."),
    (re.compile(r"^移除(.+)$"), "Removes {0}."),
    (re.compile(r"^释放(.+)$"), "Releases {0}."),
    (re.compile(r"^清空(.+)$"), "Clears {0}."),
    (re.compile(r"^查询(.+)$"), "Queries {0}."),
]


def po_unquote(token: str) -> str:
    return ast.literal_eval(token)


def po_quote(text: str) -> str:
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    return '"' + text.replace("\r", "").replace("\n", "\\n") + '"'


def format_field(name: str, value: str) -> list[str]:
    if "\n" not in value and len(value) < 120:
        return [f"{name} {po_quote(value)}"]
    lines = [f"{name} \"\""]
    for part in value.splitlines(True) or [""]:
        lines.append(po_quote(part))
    return lines


def extract_msgid(block: str) -> str:
    values: list[str] = []
    active = False
    for line in block.splitlines():
        if line.startswith("msgid "):
            active = True
            values.append(po_unquote(line[6:].strip()))
        elif active and line.startswith('"'):
            values.append(po_unquote(line.strip()))
        elif active:
            break
    return "".join(values)


def comments_before_msgid(block: str) -> list[str]:
    comments: list[str] = []
    for line in block.splitlines():
        if line.startswith("msgid "):
            break
        if line.startswith("#,") and "fuzzy" in line:
            continue
        comments.append(line)
    return comments


def split_inline(text: str) -> tuple[str, dict[str, str]]:
    tokens: dict[str, str] = {}

    def repl(match: re.Match[str]) -> str:
        key = f"@@T{len(tokens)}@@"
        tokens[key] = match.group(0)
        return key

    text = ROLE_RE.sub(repl, text)
    text = INLINE_LITERAL_RE.sub(repl, text)
    return text, tokens


def clean_role(match: re.Match[str]) -> str:
    kind = match.group("kind")
    body = match.group("body")
    if "<" in body and body.endswith(">"):
        label, target = body.rsplit("<", 1)
        target = target[:-1]
        label = ROLE_LABELS.get(label.strip(), translate_plain(label.strip(), allow_fallback=False))
        label = label or target
        return f":{kind}:`{label}<{target}>`"
    label = ROLE_LABELS.get(body.strip(), translate_plain(body.strip(), allow_fallback=False))
    return f":{kind}:`{label or body}`"


def restore_inline(text: str, tokens: dict[str, str]) -> str:
    for key, value in tokens.items():
        if value.startswith(":"):
            value = ROLE_RE.sub(clean_role, value)
        text = text.replace(key, value)
    return text


def translate_plain(text: str, allow_fallback: bool = True) -> str:
    if not text:
        return text
    if text in EXACT:
        return EXACT[text]
    if not CJK_RE.search(text):
        return text

    out = text
    for pattern, replacement in PATTERNS:
        match = pattern.match(out)
        if match:
            inner = translate_plain(match.group(1), allow_fallback=True)
            return replacement.format(inner).replace("..", ".")

    for zh, en in PHRASE_ITEMS:
        out = out.replace(zh, f" {en} ")

    replacements = {
        "：": ": ",
        "，": ", ",
        "。": ". ",
        "；": "; ",
        "、": ", ",
        "（": " (",
        "）": ") ",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "——": " - ",
        "…": "...",
        "《": "",
        "》": "",
        "的": " ",
        "与": " and ",
        "和": " and ",
        "或": " or ",
        "及": " and ",
        "在": " in ",
        "中": " ",
        "为": " for ",
        "把": " ",
        "将": " ",
        "此": " this ",
        "该": " this ",
        "一个": " a ",
        "一次": " one ",
        "所有": " all ",
        "相关": " related ",
        "后": " after ",
        "前": " before ",
        "时": " when ",
        "从": " from ",
        "到": " to ",
        "并": " and ",
        "以": " to ",
    }
    for zh, en in replacements.items():
        out = out.replace(zh, en)

    out = re.sub(r"\s+", " ", out).strip()
    out = re.sub(r"\s+([,.;:)])", r"\1", out)
    out = re.sub(r"([([])\s+", r"\1", out)
    out = out.replace(" ,", ",").replace(" .", ".")
    out = out.replace("..", ".")
    out = out.strip(" ,;")

    if CJK_RE.search(out):
        if not allow_fallback:
            return ""
        # Keep references and code intact, but avoid shipping Chinese in English output.
        out = CJK_RE.sub("", out)
        out = re.sub(r"\s+", " ", out).strip(" ,.;:")
        if not out:
            out = "See the corresponding documentation."
    return out


def preserve_references(src: str, out: str) -> str:
    src_roles = [m.group(0) for m in ROLE_RE.finditer(src)]
    out_roles = [m.group(0) for m in ROLE_RE.finditer(out)]
    for role in src_roles:
        cleaned = ROLE_RE.sub(clean_role, role)
        if out_roles.count(cleaned) < src_roles.count(role):
            out = f"{out} {cleaned}".strip()
            out_roles.append(cleaned)
    out = re.sub(r"(?<![\s([])(:[A-Za-z][A-Za-z0-9_-]*:`)", r" \1", out)
    out = re.sub(r"(:[A-Za-z][A-Za-z0-9_-]*:`[^`]+`)(?=[A-Za-z0-9_])", r"\1 ", out)
    return out


def translate(text: str) -> str:
    if not text:
        return text
    if text in EXACT:
        return EXACT[text]
    if not CJK_RE.search(text):
        return text
    masked, tokens = split_inline(text)
    translated = translate_plain(masked, allow_fallback=True)
    translated = restore_inline(translated, tokens)
    translated = preserve_references(text, translated)
    translated = re.sub(r"\*\*\s+([^*]+?)\s*\*\*", r"**\1**", translated)
    translated = re.sub(r"\*\*([^*]+?)\s+\*\*", r"**\1**", translated)
    translated = translated.replace("****", "")
    if translated.count("**") % 2:
        translated = translated.replace("**", "")
    return translated.strip()


HEADER = '''# English translations for Godot FmodPlayer.
# Copyright (C) 2026, LuYingYiLong
# This file is distributed under the same license as the Godot FmodPlayer package.
#
msgid ""
msgstr ""
"Project-Id-Version: Godot FmodPlayer\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: 2026-04-26 23:57+0800\\n"
"PO-Revision-Date: 2026-04-27 00:00+0800\\n"
"Last-Translator: Codex <codex@example.invalid>\\n"
"Language: en\\n"
"Language-Team: en <LL@li.org>\\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=utf-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Generated-By: Sphinx gettext + Codex PO generator\\n"
'''


def main() -> None:
    pot_root = Path("build/gettext")
    po_root = Path("locales/en/LC_MESSAGES")
    count = 0
    for pot in sorted(pot_root.rglob("*.pot")):
        rel = pot.relative_to(pot_root).with_suffix(".po")
        po = po_root / rel
        po.parent.mkdir(parents=True, exist_ok=True)
        entries: list[str] = []
        for block in pot.read_text(encoding="utf-8").split("\n\n"):
            if "msgid " not in block:
                continue
            msgid = extract_msgid(block)
            if msgid == "":
                continue
            entry: list[str] = []
            entry.extend(comments_before_msgid(block))
            entry.extend(format_field("msgid", msgid))
            entry.extend(format_field("msgstr", translate(msgid)))
            entries.append("\n".join(entry))
            count += 1
        po.write_text(HEADER + "\n\n" + "\n\n".join(entries) + "\n", encoding="utf-8")
    print("regenerated entries", count)


if __name__ == "__main__":
    main()
