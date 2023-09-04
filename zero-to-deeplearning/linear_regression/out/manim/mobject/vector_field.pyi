import numpy as np
from ..animation.composition import AnimationGroup
from ..animation.indication import ShowPassingFlash
from ..mobject.mobject import Mobject
from ..mobject.types.vectorized_mobject import VGroup
from PIL import Image
from _typeshed import Incomplete
from colour import Color
from manim.mobject.graphing.coordinate_systems import CoordinateSystem
from typing import Callable, Iterable, Sequence

class VectorField(VGroup):
    func: Incomplete
    single_color: bool
    color_scheme: Incomplete
    rgbs: Incomplete
    pos_to_rgb: Incomplete
    pos_to_color: Incomplete
    color: Incomplete
    submob_movement_updater: Incomplete
    def __init__(self, func: Callable[[np.ndarray], np.ndarray], color: Color | None = ..., color_scheme: Callable[[np.ndarray], float] | None = ..., min_color_scheme_value: float = ..., max_color_scheme_value: float = ..., colors: Sequence[Color] = ..., **kwargs) -> None: ...
    @staticmethod
    def shift_func(func: Callable[[np.ndarray], np.ndarray], shift_vector: np.ndarray) -> Callable[[np.ndarray], np.ndarray]: ...
    @staticmethod
    def scale_func(func: Callable[[np.ndarray], np.ndarray], scalar: float) -> Callable[[np.ndarray], np.ndarray]: ...
    def fit_to_coordinate_system(self, coordinate_system: CoordinateSystem): ...
    def nudge(self, mob: Mobject, dt: float = ..., substeps: int = ..., pointwise: bool = ...) -> VectorField: ...
    def nudge_submobjects(self, dt: float = ..., substeps: int = ..., pointwise: bool = ...) -> VectorField: ...
    def get_nudge_updater(self, speed: float = ..., pointwise: bool = ...) -> Callable[[Mobject, float], Mobject]: ...
    def start_submobject_movement(self, speed: float = ..., pointwise: bool = ...) -> VectorField: ...
    def stop_submobject_movement(self) -> VectorField: ...
    def get_colored_background_image(self, sampling_rate: int = ...) -> Image.Image: ...
    def get_vectorized_rgba_gradient_function(self, start: float, end: float, colors: Iterable): ...

class ArrowVectorField(VectorField):
    x_range: Incomplete
    y_range: Incomplete
    ranges: Incomplete
    z_range: Incomplete
    length_func: Incomplete
    opacity: Incomplete
    vector_config: Incomplete
    func: Incomplete
    def __init__(self, func: Callable[[np.ndarray], np.ndarray], color: Color | None = ..., color_scheme: Callable[[np.ndarray], float] | None = ..., min_color_scheme_value: float = ..., max_color_scheme_value: float = ..., colors: Sequence[Color] = ..., x_range: Sequence[float] = ..., y_range: Sequence[float] = ..., z_range: Sequence[float] = ..., three_dimensions: bool = ..., length_func: Callable[[float], float] = ..., opacity: float = ..., vector_config: dict | None = ..., **kwargs) -> None: ...
    def get_vector(self, point: np.ndarray): ...

class StreamLines(VectorField):
    x_range: Incomplete
    y_range: Incomplete
    ranges: Incomplete
    z_range: Incomplete
    noise_factor: Incomplete
    n_repeats: Incomplete
    virtual_time: Incomplete
    max_anchors_per_line: Incomplete
    padding: Incomplete
    stroke_width: Incomplete
    background_img: Incomplete
    values_to_rgbas: Incomplete
    stream_lines: Incomplete
    def __init__(self, func: Callable[[np.ndarray], np.ndarray], color: Color | None = ..., color_scheme: Callable[[np.ndarray], float] | None = ..., min_color_scheme_value: float = ..., max_color_scheme_value: float = ..., colors: Sequence[Color] = ..., x_range: Sequence[float] = ..., y_range: Sequence[float] = ..., z_range: Sequence[float] = ..., three_dimensions: bool = ..., noise_factor: float | None = ..., n_repeats: int = ..., dt: float = ..., virtual_time: int = ..., max_anchors_per_line: int = ..., padding: int = ..., stroke_width: int = ..., opacity: int = ..., **kwargs) -> None: ...
    def create(self, lag_ratio: float | None = ..., run_time: Callable[[float], float] | None = ..., **kwargs) -> AnimationGroup: ...
    flow_animation: Incomplete
    flow_speed: Incomplete
    time_width: Incomplete
    def start_animation(self, warm_up: bool = ..., flow_speed: float = ..., time_width: float = ..., rate_func: Callable[[float], float] = ..., line_animation_class: type[ShowPassingFlash] = ..., **kwargs) -> None: ...
    def end_animation(self) -> AnimationGroup: ...
