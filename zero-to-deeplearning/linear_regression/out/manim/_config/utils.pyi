import argparse
import configparser
import os
from .. import constants as constants
from ..constants import RendererType as RendererType
from ..utils.tex import TexTemplate as TexTemplate, TexTemplateFromFile as TexTemplateFromFile
from ..utils.tex_templates import TexTemplateLibrary as TexTemplateLibrary
from _typeshed import Incomplete
from collections.abc import Mapping, MutableMapping
from pathlib import Path
from typing import Any, Iterable, Iterator

def config_file_paths() -> list[Path]: ...
def make_config_parser(custom_file: str | os.PathLike | None = ...) -> configparser.ConfigParser: ...

class ManimConfig(MutableMapping):
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __contains__(self, key) -> bool: ...
    def __getitem__(self, key) -> Any: ...
    def __setitem__(self, key: str, val: Any) -> None: ...
    def update(self, obj: ManimConfig | dict) -> None: ...
    def __delitem__(self, key: str): ...
    def __delattr__(self, key: str): ...
    def copy(self) -> ManimConfig: ...
    def __copy__(self) -> ManimConfig: ...
    def __deepcopy__(self, memo: dict[str, Any]) -> ManimConfig: ...
    ffmpeg_loglevel: Incomplete
    def digest_parser(self, parser: configparser.ConfigParser) -> ManimConfig: ...
    input_file: Incomplete
    scene_names: Incomplete
    output_file: Incomplete
    from_animation_number: Incomplete
    upto_animation_number: Incomplete
    pixel_width: Incomplete
    pixel_height: Incomplete
    frame_rate: Incomplete
    media_dir: Incomplete
    gui_location: Incomplete
    def digest_args(self, args: argparse.Namespace) -> ManimConfig: ...
    def digest_file(self, filename: str | os.PathLike) -> ManimConfig: ...
    preview: Incomplete
    show_in_file_browser: Incomplete
    progress_bar: Incomplete
    log_to_file: Incomplete
    notify_outdated_version: Incomplete
    write_to_movie: Incomplete
    save_last_frame: Incomplete
    write_all: Incomplete
    save_pngs: Incomplete
    save_as_gif: Incomplete
    save_sections: Incomplete
    enable_wireframe: Incomplete
    force_window: Incomplete
    @property
    def verbosity(self): ...
    @property
    def format(self): ...
    ffmpeg_executable: Incomplete
    media_embed: Incomplete
    media_width: Incomplete
    aspect_ratio: Incomplete
    frame_height: Incomplete
    frame_width: Incomplete
    frame_y_radius: Incomplete
    frame_x_radius: Incomplete
    top: Incomplete
    bottom: Incomplete
    left_side: Incomplete
    right_side: Incomplete
    background_color: Incomplete
    max_files_cached: Incomplete
    window_monitor: Incomplete
    flush_cache: Incomplete
    disable_caching: Incomplete
    disable_caching_warning: Incomplete
    movie_file_extension: Incomplete
    background_opacity: Incomplete
    frame_size: Incomplete
    @property
    def quality(self): ...
    @property
    def transparent(self): ...
    @property
    def dry_run(self): ...
    @property
    def renderer(self): ...
    window_position: Incomplete
    window_size: Incomplete
    def resolve_movie_file_extension(self, is_transparent) -> None: ...
    enable_gui: Incomplete
    fullscreen: Incomplete
    use_projection_fill_shaders: Incomplete
    use_projection_stroke_shaders: Incomplete
    zero_pad: Incomplete
    def get_dir(self, key: str, **kwargs: str) -> Path: ...
    assets_dir: Incomplete
    log_dir: Incomplete
    video_dir: Incomplete
    sections_dir: Incomplete
    images_dir: Incomplete
    text_dir: Incomplete
    tex_dir: Incomplete
    partial_movie_dir: Incomplete
    custom_folders: Incomplete
    @property
    def tex_template(self): ...
    @property
    def tex_template_file(self): ...
    @property
    def plugins(self): ...

class ManimFrame(Mapping):
    def __init__(self, c: ManimConfig) -> None: ...
    def __getitem__(self, key: str | int) -> Any: ...
    def __iter__(self) -> Iterable: ...
    def __len__(self) -> int: ...
    def __setattr__(self, attr, val) -> None: ...
    def __setitem__(self, key, val) -> None: ...
    def __delitem__(self, key) -> None: ...
