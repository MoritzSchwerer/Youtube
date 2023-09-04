import typing
from _typeshed import Incomplete
from manim.animation.animation import Animation
from manim.mobject.mobject import Mobject

class UpdateFromFunc(Animation):
    update_function: Incomplete
    def __init__(self, mobject: Mobject, update_function: typing.Callable[[Mobject], typing.Any], suspend_mobject_updating: bool = ..., **kwargs) -> None: ...
    def interpolate_mobject(self, alpha: float) -> None: ...

class UpdateFromAlphaFunc(UpdateFromFunc):
    def interpolate_mobject(self, alpha: float) -> None: ...

class MaintainPositionRelativeTo(Animation):
    tracked_mobject: Incomplete
    diff: Incomplete
    def __init__(self, mobject: Mobject, tracked_mobject: Mobject, **kwargs) -> None: ...
    def interpolate_mobject(self, alpha: float) -> None: ...
