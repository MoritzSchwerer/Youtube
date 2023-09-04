import inspect
from types import MappingProxyType
from typing import Callable

def binary_search(function: Callable[[int | float], int | float], target: int | float, lower_bound: int | float, upper_bound: int | float, tolerance: int | float = ...) -> int | float | None: ...
def choose(n: int, k: int) -> int: ...
def clip(a, min_a, max_a): ...
def get_parameters(function: Callable) -> MappingProxyType[str, inspect.Parameter]: ...
def sigmoid(x: float) -> float: ...
