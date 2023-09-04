from _typeshed import Incomplete
from manim.mobject.geometry.polygram import Rectangle

class ScreenRectangle(Rectangle):
    def __init__(self, aspect_ratio=..., height: int = ..., **kwargs) -> None: ...
    @property
    def aspect_ratio(self): ...

class FullScreenRectangle(ScreenRectangle):
    height: Incomplete
    def __init__(self, **kwargs) -> None: ...
