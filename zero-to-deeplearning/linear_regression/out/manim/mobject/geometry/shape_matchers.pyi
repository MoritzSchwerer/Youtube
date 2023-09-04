from manim.constants import *
from _typeshed import Incomplete
from manim.mobject.geometry.line import Line
from manim.mobject.geometry.polygram import RoundedRectangle
from manim.mobject.mobject import Mobject
from manim.mobject.types.vectorized_mobject import VGroup
from manim.utils.color import Color, Colors

class SurroundingRectangle(RoundedRectangle):
    buff: Incomplete
    def __init__(self, mobject, color=..., buff=..., corner_radius: float = ..., **kwargs) -> None: ...

class BackgroundRectangle(SurroundingRectangle):
    original_fill_opacity: Incomplete
    def __init__(self, mobject, color: Colors | None = ..., stroke_width: float = ..., stroke_opacity: float = ..., fill_opacity: float = ..., buff: float = ..., **kwargs) -> None: ...
    def pointwise_become_partial(self, mobject, a, b): ...
    def set_style(self, fill_opacity, **kwargs): ...
    def get_fill_color(self): ...

class Cross(VGroup):
    def __init__(self, mobject: Mobject | None = ..., stroke_color: Color = ..., stroke_width: float = ..., scale_factor: float = ..., **kwargs) -> None: ...

class Underline(Line):
    def __init__(self, mobject, buff=..., **kwargs) -> None: ...
