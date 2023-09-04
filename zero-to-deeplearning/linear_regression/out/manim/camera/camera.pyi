from ..constants import *
import cairo
import numpy as np
import pathlib
from ..mobject.mobject import Mobject
from ..mobject.types.image_mobject import AbstractImageMobject
from ..mobject.types.point_cloud_mobject import PMobject
from ..mobject.types.vectorized_mobject import VMobject
from PIL import Image
from _typeshed import Incomplete
from typing import Any, Callable, Iterable

class Camera:
    background_image: Incomplete
    frame_center: Incomplete
    image_mode: Incomplete
    n_channels: Incomplete
    pixel_array_dtype: Incomplete
    cairo_line_width_multiple: Incomplete
    use_z_index: Incomplete
    background: Incomplete
    pixel_height: Incomplete
    pixel_width: Incomplete
    frame_height: Incomplete
    frame_width: Incomplete
    frame_rate: Incomplete
    max_allowable_norm: Incomplete
    rgb_max_val: Incomplete
    pixel_array_to_cairo_context: Incomplete
    def __init__(self, background_image: str | None = ..., frame_center: np.ndarray = ..., image_mode: str = ..., n_channels: int = ..., pixel_array_dtype: str = ..., cairo_line_width_multiple: float = ..., use_z_index: bool = ..., background: np.ndarray | None = ..., pixel_height: int | None = ..., pixel_width: int | None = ..., frame_height: float | None = ..., frame_width: float | None = ..., frame_rate: float | None = ..., **kwargs) -> None: ...
    canvas: Incomplete
    def __deepcopy__(self, memo): ...
    @property
    def background_color(self): ...
    @property
    def background_opacity(self): ...
    display_funcs: Incomplete
    def type_or_raise(self, mobject: Mobject): ...
    def reset_pixel_shape(self, new_height: float, new_width: float): ...
    def resize_frame_shape(self, fixed_dimension: int = ...): ...
    def init_background(self) -> None: ...
    def get_image(self, pixel_array: np.ndarray | list | tuple | None = ...): ...
    def convert_pixel_array(self, pixel_array: np.ndarray | list | tuple, convert_from_floats: bool = ...): ...
    pixel_array: Incomplete
    def set_pixel_array(self, pixel_array: np.ndarray | list | tuple, convert_from_floats: bool = ...): ...
    def set_background(self, pixel_array: np.ndarray | list | tuple, convert_from_floats: bool = ...): ...
    def make_background_from_func(self, coords_to_colors_func: Callable[[np.ndarray], np.ndarray]): ...
    def set_background_from_func(self, coords_to_colors_func: Callable[[np.ndarray], np.ndarray]): ...
    def reset(self): ...
    def set_frame_to_background(self, background) -> None: ...
    def get_mobjects_to_display(self, mobjects: Iterable[Mobject], include_submobjects: bool = ..., excluded_mobjects: list | None = ...): ...
    def is_in_frame(self, mobject: Mobject): ...
    def capture_mobject(self, mobject: Mobject, **kwargs: Any): ...
    def capture_mobjects(self, mobjects: Iterable[Mobject], **kwargs): ...
    def get_cached_cairo_context(self, pixel_array: np.ndarray): ...
    def cache_cairo_context(self, pixel_array: np.ndarray, ctx: cairo.Context): ...
    def get_cairo_context(self, pixel_array: np.ndarray): ...
    def display_multiple_vectorized_mobjects(self, vmobjects: list, pixel_array: np.ndarray): ...
    def display_multiple_non_background_colored_vmobjects(self, vmobjects: list, pixel_array: np.ndarray): ...
    def display_vectorized(self, vmobject: VMobject, ctx: cairo.Context): ...
    def set_cairo_context_path(self, ctx: cairo.Context, vmobject: VMobject): ...
    def set_cairo_context_color(self, ctx: cairo.Context, rgbas: np.ndarray, vmobject: VMobject): ...
    def apply_fill(self, ctx: cairo.Context, vmobject: VMobject): ...
    def apply_stroke(self, ctx: cairo.Context, vmobject: VMobject, background: bool = ...): ...
    def get_stroke_rgbas(self, vmobject: VMobject, background: bool = ...): ...
    def get_fill_rgbas(self, vmobject: VMobject): ...
    def get_background_colored_vmobject_displayer(self): ...
    def display_multiple_background_colored_vmobjects(self, cvmobjects: list, pixel_array: np.ndarray): ...
    def display_multiple_point_cloud_mobjects(self, pmobjects: list, pixel_array: np.ndarray): ...
    def display_point_cloud(self, pmobject: PMobject, points: list, rgbas: np.ndarray, thickness: float, pixel_array: np.ndarray): ...
    def display_multiple_image_mobjects(self, image_mobjects: list, pixel_array: np.ndarray): ...
    def display_image_mobject(self, image_mobject: AbstractImageMobject, pixel_array: np.ndarray): ...
    def overlay_rgba_array(self, pixel_array: np.ndarray, new_array: np.ndarray): ...
    def overlay_PIL_image(self, pixel_array: np.ndarray, image: Image): ...
    def adjust_out_of_range_points(self, points: np.ndarray): ...
    def transform_points_pre_display(self, mobject, points): ...
    def points_to_pixel_coords(self, mobject, points): ...
    def on_screen_pixels(self, pixel_coords: np.ndarray): ...
    def adjusted_thickness(self, thickness: float): ...
    def get_thickening_nudges(self, thickness: float): ...
    def thickened_coordinates(self, pixel_coords: np.ndarray, thickness: float): ...
    def get_coords_of_all_pixels(self): ...

class BackgroundColoredVMobjectDisplayer:
    camera: Incomplete
    file_name_to_pixel_array_map: Incomplete
    pixel_array: Incomplete
    def __init__(self, camera: Camera) -> None: ...
    def reset_pixel_array(self) -> None: ...
    def resize_background_array(self, background_array: np.ndarray, new_width: float, new_height: float, mode: str = ...): ...
    def resize_background_array_to_match(self, background_array: np.ndarray, pixel_array: np.ndarray): ...
    def get_background_array(self, image: Image.Image | pathlib.Path | str): ...
    def display(self, *cvmobjects: VMobject): ...
