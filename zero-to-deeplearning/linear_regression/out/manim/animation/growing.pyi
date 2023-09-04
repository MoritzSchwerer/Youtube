import numpy as np
from ..animation.transform import Transform
from ..mobject.mobject import Mobject
from _typeshed import Incomplete
from manim.mobject.geometry.line import Arrow

class GrowFromPoint(Transform):
    point: Incomplete
    point_color: Incomplete
    def __init__(self, mobject: Mobject, point: np.ndarray, point_color: str = ..., **kwargs) -> None: ...
    def create_target(self) -> Mobject: ...
    def create_starting_mobject(self) -> Mobject: ...

class GrowFromCenter(GrowFromPoint):
    def __init__(self, mobject: Mobject, point_color: str = ..., **kwargs) -> None: ...

class GrowFromEdge(GrowFromPoint):
    def __init__(self, mobject: Mobject, edge: np.ndarray, point_color: str = ..., **kwargs) -> None: ...

class GrowArrow(GrowFromPoint):
    def __init__(self, arrow: Arrow, point_color: str = ..., **kwargs) -> None: ...
    def create_starting_mobject(self) -> Mobject: ...

class SpinInFromNothing(GrowFromCenter):
    angle: Incomplete
    def __init__(self, mobject: Mobject, angle: float = ..., point_color: str = ..., **kwargs) -> None: ...
