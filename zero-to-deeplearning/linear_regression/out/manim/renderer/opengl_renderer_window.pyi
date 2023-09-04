from .. import config as config
from _typeshed import Incomplete
from moderngl_window.context.pyglet.window import Window as PygletWindow

class Window(PygletWindow):
    fullscreen: bool
    resizable: bool
    gl_version: Incomplete
    vsync: bool
    cursor: bool
    title: Incomplete
    size: Incomplete
    renderer: Incomplete
    timer: Incomplete
    config: Incomplete
    position: Incomplete
    def __init__(self, renderer, size=..., **kwargs) -> None: ...
    def on_mouse_motion(self, x, y, dx, dy) -> None: ...
    def on_mouse_scroll(self, x, y, x_offset: float, y_offset: float): ...
    def on_key_press(self, symbol, modifiers) -> None: ...
    def on_key_release(self, symbol, modifiers) -> None: ...
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers) -> None: ...
    def find_initial_position(self, size, monitor): ...
    def on_mouse_press(self, x, y, button, modifiers) -> None: ...
