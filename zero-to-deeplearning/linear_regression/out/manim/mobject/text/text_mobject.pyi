from manim.constants import *
from _typeshed import Incomplete
from colour import Color
from manim.mobject.svg.svg_mobject import SVGMobject
from manim.mobject.types.vectorized_mobject import VGroup
from pathlib import Path
from typing import Sequence

class Paragraph(VGroup):
    line_spacing: Incomplete
    alignment: Incomplete
    consider_spaces_as_chars: Incomplete
    lines_text: Incomplete
    chars: Incomplete
    lines: Incomplete
    lines_initial_positions: Incomplete
    def __init__(self, *text: Sequence[str], line_spacing: float = ..., alignment: Optional[str] = ..., **kwargs) -> None: ...

class Text(SVGMobject):
    line_spacing: Incomplete
    font: Incomplete
    slant: Incomplete
    weight: Incomplete
    gradient: Incomplete
    tab_width: Incomplete
    t2c: Incomplete
    t2f: Incomplete
    t2g: Incomplete
    t2s: Incomplete
    t2w: Incomplete
    original_text: Incomplete
    disable_ligatures: Incomplete
    text: Incomplete
    submobjects: Incomplete
    chars: Incomplete
    initial_height: Incomplete
    def __init__(self, text: str, fill_opacity: float = ..., stroke_width: float = ..., color: Color | str | None = ..., font_size: float = ..., line_spacing: float = ..., font: str = ..., slant: str = ..., weight: str = ..., t2c: dict[str, str] = ..., t2f: dict[str, str] = ..., t2g: dict[str, tuple] = ..., t2s: dict[str, str] = ..., t2w: dict[str, str] = ..., gradient: tuple = ..., tab_width: int = ..., height: float = ..., width: float = ..., should_center: bool = ..., disable_ligatures: bool = ..., **kwargs) -> None: ...
    @property
    def font_size(self): ...
    def init_colors(self, propagate_colors: bool = ...) -> None: ...

class MarkupText(SVGMobject):
    text: Incomplete
    line_spacing: Incomplete
    font: Incomplete
    slant: Incomplete
    weight: Incomplete
    gradient: Incomplete
    tab_width: Incomplete
    justify: Incomplete
    original_text: Incomplete
    disable_ligatures: Incomplete
    chars: Incomplete
    initial_height: Incomplete
    def __init__(self, text: str, fill_opacity: float = ..., stroke_width: float = ..., color: Color | None = ..., font_size: float = ..., line_spacing: int = ..., font: str = ..., slant: str = ..., weight: str = ..., justify: bool = ..., gradient: tuple = ..., tab_width: int = ..., height: int = ..., width: int = ..., should_center: bool = ..., disable_ligatures: bool = ..., **kwargs) -> None: ...
    @property
    def font_size(self): ...

def register_font(font_file: str | Path): ...
