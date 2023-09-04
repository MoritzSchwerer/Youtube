from _typeshed import Incomplete
from docutils import nodes
from docutils.parsers.rst import Directive
from manim import QUALITIES as QUALITIES

classnamedict: Incomplete

class SkipManimNode(nodes.Admonition, nodes.Element): ...

def visit(self, node, name: str = ...) -> None: ...
def depart(self, node) -> None: ...
def process_name_list(option_input: str, reference_type: str) -> list[str]: ...

class ManimDirective(Directive):
    has_content: bool
    required_arguments: int
    optional_arguments: int
    option_spec: Incomplete
    final_argument_whitespace: bool
    def run(self): ...

rendering_times_file_path: Incomplete

def setup(app): ...

TEMPLATE: str
