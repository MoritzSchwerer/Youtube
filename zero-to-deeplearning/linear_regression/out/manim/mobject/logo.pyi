from ..animation.composition import AnimationGroup, Succession
from ..mobject.types.vectorized_mobject import VGroup
from _typeshed import Incomplete

class ManimBanner(VGroup):
    font_color: Incomplete
    scale_factor: int
    M: Incomplete
    circle: Incomplete
    square: Incomplete
    triangle: Incomplete
    shapes: Incomplete
    anim: Incomplete
    def __init__(self, dark_theme: bool = ...) -> None: ...
    def scale(self, scale_factor: float, **kwargs) -> ManimBanner: ...
    def create(self, run_time: float = ...) -> AnimationGroup: ...
    def expand(self, run_time: float = ..., direction: str = ...) -> Succession: ...
