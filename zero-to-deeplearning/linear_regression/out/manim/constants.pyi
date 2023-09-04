import numpy as np
from _typeshed import Incomplete
from enum import Enum

SCENE_NOT_FOUND_MESSAGE: str
CHOOSE_NUMBER_MESSAGE: str
INVALID_NUMBER_MESSAGE: str
NO_SCENE_MESSAGE: str
NORMAL: str
ITALIC: str
OBLIQUE: str
BOLD: str
THIN: str
ULTRALIGHT: str
LIGHT: str
SEMILIGHT: str
BOOK: str
MEDIUM: str
SEMIBOLD: str
ULTRABOLD: str
HEAVY: str
ULTRAHEAVY: str
RESAMPLING_ALGORITHMS: Incomplete
ORIGIN: np.ndarray
UP: np.ndarray
DOWN: np.ndarray
RIGHT: np.ndarray
LEFT: np.ndarray
IN: np.ndarray
OUT: np.ndarray
X_AXIS: np.ndarray
Y_AXIS: np.ndarray
Z_AXIS: np.ndarray
UL: np.ndarray
UR: np.ndarray
DL: np.ndarray
DR: np.ndarray
START_X: int
START_Y: int
DEFAULT_DOT_RADIUS: float
DEFAULT_SMALL_DOT_RADIUS: float
DEFAULT_DASH_LENGTH: float
DEFAULT_ARROW_TIP_LENGTH: float
SMALL_BUFF: float
MED_SMALL_BUFF: float
MED_LARGE_BUFF: float
LARGE_BUFF: float
DEFAULT_MOBJECT_TO_EDGE_BUFFER: float
DEFAULT_MOBJECT_TO_MOBJECT_BUFFER: float
DEFAULT_POINTWISE_FUNCTION_RUN_TIME: float
DEFAULT_WAIT_TIME: float
DEFAULT_POINT_DENSITY_2D: int
DEFAULT_POINT_DENSITY_1D: int
DEFAULT_STROKE_WIDTH: int
DEFAULT_FONT_SIZE: float
PI: float
TAU: float
DEGREES: float
QUALITIES: dict[str, dict[str, str | int | None]]
DEFAULT_QUALITY: str
EPILOG: str
SHIFT_VALUE: int
CTRL_VALUE: int
CONTEXT_SETTINGS: Incomplete

class RendererType(Enum):
    CAIRO: str
    OPENGL: str

class LineJointType(Enum):
    AUTO: int
    ROUND: int
    BEVEL: int
    MITER: int
