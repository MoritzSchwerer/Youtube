from ...constants import *
from ...mobject.types.vectorized_mobject import VMobject
from ..svg.svg_mobject import VMobjectFromSVGPath
from _typeshed import Incomplete
from manim.mobject.geometry.arc import Arc
from manim.mobject.mobject import Mobject
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from typing import Sequence

class Brace(VMobjectFromSVGPath):
    buff: Incomplete
    def __init__(self, mobject: Mobject, direction: Sequence[float] | None = ..., buff: float = ..., sharpness: int = ..., stroke_width: int = ..., fill_opacity: float = ..., background_stroke_width: int = ..., background_stroke_color=..., **kwargs) -> None: ...
    def put_at_tip(self, mob, use_next_to: bool = ..., **kwargs): ...
    def get_text(self, *text, **kwargs): ...
    def get_tex(self, *tex, **kwargs): ...
    def get_tip(self): ...
    def get_direction(self): ...

class BraceLabel(VMobject, metaclass=ConvertToOpenGL):
    label_constructor: Incomplete
    brace_direction: Incomplete
    buff: Incomplete
    brace: Incomplete
    label: Incomplete
    def __init__(self, obj, text, brace_direction=..., label_constructor=..., font_size=..., buff: float = ..., **kwargs) -> None: ...
    def creation_anim(self, label_anim=..., brace_anim=...): ...
    def shift_brace(self, obj, **kwargs): ...
    def change_label(self, *text, **kwargs): ...
    def change_brace_label(self, obj, *text, **kwargs): ...

class BraceText(BraceLabel):
    def __init__(self, obj, text, label_constructor=..., **kwargs) -> None: ...

class BraceBetweenPoints(Brace):
    def __init__(self, point_1: Sequence[float] | None, point_2: Sequence[float] | None, direction: Sequence[float] | None = ..., **kwargs) -> None: ...

class ArcBrace(Brace):
    def __init__(self, arc: Arc = ..., direction: Sequence[float] = ..., **kwargs) -> None: ...
