from . import cli_ctx_settings as cli_ctx_settings, console as console
from .cli.cfg.group import cfg as cfg
from .cli.default_group import DefaultGroup as DefaultGroup
from .cli.init.commands import init as init
from .cli.new.group import new as new
from .cli.plugins.commands import plugins as plugins
from .cli.render.commands import render as render
from .constants import EPILOG as EPILOG

def exit_early(ctx, param, value) -> None: ...
def main(ctx) -> None: ...
