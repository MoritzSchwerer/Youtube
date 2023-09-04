from _typeshed import Incomplete
from manim.mobject.graphing.scale import _ScaleBase
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.types.vectorized_mobject import VMobject
from typing import Callable, Iterable, Sequence

class ParametricFunction(VMobject, metaclass=ConvertToOpenGL):
    function: Incomplete
    scaling: Incomplete
    dt: Incomplete
    discontinuities: Incomplete
    use_smoothing: Incomplete
    use_vectorized: Incomplete
    def __init__(self, function: Callable[[float, float], float], t_range: Sequence[float] | None = ..., scaling: _ScaleBase = ..., dt: float = ..., discontinuities: Iterable[float] | None = ..., use_smoothing: bool = ..., use_vectorized: bool = ..., **kwargs) -> None: ...
    def get_function(self): ...
    def get_point_from_function(self, t): ...
    def generate_points(self): ...
    init_points = generate_points

class FunctionGraph(ParametricFunction):
    x_range: Incomplete
    parametric_function: Incomplete
    function: Incomplete
    def __init__(self, function, x_range: Incomplete | None = ..., color=..., **kwargs) -> None: ...
    def get_function(self): ...
    def get_point_from_function(self, x): ...

class ImplicitFunction(VMobject, metaclass=ConvertToOpenGL):
    function: Incomplete
    min_depth: Incomplete
    max_quads: Incomplete
    use_smoothing: Incomplete
    x_range: Incomplete
    y_range: Incomplete
    def __init__(self, func: Callable[[float, float], float], x_range: Sequence[float] | None = ..., y_range: Sequence[float] | None = ..., min_depth: int = ..., max_quads: int = ..., use_smoothing: bool = ..., **kwargs) -> None: ...
    def generate_points(self): ...
    init_points = generate_points
