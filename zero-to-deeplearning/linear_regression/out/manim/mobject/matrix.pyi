from ..constants import *
from ..mobject.types.vectorized_mobject import VMobject
from _typeshed import Incomplete
from manim.mobject.mobject import Mobject
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.text.tex_mobject import MathTex
from typing import Iterable, Sequence

def matrix_to_tex_string(matrix): ...
def matrix_to_mobject(matrix): ...

class Matrix(VMobject, metaclass=ConvertToOpenGL):
    v_buff: Incomplete
    h_buff: Incomplete
    bracket_h_buff: Incomplete
    bracket_v_buff: Incomplete
    add_background_rectangles_to_entries: Incomplete
    include_background_rectangle: Incomplete
    element_to_mobject: Incomplete
    element_to_mobject_config: Incomplete
    element_alignment_corner: Incomplete
    left_bracket: Incomplete
    right_bracket: Incomplete
    stretch_brackets: Incomplete
    elements: Incomplete
    mob_matrix: Incomplete
    def __init__(self, matrix: Iterable, v_buff: float = ..., h_buff: float = ..., bracket_h_buff: float = ..., bracket_v_buff: float = ..., add_background_rectangles_to_entries: bool = ..., include_background_rectangle: bool = ..., element_to_mobject: type[MathTex] = ..., element_to_mobject_config: dict = ..., element_alignment_corner: Sequence[float] = ..., left_bracket: str = ..., right_bracket: str = ..., stretch_brackets: bool = ..., bracket_config: dict = ..., **kwargs) -> None: ...
    def get_columns(self): ...
    def set_column_colors(self, *colors: str): ...
    def get_rows(self): ...
    def set_row_colors(self, *colors: str): ...
    def add_background_to_entries(self): ...
    def get_mob_matrix(self): ...
    def get_entries(self): ...
    def get_brackets(self): ...

class DecimalMatrix(Matrix):
    def __init__(self, matrix: Iterable, element_to_mobject: Mobject = ..., element_to_mobject_config: dict[str, Mobject] = ..., **kwargs) -> None: ...

class IntegerMatrix(Matrix):
    def __init__(self, matrix: Iterable, element_to_mobject: Mobject = ..., **kwargs) -> None: ...

class MobjectMatrix(Matrix):
    def __init__(self, matrix, element_to_mobject=..., **kwargs) -> None: ...

def get_det_text(matrix: Matrix, determinant: int | str | None = ..., background_rect: bool = ..., initial_scale_factor: float = ...): ...
