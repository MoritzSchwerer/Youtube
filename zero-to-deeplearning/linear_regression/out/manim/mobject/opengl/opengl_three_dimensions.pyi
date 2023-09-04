from _typeshed import Incomplete
from manim.mobject.opengl.opengl_surface import OpenGLSurface as OpenGLSurface
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVGroup as OpenGLVGroup, OpenGLVMobject as OpenGLVMobject

class OpenGLSurfaceMesh(OpenGLVGroup):
    uv_surface: Incomplete
    resolution: Incomplete
    normal_nudge: Incomplete
    def __init__(self, uv_surface, resolution: Incomplete | None = ..., stroke_width: int = ..., normal_nudge: float = ..., depth_test: bool = ..., flat_stroke: bool = ..., **kwargs) -> None: ...
    def init_points(self) -> None: ...
