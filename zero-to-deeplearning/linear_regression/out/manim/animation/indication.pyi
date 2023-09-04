from ..constants import *
import numpy as np
from ..animation.animation import Animation
from ..animation.composition import AnimationGroup, Succession
from ..animation.creation import ShowPartial
from ..animation.movement import Homotopy
from ..animation.transform import Transform
from ..mobject.mobject import Mobject
from ..mobject.types.vectorized_mobject import VGroup, VMobject
from _typeshed import Incomplete
from colour import Color
from manim.mobject.geometry.arc import Dot
from typing import Callable, Iterable, Optional, Type, Union

class FocusOn(Transform):
    focus_point: Incomplete
    color: Incomplete
    opacity: Incomplete
    def __init__(self, focus_point: Union[np.ndarray, Mobject], opacity: float = ..., color: str = ..., run_time: float = ..., **kwargs) -> None: ...
    def create_target(self) -> Dot: ...

class Indicate(Transform):
    color: Incomplete
    scale_factor: Incomplete
    def __init__(self, mobject: Mobject, scale_factor: float = ..., color: str = ..., rate_func: Callable[[float, Optional[float]], np.ndarray] = ..., **kwargs) -> None: ...
    def create_target(self) -> Mobject: ...

class Flash(AnimationGroup):
    point: Incomplete
    color: Incomplete
    line_length: Incomplete
    num_lines: Incomplete
    flash_radius: Incomplete
    line_stroke_width: Incomplete
    run_time: Incomplete
    time_width: Incomplete
    animation_config: Incomplete
    lines: Incomplete
    def __init__(self, point: Union[np.ndarray, Mobject], line_length: float = ..., num_lines: int = ..., flash_radius: float = ..., line_stroke_width: int = ..., color: str = ..., time_width: float = ..., run_time: float = ..., **kwargs) -> None: ...
    def create_lines(self) -> VGroup: ...
    def create_line_anims(self) -> Iterable['ShowPassingFlash']: ...

class ShowPassingFlash(ShowPartial):
    time_width: Incomplete
    def __init__(self, mobject: VMobject, time_width: float = ..., **kwargs) -> None: ...
    def clean_up_from_scene(self, scene: Scene) -> None: ...

class ShowPassingFlashWithThinningStrokeWidth(AnimationGroup):
    n_segments: Incomplete
    time_width: Incomplete
    remover: Incomplete
    def __init__(self, vmobject, n_segments: int = ..., time_width: float = ..., remover: bool = ..., **kwargs) -> None: ...

class ShowCreationThenFadeOut(Succession):
    def __init__(self, mobject: Mobject, remover: bool = ..., **kwargs) -> None: ...

class ApplyWave(Homotopy):
    def __init__(self, mobject: Mobject, direction: np.ndarray = ..., amplitude: float = ..., wave_func: Callable[[float], float] = ..., time_width: float = ..., ripples: int = ..., run_time: float = ..., **kwargs) -> None: ...

class Wiggle(Animation):
    scale_value: Incomplete
    rotation_angle: Incomplete
    n_wiggles: Incomplete
    scale_about_point: Incomplete
    rotate_about_point: Incomplete
    def __init__(self, mobject: Mobject, scale_value: float = ..., rotation_angle: float = ..., n_wiggles: int = ..., scale_about_point: Optional[np.ndarray] = ..., rotate_about_point: Optional[np.ndarray] = ..., run_time: float = ..., **kwargs) -> None: ...
    def get_scale_about_point(self) -> np.ndarray: ...
    def get_rotate_about_point(self) -> np.ndarray: ...
    def interpolate_submobject(self, submobject: Mobject, starting_submobject: Mobject, alpha: float) -> None: ...

class Circumscribe(Succession):
    def __init__(self, mobject: Mobject, shape: Type = ..., fade_in: bool = ..., fade_out: bool = ..., time_width: float = ..., buff: float = ..., color: Color = ..., run_time: int = ..., stroke_width=..., **kwargs) -> None: ...
