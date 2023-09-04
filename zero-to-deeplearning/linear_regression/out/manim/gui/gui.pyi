from .. import config as config
from ..utils.module_ops import scene_classes_from_file as scene_classes_from_file
from _typeshed import Incomplete

dearpygui_imported: bool
window: Incomplete

def configure_pygui(renderer, widgets, update: bool = ...) -> None: ...
