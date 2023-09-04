import numpy as np
from ..animation.animation import Animation
from ..animation.transform import Transform
from ..mobject.mobject import Mobject
from _typeshed import Incomplete
from typing import Callable, Sequence

class Rotating(Animation):
    axis: Incomplete
    radians: Incomplete
    about_point: Incomplete
    about_edge: Incomplete
    def __init__(self, mobject: Mobject, axis: np.ndarray = ..., radians: np.ndarray = ..., about_point: np.ndarray | None = ..., about_edge: np.ndarray | None = ..., run_time: float = ..., rate_func: Callable[[float], float] = ..., **kwargs) -> None: ...
    def interpolate_mobject(self, alpha: float) -> None: ...

class Rotate(Transform):
    angle: Incomplete
    axis: Incomplete
    about_edge: Incomplete
    about_point: Incomplete
    def __init__(self, mobject: Mobject, angle: float = ..., axis: np.ndarray = ..., about_point: Sequence[float] | None = ..., about_edge: Sequence[float] | None = ..., **kwargs) -> None: ...
    def create_target(self) -> Mobject: ...
