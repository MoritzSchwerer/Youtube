from ..constants import *
from ..scene.scene_file_writer import SceneFileWriter as SceneFileWriter
from ..utils import opengl as opengl
from ..utils.simple_functions import clip as clip
from ..utils.space_ops import angle_of_vector as angle_of_vector, quaternion_from_angle_axis as quaternion_from_angle_axis, quaternion_mult as quaternion_mult, rotation_matrix_transpose as rotation_matrix_transpose, rotation_matrix_transpose_from_quaternion as rotation_matrix_transpose_from_quaternion
from .shader import Mesh as Mesh, Shader as Shader
from .vectorized_mobject_rendering import render_opengl_vectorized_mobject_fill as render_opengl_vectorized_mobject_fill, render_opengl_vectorized_mobject_stroke as render_opengl_vectorized_mobject_stroke
from PIL import Image
from _typeshed import Incomplete
from functools import cached_property as cached_property
from manim import config as config, logger as logger
from manim.mobject.opengl.opengl_mobject import OpenGLMobject as OpenGLMobject, OpenGLPoint as OpenGLPoint
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject as OpenGLVMobject
from manim.utils.caching import handle_caching_play as handle_caching_play
from manim.utils.color import color_to_rgba as color_to_rgba
from manim.utils.exceptions import EndSceneEarlyException as EndSceneEarlyException

class OpenGLCamera(OpenGLMobject):
    euler_angles: Incomplete
    use_z_index: bool
    frame_rate: int
    orthographic: Incomplete
    minimum_polar_angle: Incomplete
    maximum_polar_angle: Incomplete
    projection_matrix: Incomplete
    unformatted_projection_matrix: Incomplete
    frame_shape: Incomplete
    center_point: Incomplete
    focal_distance: Incomplete
    light_source_position: Incomplete
    light_source: Incomplete
    default_model_matrix: Incomplete
    def __init__(self, frame_shape: Incomplete | None = ..., center_point: Incomplete | None = ..., euler_angles=..., focal_distance: int = ..., light_source_position=..., orthographic: bool = ..., minimum_polar_angle=..., maximum_polar_angle=..., model_matrix: Incomplete | None = ..., **kwargs) -> None: ...
    def get_position(self): ...
    def set_position(self, position): ...
    @cached_property
    def formatted_view_matrix(self): ...
    @cached_property
    def unformatted_view_matrix(self): ...
    def init_points(self) -> None: ...
    model_matrix: Incomplete
    def to_default_state(self): ...
    inverse_rotation_matrix: Incomplete
    def refresh_rotation_matrix(self) -> None: ...
    def rotate(self, angle, axis=..., **kwargs): ...
    def set_euler_angles(self, theta: Incomplete | None = ..., phi: Incomplete | None = ..., gamma: Incomplete | None = ...): ...
    def set_theta(self, theta): ...
    def set_phi(self, phi): ...
    def set_gamma(self, gamma): ...
    def increment_theta(self, dtheta): ...
    def increment_phi(self, dphi): ...
    def increment_gamma(self, dgamma): ...
    def get_shape(self): ...
    def get_center(self): ...
    def get_width(self): ...
    def get_height(self): ...
    def get_focal_distance(self): ...
    def interpolate(self, *args, **kwargs) -> None: ...

points_per_curve: int

class OpenGLRenderer:
    anti_alias_width: float
    skip_animations: Incomplete
    animation_start_time: int
    animation_elapsed_time: int
    time: int
    animations_hashes: Incomplete
    num_plays: int
    camera: Incomplete
    pressed_keys: Incomplete
    path_to_texture_id: Incomplete
    def __init__(self, file_writer_class=..., skip_animations: bool = ...) -> None: ...
    partial_movie_files: Incomplete
    file_writer: Incomplete
    scene: Incomplete
    window: Incomplete
    context: Incomplete
    frame_buffer_object: Incomplete
    def init_scene(self, scene) -> None: ...
    def should_create_window(self): ...
    def get_pixel_shape(self): ...
    perspective_uniforms: Incomplete
    def refresh_perspective_uniforms(self, camera) -> None: ...
    def render_mobject(self, mobject) -> None: ...
    def get_texture_id(self, path): ...
    def update_skipping_status(self) -> None: ...
    def play(self, scene, *args, **kwargs) -> None: ...
    def clear_screen(self) -> None: ...
    def render(self, scene, frame_offset, moving_mobjects) -> None: ...
    def update_frame(self, scene) -> None: ...
    def scene_finished(self, scene) -> None: ...
    def should_save_last_frame(self): ...
    def get_image(self) -> Image.Image: ...
    def save_static_frame_data(self, scene, static_mobjects) -> None: ...
    def get_frame_buffer_object(self, context, samples: int = ...): ...
    def get_raw_frame_buffer_object_data(self, dtype: str = ...): ...
    def get_frame(self): ...
    def pixel_coords_to_space_coords(self, px, py, relative: bool = ..., top_left: bool = ...): ...
    @property
    def background_color(self): ...
