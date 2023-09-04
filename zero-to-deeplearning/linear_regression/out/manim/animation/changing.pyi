from _typeshed import Incomplete
from colour import Color
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.types.vectorized_mobject import VGroup, VMobject
from typing import Callable

class AnimatedBoundary(VGroup):
    colors: Incomplete
    max_stroke_width: Incomplete
    cycle_rate: Incomplete
    back_and_forth: Incomplete
    draw_rate_func: Incomplete
    fade_rate_func: Incomplete
    vmobject: Incomplete
    boundary_copies: Incomplete
    total_time: int
    def __init__(self, vmobject, colors=..., max_stroke_width: int = ..., cycle_rate: float = ..., back_and_forth: bool = ..., draw_rate_func=..., fade_rate_func=..., **kwargs) -> None: ...
    def update_boundary_copies(self, dt) -> None: ...
    def full_family_become_partial(self, mob1, mob2, a, b): ...

class TracedPath(VMobject, metaclass=ConvertToOpenGL):
    traced_point_func: Incomplete
    dissipating_time: Incomplete
    time: Incomplete
    def __init__(self, traced_point_func: Callable, stroke_width: float = ..., stroke_color: Color = ..., dissipating_time: float | None = ..., **kwargs) -> None: ...
    def update_path(self, mob, dt) -> None: ...
