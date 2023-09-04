from ..animation.animation import Animation
from ..mobject.mobject import Group, Mobject
from ..mobject.types.vectorized_mobject import VGroup
from ..scene.scene import Scene
from _typeshed import Incomplete
from manim.mobject.opengl.opengl_mobject import OpenGLGroup
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVGroup
from typing import Callable, Sequence

class AnimationGroup(Animation):
    animations: Incomplete
    rate_func: Incomplete
    group: Incomplete
    run_time: Incomplete
    def __init__(self, *animations: Animation, group: Group | VGroup | OpenGLGroup | OpenGLVGroup = ..., run_time: float | None = ..., rate_func: Callable[[float], float] = ..., lag_ratio: float = ..., **kwargs) -> None: ...
    def get_all_mobjects(self) -> Sequence[Mobject]: ...
    def begin(self) -> None: ...
    def finish(self) -> None: ...
    def clean_up_from_scene(self, scene: Scene) -> None: ...
    def update_mobjects(self, dt: float) -> None: ...
    max_end_time: Incomplete
    def init_run_time(self, run_time) -> float: ...
    anims_with_timings: Incomplete
    def build_animations_with_timings(self) -> None: ...
    def interpolate(self, alpha: float) -> None: ...

class Succession(AnimationGroup):
    def __init__(self, *animations: Animation, lag_ratio: float = ..., **kwargs) -> None: ...
    def begin(self) -> None: ...
    def finish(self) -> None: ...
    def update_mobjects(self, dt: float) -> None: ...
    active_index: Incomplete
    active_animation: Incomplete
    active_start_time: Incomplete
    active_end_time: Incomplete
    def update_active_animation(self, index: int) -> None: ...
    def next_animation(self) -> None: ...
    def interpolate(self, alpha: float) -> None: ...

class LaggedStart(AnimationGroup):
    def __init__(self, *animations: Animation, lag_ratio: float = ..., **kwargs) -> None: ...

class LaggedStartMap(LaggedStart):
    def __init__(self, AnimationClass: Callable[..., Animation], mobject: Mobject, arg_creator: Callable[[Mobject], str] = ..., run_time: float = ..., **kwargs) -> None: ...
