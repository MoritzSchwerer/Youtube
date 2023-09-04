from ..constants import RendererType as RendererType
from IPython.core.interactiveshell import InteractiveShell as InteractiveShell
from IPython.core.magic import Magics
from _typeshed import Incomplete
from manim import Group as Group, config as config, logger as logger, tempconfig as tempconfig
from manim.__main__ import main as main
from manim.renderer.shader import shader_program_cache as shader_program_cache
from typing import Any

class ManimMagic(Magics):
    rendered_files: Incomplete
    def __init__(self, shell: InteractiveShell) -> None: ...
    def manim(self, line: str, cell: str = ..., local_ns: dict[str, Any] = ...) -> None: ...
    def add_additional_args(self, args: list[str]) -> list[str]: ...
