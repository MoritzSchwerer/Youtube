import numpy as np
from _typeshed import Incomplete
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface
from pathlib import Path

class OpenGLImageMobject(OpenGLTexturedSurface):
    image: Incomplete
    resampling_algorithm: Incomplete
    size: Incomplete
    def __init__(self, filename_or_array: str | Path | np.ndarray, width: float = ..., height: float = ..., image_mode: str = ..., resampling_algorithm: int = ..., opacity: float = ..., gloss: float = ..., shadow: float = ..., **kwargs) -> None: ...
    def get_image_from_file(self, image_file: str | Path | np.ndarray, image_mode: str): ...
