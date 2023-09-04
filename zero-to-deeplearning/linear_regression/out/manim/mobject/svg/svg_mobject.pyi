import os
import svgelements as se
from ..geometry.arc import Circle
from ..geometry.line import Line
from ..geometry.polygram import Polygon, Rectangle
from ..opengl.opengl_compatibility import ConvertToOpenGL
from ..types.vectorized_mobject import VMobject
from _typeshed import Incomplete
from pathlib import Path
from xml.etree import ElementTree as ET

class SVGMobject(VMobject, metaclass=ConvertToOpenGL):
    file_name: Incomplete
    should_center: Incomplete
    svg_height: Incomplete
    svg_width: Incomplete
    color: Incomplete
    opacity: Incomplete
    fill_color: Incomplete
    fill_opacity: Incomplete
    stroke_color: Incomplete
    stroke_opacity: Incomplete
    stroke_width: Incomplete
    svg_default: Incomplete
    path_string_config: Incomplete
    def __init__(self, file_name: str | os.PathLike | None = ..., should_center: bool = ..., height: float | None = ..., width: float | None = ..., color: str | None = ..., opacity: float | None = ..., fill_color: str | None = ..., fill_opacity: float | None = ..., stroke_color: str | None = ..., stroke_opacity: float | None = ..., stroke_width: float | None = ..., svg_default: dict | None = ..., path_string_config: dict | None = ..., **kwargs) -> None: ...
    def init_svg_mobject(self) -> None: ...
    @property
    def hash_seed(self) -> tuple: ...
    def generate_mobject(self) -> None: ...
    def get_file_path(self) -> Path: ...
    def modify_xml_tree(self, element_tree: ET.ElementTree) -> ET.ElementTree: ...
    def generate_config_style_dict(self) -> dict[str, str]: ...
    def get_mobjects_from(self, svg: se.SVG) -> list[VMobject]: ...
    @staticmethod
    def handle_transform(mob: VMobject, matrix: se.Matrix) -> VMobject: ...
    @staticmethod
    def apply_style_to_mobject(mob: VMobject, shape: se.GraphicObject) -> VMobject: ...
    def path_to_mobject(self, path: se.Path) -> VMobjectFromSVGPath: ...
    @staticmethod
    def line_to_mobject(line: se.Line) -> Line: ...
    @staticmethod
    def rect_to_mobject(rect: se.Rect) -> Rectangle: ...
    @staticmethod
    def ellipse_to_mobject(ellipse: se.Ellipse | se.Circle) -> Circle: ...
    @staticmethod
    def polygon_to_mobject(polygon: se.Polygon) -> Polygon: ...
    def polyline_to_mobject(self, polyline: se.Polyline) -> VMobject: ...
    @staticmethod
    def text_to_mobject(text: se.Text): ...
    def move_into_position(self) -> None: ...

class VMobjectFromSVGPath(VMobject, metaclass=ConvertToOpenGL):
    path_obj: Incomplete
    long_lines: Incomplete
    should_subdivide_sharp_curves: Incomplete
    should_remove_null_curves: Incomplete
    def __init__(self, path_obj: se.Path, long_lines: bool = ..., should_subdivide_sharp_curves: bool = ..., should_remove_null_curves: bool = ..., **kwargs) -> None: ...
    def init_points(self) -> None: ...
    generate_points = init_points
    def handle_commands(self) -> None: ...
