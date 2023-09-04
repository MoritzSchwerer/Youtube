from ..constants import *
from ..scene.moving_camera_scene import MovingCameraScene
from _typeshed import Incomplete

class ZoomedScene(MovingCameraScene):
    zoomed_display_height: Incomplete
    zoomed_display_width: Incomplete
    zoomed_display_center: Incomplete
    zoomed_display_corner: Incomplete
    zoomed_display_corner_buff: Incomplete
    zoomed_camera_config: Incomplete
    zoomed_camera_image_mobject_config: Incomplete
    zoomed_camera_frame_starting_position: Incomplete
    zoom_factor: Incomplete
    image_frame_stroke_width: Incomplete
    zoom_activated: Incomplete
    def __init__(self, camera_class=..., zoomed_display_height: int = ..., zoomed_display_width: int = ..., zoomed_display_center: Incomplete | None = ..., zoomed_display_corner=..., zoomed_display_corner_buff=..., zoomed_camera_config=..., zoomed_camera_image_mobject_config=..., zoomed_camera_frame_starting_position=..., zoom_factor: float = ..., image_frame_stroke_width: int = ..., zoom_activated: bool = ..., **kwargs) -> None: ...
    zoomed_camera: Incomplete
    zoomed_display: Incomplete
    def setup(self) -> None: ...
    def activate_zooming(self, animate: bool = ...): ...
    def get_zoom_in_animation(self, run_time: float = ..., **kwargs): ...
    def get_zoomed_display_pop_out_animation(self, **kwargs): ...
    def get_zoom_factor(self): ...
