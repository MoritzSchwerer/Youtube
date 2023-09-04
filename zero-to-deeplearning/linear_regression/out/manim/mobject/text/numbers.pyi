from manim.constants import *
from _typeshed import Incomplete
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.text.tex_mobject import MathTex, SingleStringMathTex, Tex
from manim.mobject.text.text_mobject import Text
from manim.mobject.types.vectorized_mobject import VMobject
from typing import Sequence

class DecimalNumber(VMobject, metaclass=ConvertToOpenGL):
    number: Incomplete
    num_decimal_places: Incomplete
    include_sign: Incomplete
    mob_class: Incomplete
    group_with_commas: Incomplete
    digit_buff_per_font_unit: Incomplete
    show_ellipsis: Incomplete
    unit: Incomplete
    include_background_rectangle: Incomplete
    edge_to_fix: Incomplete
    stroke_width: Incomplete
    fill_opacity: Incomplete
    initial_config: Incomplete
    def __init__(self, number: float = ..., num_decimal_places: int = ..., mob_class: VMobject = ..., include_sign: bool = ..., group_with_commas: bool = ..., digit_buff_per_font_unit: float = ..., show_ellipsis: bool = ..., unit: str | None = ..., include_background_rectangle: bool = ..., edge_to_fix: Sequence[float] = ..., font_size: float = ..., stroke_width: float = ..., fill_opacity: float = ..., **kwargs) -> None: ...
    @property
    def font_size(self): ...
    def set_value(self, number: float): ...
    def get_value(self): ...
    def increment_value(self, delta_t: int = ...) -> None: ...

class Integer(DecimalNumber):
    def __init__(self, number: int = ..., num_decimal_places: int = ..., **kwargs) -> None: ...
    def get_value(self): ...

class Variable(VMobject, metaclass=ConvertToOpenGL):
    label: Incomplete
    tracker: Incomplete
    value: Incomplete
    def __init__(self, var: float, label: str | Tex | MathTex | Text | SingleStringMathTex, var_type: DecimalNumber | Integer = ..., num_decimal_places: int = ..., **kwargs) -> None: ...
