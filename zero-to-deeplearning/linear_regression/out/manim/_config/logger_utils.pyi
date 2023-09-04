import configparser
import logging
from _typeshed import Incomplete
from pathlib import Path
from rich.console import Console
from rich.theme import Theme

HIGHLIGHTED_KEYWORDS: Incomplete
WRONG_COLOR_CONFIG_MSG: str

def make_logger(parser: configparser.ConfigParser, verbosity: str) -> tuple[logging.Logger, Console]: ...
def parse_theme(parser: configparser.ConfigParser) -> Theme: ...
def set_file_logger(scene_name: str, module_name: str, log_dir: Path) -> None: ...

class JSONFormatter(logging.Formatter):
    def format(self, record: dict) -> str: ...
