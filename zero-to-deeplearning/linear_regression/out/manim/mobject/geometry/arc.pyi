from manim.constants import *
from manim.utils.color import *
import numpy as np
from _typeshed import Incomplete
from colour import Color
from manim.mobject.mobject import Mobject
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.text.tex_mobject import SingleStringMathTex, Tex
from manim.mobject.text.text_mobject import Text
from manim.mobject.types.vectorized_mobject import VMobject
from typing import Sequence

class TipableVMobject(VMobject, metaclass=ConvertToOpenGL):
    tip_length: Incomplete
    normal_vector: Incomplete
    tip_style: Incomplete
    def __init__(self, tip_length=..., normal_vector=..., tip_style=..., **kwargs) -> None: ...
    def add_tip(self, tip: Incomplete | None = ..., tip_shape: Incomplete | None = ..., tip_length: Incomplete | None = ..., tip_width: Incomplete | None = ..., at_start: bool = ...): ...
    def create_tip(self, tip_shape: Incomplete | None = ..., tip_length: Incomplete | None = ..., tip_width: Incomplete | None = ..., at_start: bool = ...): ...
    def get_unpositioned_tip(self, tip_shape: Incomplete | None = ..., tip_length: Incomplete | None = ..., tip_width: Incomplete | None = ...): ...
    def position_tip(self, tip, at_start: bool = ...): ...
    def reset_endpoints_based_on_tip(self, tip, at_start): ...
    start_tip: Incomplete
    tip: Incomplete
    def asign_tip_attr(self, tip, at_start): ...
    def has_tip(self): ...
    def has_start_tip(self): ...
    def pop_tips(self): ...
    def get_tips(self): ...
    def get_tip(self): ...
    def get_default_tip_length(self): ...
    def get_first_handle(self): ...
    def get_last_handle(self): ...
    def get_end(self): ...
    def get_start(self): ...
    def get_length(self): ...

class Arc(TipableVMobject):
    radius: Incomplete
    num_components: Incomplete
    arc_center: Incomplete
    start_angle: Incomplete
    angle: Incomplete
    def __init__(self, radius: float = ..., start_angle: int = ..., angle=..., num_components: int = ..., arc_center=..., **kwargs) -> None: ...
    def generate_points(self) -> None: ...
    def init_points(self) -> None: ...
    def get_arc_center(self, warning: bool = ...): ...
    def move_arc_center_to(self, point): ...
    def stop_angle(self): ...

class ArcBetweenPoints(Arc):
    radius: Incomplete
    def __init__(self, start, end, angle=..., radius: Incomplete | None = ..., **kwargs) -> None: ...

class CurvedArrow(ArcBetweenPoints):
    def __init__(self, start_point, end_point, **kwargs) -> None: ...

class CurvedDoubleArrow(CurvedArrow):
    def __init__(self, start_point, end_point, **kwargs) -> None: ...

class Circle(Arc):
    def __init__(self, radius: float | None = ..., color: Color | str = ..., **kwargs) -> None: ...
    width: Incomplete
    def surround(self, mobject: Mobject, dim_to_match: int = ..., stretch: bool = ..., buffer_factor: float = ...): ...
    def point_at_angle(self, angle: float): ...
    @staticmethod
    def from_three_points(p1: Sequence[float], p2: Sequence[float], p3: Sequence[float], **kwargs): ...

class Dot(Circle):
    def __init__(self, point: list | np.ndarray = ..., radius: float = ..., stroke_width: float = ..., fill_opacity: float = ..., color: Color | str = ..., **kwargs) -> None: ...

class AnnotationDot(Dot):
    def __init__(self, radius: float = ..., stroke_width: int = ..., stroke_color=..., fill_color=..., **kwargs) -> None: ...

class LabeledDot(Dot):
    def __init__(self, label: str | SingleStringMathTex | Text | Tex, radius: float | None = ..., **kwargs) -> None: ...

class Ellipse(Circle):
    def __init__(self, width: float = ..., height: float = ..., **kwargs) -> None: ...

class AnnularSector(Arc):
    inner_radius: Incomplete
    outer_radius: Incomplete
    def __init__(self, inner_radius: int = ..., outer_radius: int = ..., angle=..., start_angle: int = ..., fill_opacity: int = ..., stroke_width: int = ..., color=..., **kwargs) -> None: ...
    def generate_points(self) -> None: ...
    init_points = generate_points

class Sector(AnnularSector):
    def __init__(self, outer_radius: int = ..., inner_radius: int = ..., **kwargs) -> None: ...

class Annulus(Circle):
    mark_paths_closed: Incomplete
    inner_radius: Incomplete
    outer_radius: Incomplete
    def __init__(self, inner_radius: float | None = ..., outer_radius: float | None = ..., fill_opacity: int = ..., stroke_width: int = ..., color=..., mark_paths_closed: bool = ..., **kwargs) -> None: ...
    radius: Incomplete
    def generate_points(self) -> None: ...
    init_points = generate_points

class CubicBezier(VMobject, metaclass=ConvertToOpenGL):
    def __init__(self, start_anchor, start_handle, end_handle, end_anchor, **kwargs) -> None: ...

class ArcPolygon(VMobject, metaclass=ConvertToOpenGL):
    arcs: Incomplete
    def __init__(self, *vertices: list | np.ndarray, angle: float = ..., radius: float | None = ..., arc_config: list[dict] | None = ..., **kwargs) -> None: ...

class ArcPolygonFromArcs(VMobject, metaclass=ConvertToOpenGL):
    arcs: Incomplete
    def __init__(self, *arcs: Arc | ArcBetweenPoints, **kwargs) -> None: ...
