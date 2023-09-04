from ..utils import opengl as opengl
from ..utils.space_ops import cross2d as cross2d, earclip_triangulation as earclip_triangulation
from .shader import Shader as Shader

def build_matrix_lists(mob): ...
def render_opengl_vectorized_mobject_fill(renderer, mobject) -> None: ...
def render_mobject_fills_with_matrix(renderer, model_matrix, mobjects) -> None: ...
def triangulate_mobject(mob): ...
def render_opengl_vectorized_mobject_stroke(renderer, mobject) -> None: ...
def render_mobject_strokes_with_matrix(renderer, model_matrix, mobjects) -> None: ...
