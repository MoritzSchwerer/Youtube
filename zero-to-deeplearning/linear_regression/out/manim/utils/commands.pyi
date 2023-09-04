import os
from _typeshed import Incomplete
from pathlib import Path
from typing import Generator

def capture(command, cwd: Incomplete | None = ..., command_input: Incomplete | None = ...): ...
def get_video_metadata(path_to_video: str | os.PathLike) -> dict[str]: ...
def get_dir_layout(dirpath: Path) -> Generator[str, None, None]: ...
