import json
import typing
from .. import config as config, logger as logger
from _typeshed import Incomplete
from manim.animation.animation import Animation as Animation
from manim.camera.camera import Camera as Camera
from manim.mobject.mobject import Mobject as Mobject
from manim.scene.scene import Scene as Scene
from typing import Any

KEYS_TO_FILTER_OUT: Incomplete

class _Memoizer:
    ALREADY_PROCESSED_PLACEHOLDER: str
    THRESHOLD_WARNING: int
    @classmethod
    def reset_already_processed(cls) -> None: ...
    @classmethod
    def check_already_processed_decorator(cls, is_method: bool = ...): ...
    @classmethod
    def check_already_processed(cls, obj: Any) -> Any: ...
    @classmethod
    def mark_as_processed(cls, obj: Any) -> None: ...

class _CustomEncoder(json.JSONEncoder):
    def default(self, obj: Any): ...
    def encode(self, obj: Any): ...

def get_json(obj: dict): ...
def get_hash_from_play_call(scene_object: Scene, camera_object: Camera, animations_list: typing.Iterable[Animation], current_mobjects_list: typing.Iterable[Mobject]) -> str: ...
