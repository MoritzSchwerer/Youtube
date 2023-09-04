import logging
from .utils import ManimConfig
from _typeshed import Incomplete
from contextlib import _GeneratorContextManager

logger: logging.Logger
console: Incomplete
error_console: Incomplete
cli_ctx_settings: Incomplete
config: Incomplete
frame: Incomplete

def tempconfig(temp: ManimConfig | dict) -> _GeneratorContextManager: ...
