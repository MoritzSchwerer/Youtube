from ._test_class_makers import DummySceneFileWriter as DummySceneFileWriter
from _pytest.fixtures import FixtureRequest as FixtureRequest
from _typeshed import Incomplete
from manim import Scene as Scene
from manim._config import tempconfig as tempconfig
from manim._config.utils import ManimConfig as ManimConfig
from manim.camera.three_d_camera import ThreeDCamera as ThreeDCamera
from manim.renderer.cairo_renderer import CairoRenderer as CairoRenderer
from manim.scene.three_d_scene import ThreeDScene as ThreeDScene

SCENE_PARAMETER_NAME: str
PATH_CONTROL_DATA: Incomplete

def frames_comparison(func: Incomplete | None = ..., *, last_frame: bool = ..., renderer_class=..., base_scene=..., **custom_config): ...
