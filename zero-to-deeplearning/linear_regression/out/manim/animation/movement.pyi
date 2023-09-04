import numpy as np
from ..animation.animation import Animation
from ..mobject.mobject import Mobject, VMobject
from _typeshed import Incomplete
from typing import Any, Callable

class Homotopy(Animation):
    homotopy: Incomplete
    apply_function_kwargs: Incomplete
    def __init__(self, homotopy: Callable[[float, float, float, float], tuple[float, float, float]], mobject: Mobject, run_time: float = ..., apply_function_kwargs: dict[str, Any] | None = ..., **kwargs) -> None: ...
    def function_at_time_t(self, t: float) -> tuple[float, float, float]: ...
    def interpolate_submobject(self, submobject: Mobject, starting_submobject: Mobject, alpha: float) -> None: ...

class SmoothedVectorizedHomotopy(Homotopy):
    def interpolate_submobject(self, submobject: Mobject, starting_submobject: Mobject, alpha: float) -> None: ...

class ComplexHomotopy(Homotopy):
    def __init__(self, complex_homotopy: Callable[[complex], float], mobject: Mobject, **kwargs) -> None: ...

class PhaseFlow(Animation):
    virtual_time: Incomplete
    function: Incomplete
    def __init__(self, function: Callable[[np.ndarray], np.ndarray], mobject: Mobject, virtual_time: float = ..., suspend_mobject_updating: bool = ..., rate_func: Callable[[float], float] = ..., **kwargs) -> None: ...
    last_alpha: Incomplete
    def interpolate_mobject(self, alpha: float) -> None: ...

class MoveAlongPath(Animation):
    path: Incomplete
    def __init__(self, mobject: Mobject, path: VMobject, suspend_mobject_updating: bool | None = ..., **kwargs) -> None: ...
    def interpolate_mobject(self, alpha: float) -> None: ...
