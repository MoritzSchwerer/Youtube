from manim.constants import *
import os
from _typeshed import Incomplete
from manim.mobject.types.vectorized_mobject import VGroup

class Code(VGroup):
    styles_list: Incomplete
    background_stroke_color: Incomplete
    background_stroke_width: Incomplete
    tab_width: Incomplete
    line_spacing: Incomplete
    font: Incomplete
    font_size: Incomplete
    margin: Incomplete
    indentation_chars: Incomplete
    background: Incomplete
    corner_radius: Incomplete
    insert_line_no: Incomplete
    line_no_from: Incomplete
    line_no_buff: Incomplete
    style: Incomplete
    language: Incomplete
    generate_html_file: Incomplete
    file_path: Incomplete
    file_name: Incomplete
    code_string: Incomplete
    background_color: Incomplete
    code: Incomplete
    line_numbers: Incomplete
    background_mobject: Incomplete
    def __init__(self, file_name: str | os.PathLike | None = ..., code: str | None = ..., tab_width: int = ..., line_spacing: float = ..., font_size: float = ..., font: str = ..., stroke_width: float = ..., margin: float = ..., indentation_chars: str = ..., background: str = ..., background_stroke_width: float = ..., background_stroke_color: str = ..., corner_radius: float = ..., insert_line_no: bool = ..., line_no_from: int = ..., line_no_buff: float = ..., style: str = ..., language: str | None = ..., generate_html_file: bool = ..., **kwargs) -> None: ...
