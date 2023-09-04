from _typeshed import Incomplete
from manim.mobject.opengl.opengl_point_cloud_mobject import OpenGLPMobject

class DotCloud(OpenGLPMobject):
    radius: Incomplete
    epsilon: Incomplete
    def __init__(self, color=..., stroke_width: float = ..., radius: float = ..., density: int = ..., **kwargs) -> None: ...
    points: Incomplete
    def init_points(self) -> None: ...
    def make_3d(self, gloss: float = ..., shadow: float = ...): ...

class TrueDot(DotCloud):
    radius: Incomplete
    def __init__(self, center=..., stroke_width: float = ..., **kwargs) -> None: ...
