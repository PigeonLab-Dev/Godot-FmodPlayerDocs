from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "source" / "_static" / "mix_matrix"


@dataclass(frozen=True)
class Diagram:
    filename: str
    title: str
    subtitle: str
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    matrix: tuple[tuple[float, ...], ...]
    formula: tuple[str, ...]


def lerp(a: int, b: int, t: float) -> int:
    return round(a + (b - a) * t)


def cell_color(value: float) -> str:
    amount = min(max(abs(value), 0.0), 1.0)
    if amount == 0.0:
        return "#f5f7fb"
    r = lerp(232, 43, amount)
    g = lerp(240, 118, amount)
    b = lerp(254, 185, amount)
    return f"#{r:02x}{g:02x}{b:02x}"


def text(x: float, y: float, value: str, size: int = 15, weight: str = "400",
         fill: str = "#172033", anchor: str = "middle") -> str:
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="Segoe UI, Arial, sans-serif" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}">{escape(value)}</text>'
    )


def rect(x: float, y: float, w: float, h: float, fill: str,
         stroke: str = "#c7d2e5", radius: int = 8) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="1"/>'
    )


def render(diagram: Diagram) -> str:
    left = 118
    top = 118
    cell_w = 92
    cell_h = 62
    gap = 8
    label_w = 102
    formula_h = 34 * max(1, len(diagram.formula))
    width = left + label_w + len(diagram.inputs) * (cell_w + gap) + 46
    height = top + 42 + len(diagram.outputs) * (cell_h + gap) + formula_h + 54

    parts: list[str] = [
        '<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width} {height}" role="img">',
        "<defs>",
        '<filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">',
        '<feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#64748b" flood-opacity="0.16"/>',
        "</filter>",
        "</defs>",
        rect(16, 16, width - 32, height - 32, "#ffffff", "#dbe4f0", 12),
        text(36, 50, diagram.title, 22, "700", "#111827", "start"),
        text(36, 78, diagram.subtitle, 14, "400", "#526176", "start"),
        text(left + label_w + (len(diagram.inputs) * (cell_w + gap) - gap) / 2, 104, "Input channels", 13, "600", "#64748b"),
        text(34, top + 28 + (len(diagram.outputs) * (cell_h + gap) - gap) / 2, "Output", 13, "600", "#64748b", "start"),
    ]

    for col, label in enumerate(diagram.inputs):
        x = left + label_w + col * (cell_w + gap)
        parts.append(rect(x, top, cell_w, 34, "#eef4ff", "#c7d2e5", 8))
        parts.append(text(x + cell_w / 2, top + 22, label, 13, "700", "#334155"))

    row_start = top + 42
    for row, output in enumerate(diagram.outputs):
        y = row_start + row * (cell_h + gap)
        parts.append(rect(left, y, label_w - gap, cell_h, "#f8fafc", "#c7d2e5", 8))
        parts.append(text(left + (label_w - gap) / 2, y + 38, output, 13, "700", "#334155"))

        for col, value in enumerate(diagram.matrix[row]):
            x = left + label_w + col * (cell_w + gap)
            parts.append(rect(x, y, cell_w, cell_h, cell_color(value), "#b6c6dc", 8))
            fill = "#ffffff" if abs(value) >= 0.82 else "#102033"
            parts.append(text(x + cell_w / 2, y + 39, f"{value:g}", 18, "700", fill))

    formula_y = row_start + len(diagram.outputs) * (cell_h + gap) + 28
    parts.append(text(36, formula_y, "Result", 13, "700", "#64748b", "start"))
    for index, line in enumerate(diagram.formula):
        parts.append(text(118, formula_y + 30 + index * 28, line, 15, "500", "#172033", "start"))

    parts.append("</svg>")
    return "\n".join(parts)


DIAGRAMS = (
    Diagram(
        filename="stereo_identity.svg",
        title="Stereo identity matrix",
        subtitle="Keep left and right channels unchanged.",
        inputs=("In L", "In R"),
        outputs=("Out L", "Out R"),
        matrix=((1.0, 0.0), (0.0, 1.0)),
        formula=("Out L = In L * 1.0 + In R * 0.0", "Out R = In L * 0.0 + In R * 1.0"),
    ),
    Diagram(
        filename="mono_upmix_left_bias.svg",
        title="Mono to stereo upmix",
        subtitle="Send one mono source to two outputs, biased to the left.",
        inputs=("Mono",),
        outputs=("Out L", "Out R"),
        matrix=((1.0,), (0.35,)),
        formula=("Out L = Mono * 1.0", "Out R = Mono * 0.35"),
    ),
    Diagram(
        filename="stereo_downmix_mono.svg",
        title="Stereo to mono downmix",
        subtitle="Fold left and right into one output with headroom.",
        inputs=("In L", "In R"),
        outputs=("Mono",),
        matrix=((0.5, 0.5),),
        formula=("Mono = In L * 0.5 + In R * 0.5",),
    ),
    Diagram(
        filename="surround_downmix_stereo.svg",
        title="5.1 to stereo downmix",
        subtitle="A simplified fold-down from surround channels to left and right.",
        inputs=("FL", "FR", "C", "LFE", "SL", "SR"),
        outputs=("Out L", "Out R"),
        matrix=((1.0, 0.0, 0.707, 0.0, 0.707, 0.0), (0.0, 1.0, 0.707, 0.0, 0.0, 0.707)),
        formula=("Out L = FL + C * 0.707 + SL * 0.707", "Out R = FR + C * 0.707 + SR * 0.707"),
    ),
)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for diagram in DIAGRAMS:
        (OUT_DIR / diagram.filename).write_text(render(diagram), encoding="utf-8")
        print(f"wrote {OUT_DIR / diagram.filename}")


if __name__ == "__main__":
    main()
