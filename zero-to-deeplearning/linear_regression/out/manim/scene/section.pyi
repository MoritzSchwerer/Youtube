from _typeshed import Incomplete
from enum import Enum
from manim import get_video_metadata as get_video_metadata
from pathlib import Path
from typing import Any

class DefaultSectionType(str, Enum):
    NORMAL: str

class Section:
    type: Incomplete
    video: Incomplete
    name: Incomplete
    skip_animations: Incomplete
    partial_movie_files: Incomplete
    def __init__(self, type: str, video: str | None, name: str, skip_animations: bool) -> None: ...
    def is_empty(self) -> bool: ...
    def get_clean_partial_movie_files(self) -> list[str]: ...
    def get_dict(self, sections_dir: Path) -> dict[str, Any]: ...
