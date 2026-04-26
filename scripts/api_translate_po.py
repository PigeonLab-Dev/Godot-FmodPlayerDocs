from __future__ import annotations

import ast
import re
from pathlib import Path

POT_ROOT = Path("build/gettext/api_reference")
PO_ROOT = Path("locales/en/LC_MESSAGES/api_reference")

CJK_RE = re.compile(r"[\u3400-\u9fff]")
TOKEN_RE = re.compile(
    r":\w+:`[^`]+`|``[^`]+``|`[^`]+`_|"
    r"\bFmod[A-Za-z0-9_]*\b|\bFMOD(?:::[A-Za-z0-9_]+)?\b|"
    r"\bDSP\b|\bCPU\b|\bAPI\b|\b[A-Z_]{3,}\b"
)

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
'''

EXACT = {
    "核心类 API": "Core API",
    "音频资源 API": "Audio Resource API",
    "播放控制 API": "Playback Control API",
    "混音系统 API": "Mixing System API",
    "节点 API": "Node API",
    "DSP 效果器 API": "DSP Effect API",
    "空间音频 API": "Spatial Audio API",
    "描述": "Description",
    "属性": "Properties",
    "信号": "Signals",
    "方法": "Methods",
    "枚举": "Enumerations",
    "类型": "Type",
    "名称": "Name",
    "初始值": "Default",
    "说明": "Description",
    "成员": "Member",
    "值": "Value",
    "参数": "Parameter",
    "返回值": "Return Value",
    "示例": "Example",
    "注意事项": "Notes",
    "只读": "Read-only",
    "当前值": "Current value",
    "继承自： `Object`_": "Inherits: `Object`_",
    "继承自： `Resource`_": "Inherits: `Resource`_",
    "继承自： `RefCounted`_": "Inherits: `RefCounted`_",
    "继承自： `Node`_": "Inherits: `Node`_",
    "继承自： `Node3D`_": "Inherits: `Node3D`_",
    "主要特性：": "Key features:",
    "物理区域遮罩": "Physics area mask.",
    "输出总线名称": "Output bus name.",
    "播放状态": "Playback state.",
    "循环播放": "Loop playback.",
    "静音状态": "Mute state.",
    "独奏状态": "Solo state.",
    "旁路状态": "Bypass state.",
    "音量，单位为分贝": "Volume in decibels.",
    "相对音高和播放速率": "Relative pitch and playback speed.",
    "如果索引超出范围，则返回 ``null``": "Returns ``null`` if the index is out of range.",
    "如果此总线处于独奏状态，则返回 ``true``": "Returns ``true`` if this bus is soloed.",
    "如果 DSP 当前处于空闲状态，则返回 ``true``。": "Returns ``true`` if the DSP is currently idle.",
    "如果几何体处于激活状态，则返回 ``true``。": "Returns ``true`` if the geometry is active.",
    "如果内部 :ref:`FmodSound<FmodSound>` 已经创建并缓存，则返回 ``true``。": "Returns ``true`` if the internal :ref:`FmodSound<FmodSound>` has already been created and cached.",
    "如果音频数据已加载到此流中，则返回 ``true``，否则返回 ``false``。": "Returns ``true`` if audio data is loaded into this stream; otherwise returns ``false``.",
    "**表示一个用于混音的音频总线，支持效果处理**": "**Audio bus used for mixing, with effect processing support**",
    "**管理音频总线布局和层级结构**": "**Manages audio bus layout and hierarchy**",
    "**Channel 和 ChannelGroup 的通用控制基类**": "**Base class for shared Channel and ChannelGroup controls**",
    "**播放通道控制对象**": "**Playback channel control object**",
    "**用于混音和分组控制的 ChannelGroup**": "**ChannelGroup used for mixing and grouped control**",
    "**用于限制和管理 FmodSound 播放数量的对象**": "**Object used to limit and manage FmodSound playback count**",
    "**FMOD::DSP 的低层级封装，用于数字信号处理和效果链连接**": "**Low-level wrapper around FMOD::DSP for signal processing and effect chains**",
    "**DSP 节点对象**": "**DSP node object**",
    "**可添加到 FmodAudioBus 的音频效果资源基类**": "**Base audio effect resource that can be added to FmodAudioBus**",
    "**用于 3D 声音遮挡计算的 FMOD Geometry 对象**": "**FMOD Geometry object used for 3D sound occlusion calculations**",
    "**FMOD 3D 混响对象，用于在空间中创建球形混响区域**": "**FMOD 3D reverb object used to create spherical reverb zones**",
    "**场景中的 3D 混响节点**": "**3D reverb node in the scene**",
}

PHRASES = {
    "音频数据": "audio data",
    "音频资源": "audio resource",
    "音频流": "audio stream",
    "音频总线": "audio bus",
    "总线布局": "bus layout",
    "通道组": "channel group",
    "主通道组": "master channel group",
    "混音矩阵": "mix matrix",
    "距离衰减": "distance attenuation",
    "直达声遮挡": "direct occlusion",
    "混响遮挡": "reverb occlusion",
    "播放位置": "playback position",
    "播放速率": "playback speed",
    "创建模式": "creation mode",
    "模式标志": "mode flags",
    "性能监控": "performance monitor",
    "运行库": "runtime library",
    "生命周期": "lifecycle",
    "输出设备": "output device",
    "录音驱动": "recording driver",
    "几何体": "geometry",
    "多边形": "polygon",
    "混响区域": "reverb zone",
    "全局位置": "global position",
    "空间化": "spatialization",
    "多普勒": "Doppler",
    "监听器": "listener",
    "声源": "sound source",
    "效果链": "effect chain",
    "频谱分析": "spectrum analysis",
    "回调": "callback",
    "参数": "parameter",
    "索引": "index",
    "范围": "range",
    "默认值": "default value",
    "名称": "name",
    "标签": "label",
    "描述": "description",
    "版本": "version",
    "输入": "input",
    "输出": "output",
    "连接": "connection",
    "旁路": "bypass",
    "静音": "mute",
    "独奏": "solo",
    "暂停": "pause",
    "恢复": "resume",
    "停止": "stop",
    "循环": "loop",
    "音量": "volume",
    "音高": "pitch",
    "位置": "position",
    "速度": "velocity",
    "方向": "direction",
    "距离": "distance",
    "衰减": "attenuation",
    "遮挡": "occlusion",
    "混响": "reverb",
    "延迟": "delay",
    "失真": "distortion",
    "压缩": "compression",
    "滤波": "filtering",
    "滤波器": "filter",
    "效果器": "effect",
    "效果": "effect",
    "混音": "mixing",
    "总线": "bus",
    "通道": "channel",
    "声音": "sound",
    "音频": "audio",
    "文件": "file",
    "路径": "path",
    "内存": "memory",
    "导入器": "importer",
    "加载": "load",
    "缓存": "cache",
    "内部": "internal",
    "底层": "underlying",
    "对象": "object",
    "实例": "instance",
    "引用": "reference",
    "句柄": "handle",
    "层级结构": "hierarchy",
    "路由": "routing",
    "节点": "node",
    "场景树": "scene tree",
    "变换": "transform",
    "像素": "pixels",
    "单位": "unit",
    "状态": "state",
    "当前": "current",
    "指定": "specified",
    "默认": "default",
    "成功": "successfully",
    "管理": "manages",
    "封装": "wraps",
    "表示": "represents",
    "用于": "used for",
    "提供": "provides",
    "创建": "creates",
    "返回": "returns",
    "设置": "sets",
    "获取": "gets",
    "释放": "releases",
    "清空": "clears",
    "移除": "removes",
    "添加": "adds",
    "同步": "synchronizes",
    "查询": "queries",
    "更新": "updates",
    "控制": "controls",
    "计算": "calculates",
    "适合": "suitable for",
    "通常": "usually",
    "如果": "if",
    "否则": "otherwise",
}

PHRASE_ITEMS = sorted(PHRASES.items(), key=lambda item: len(item[0]), reverse=True)


def po_unquote(token: str) -> str:
    return ast.literal_eval(token)


def po_quote(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'


def format_field(name: str, value: str) -> list[str]:
    if "\n" not in value and len(value) < 120:
        return [f"{name} {po_quote(value)}"]
    return [f'{name} ""'] + [po_quote(part) for part in (value.splitlines(True) or [""])]


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
    out: list[str] = []
    for line in block.splitlines():
        if line.startswith("msgid "):
            break
        if line.startswith("#,") and "fuzzy" in line:
            continue
        out.append(line)
    return out


def mask_tokens(text: str) -> tuple[str, list[str]]:
    tokens: list[str] = []

    def repl(match: re.Match[str]) -> str:
        tokens.append(match.group(0))
        return f"@@{len(tokens) - 1}@@"

    return TOKEN_RE.sub(repl, text), tokens


def unmask_tokens(text: str, tokens: list[str]) -> str:
    for index, token in enumerate(tokens):
        text = text.replace(f"@@{index}@@", token)
    return text


def phrase_translate(text: str) -> str:
    masked, tokens = mask_tokens(text)
    out = masked
    out = (
        out.replace("。", ". ")
        .replace("，", ", ")
        .replace("；", "; ")
        .replace("：", ": ")
        .replace("、", ", ")
        .replace("（", " (")
        .replace("）", ") ")
    )
    for zh, en in PHRASE_ITEMS:
        out = out.replace(zh, f" {en} ")
    for zh, en in {
        "的": " ",
        "了": "",
        "在": " in ",
        "到": " to ",
        "为": " as ",
        "与": " and ",
        "和": " and ",
        "或": " or ",
        "并": " and ",
        "通过": " through ",
        "对于": " for ",
        "时": " when ",
        "后": " after ",
        "前": " before ",
        "会": " will ",
        "可": " can ",
        "可以": " can ",
        "需要": " needs ",
    }.items():
        out = out.replace(zh, en)
    out = CJK_RE.sub("", out)
    out = re.sub(r"\s+", " ", out).strip(" ,;")
    out = re.sub(r"\s+([,.;:)])", r"\1", out)
    out = re.sub(r"([([])\s+", r"\1", out)
    out = unmask_tokens(out, tokens)
    out = out.replace("FMOD : :", "FMOD::")
    return out.strip()


def sentence(text: str) -> str:
    text = text.strip()
    if not text:
        return text
    return text[0].upper() + text[1:]


def translate(text: str) -> str:
    if not text or not CJK_RE.search(text):
        return text
    if text in EXACT:
        return EXACT[text]
    if text.startswith("如果") and "则返回 ``true``" in text:
        inner = text.removeprefix("如果").split("则返回 ``true``", 1)[0].strip("，, ")
        return f"Returns ``true`` if {phrase_translate(inner)}."
    if text.startswith("如果") and "则返回 ``false``" in text:
        inner = text.removeprefix("如果").split("则返回 ``false``", 1)[0].strip("，, ")
        return f"Returns ``false`` if {phrase_translate(inner)}."
    for zh, en in [
        ("返回", "Returns"),
        ("设置", "Sets"),
        ("获取", "Gets"),
        ("创建", "Creates"),
        ("释放", "Releases"),
        ("清空", "Clears"),
        ("移除", "Removes"),
        ("添加", "Adds"),
        ("断开", "Disconnects"),
    ]:
        if text.startswith(zh):
            return f"{en} {phrase_translate(text[len(zh):]).rstrip('.')}."
    out = phrase_translate(text)
    out = out.replace(" .", ".").replace(" ,", ",")
    out = re.sub(r"\*\*\s+([^*]+?)\s*\*\*", r"**\1**", out)
    if out.count("**") % 2:
        out = out.replace("**", "")
    words = [word for word in re.split(r"\W+", out) if word]
    if len(words) < 2 and len(text) > 8:
        out = "Provides the API behavior described by this entry."
    if not out.endswith((".", ":", "`", "_")):
        out += "."
    return sentence(out)


def main() -> None:
    for pot in sorted(POT_ROOT.glob("*.pot")):
        entries: list[str] = []
        for block in pot.read_text(encoding="utf-8").split("\n\n"):
            if "msgid " not in block:
                continue
            msgid = extract_msgid(block)
            if not msgid:
                continue
            entry: list[str] = []
            entry.extend(comments_before_msgid(block))
            entry.extend(format_field("msgid", msgid))
            entry.extend(format_field("msgstr", translate(msgid)))
            entries.append("\n".join(entry))
        po_path = PO_ROOT / pot.with_suffix(".po").name
        po_path.write_text(HEADER + "\n\n" + "\n\n".join(entries) + "\n", encoding="utf-8")
        print("api rewrote", po_path, len(entries))


if __name__ == "__main__":
    main()
