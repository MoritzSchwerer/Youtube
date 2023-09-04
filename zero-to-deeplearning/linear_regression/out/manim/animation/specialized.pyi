from ..constants import *
from .composition import LaggedStart
from _typeshed import Incomplete
from typing import Any, Sequence

class Broadcast(LaggedStart):
    focal_point: Incomplete
    n_mobs: Incomplete
    initial_opacity: Incomplete
    final_opacity: Incomplete
    initial_width: Incomplete
    def __init__(self, mobject, focal_point: Sequence[float] = ..., n_mobs: int = ..., initial_opacity: float = ..., final_opacity: float = ..., initial_width: float = ..., remover: bool = ..., lag_ratio: float = ..., run_time: float = ..., **kwargs: Any) -> None: ...
