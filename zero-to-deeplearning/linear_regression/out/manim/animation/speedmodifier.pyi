from ..animation.animation import Animation as Animation, Wait as Wait, prepare_animation as prepare_animation
from ..animation.composition import AnimationGroup as AnimationGroup
from ..mobject.mobject import Mobject as Mobject, Updater as Updater, _AnimationBuilder
from ..scene.scene import Scene as Scene
from _typeshed import Incomplete
from manim.utils.simple_functions import get_parameters as get_parameters
from typing import Callable

class ChangeSpeed(Animation):
    dt: int
    is_changing_dt: bool
    anim: Incomplete
    t: int
    affects_speed_updaters: Incomplete
    rate_func: Incomplete
    speed_modifier: Incomplete
    f_inv_1: Incomplete
    speedinfo: Incomplete
    functions: Incomplete
    conditions: Incomplete
    def __init__(self, anim: Animation | _AnimationBuilder, speedinfo: dict[float, float], rate_func: Callable[[float], float] | None = ..., affects_speed_updaters: bool = ..., **kwargs) -> None: ...
    def setup(self, anim): ...
    def get_scaled_total_time(self) -> float: ...
    @classmethod
    def add_updater(cls, mobject: Mobject, update_function: Updater, index: int | None = ..., call_updater: bool = ...): ...
    def interpolate(self, alpha: float) -> None: ...
    def update_mobjects(self, dt: float) -> None: ...
    def finish(self) -> None: ...
    def begin(self) -> None: ...
    def clean_up_from_scene(self, scene: Scene) -> None: ...
