from manim.constants import *
from _typeshed import Incomplete
from manim.mobject.geometry.arc import Circle
from manim.mobject.geometry.polygram import Square, Triangle
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.types.vectorized_mobject import VMobject

class ArrowTip(VMobject, metaclass=ConvertToOpenGL):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def base(self): ...
    @property
    def tip_point(self): ...
    @property
    def vector(self): ...
    @property
    def tip_angle(self): ...
    @property
    def length(self): ...

class ArrowTriangleTip(ArrowTip, Triangle):
    width: Incomplete
    def __init__(self, fill_opacity: int = ..., stroke_width: int = ..., length=..., width=..., start_angle=..., **kwargs) -> None: ...

class ArrowTriangleFilledTip(ArrowTriangleTip):
    def __init__(self, fill_opacity: int = ..., stroke_width: int = ..., **kwargs) -> None: ...

class ArrowCircleTip(ArrowTip, Circle):
    start_angle: Incomplete
    width: Incomplete
    def __init__(self, fill_opacity: int = ..., stroke_width: int = ..., length=..., start_angle=..., **kwargs) -> None: ...

class ArrowCircleFilledTip(ArrowCircleTip):
    def __init__(self, fill_opacity: int = ..., stroke_width: int = ..., **kwargs) -> None: ...

class ArrowSquareTip(ArrowTip, Square):
    start_angle: Incomplete
    width: Incomplete
    def __init__(self, fill_opacity: int = ..., stroke_width: int = ..., length=..., start_angle=..., **kwargs) -> None: ...

class ArrowSquareFilledTip(ArrowSquareTip):
    def __init__(self, fill_opacity: int = ..., stroke_width: int = ..., **kwargs) -> None: ...
