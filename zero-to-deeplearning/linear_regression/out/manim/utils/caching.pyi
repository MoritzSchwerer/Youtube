from .. import config as config, logger as logger
from ..utils.hashing import get_hash_from_play_call as get_hash_from_play_call
from typing import Callable

def handle_caching_play(func: Callable[..., None]): ...
