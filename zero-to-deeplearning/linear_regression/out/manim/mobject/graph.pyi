import networkx as nx
from .mobject import Mobject
from .types.vectorized_mobject import VMobject
from _typeshed import Incomplete
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from typing import Hashable

class Graph(VMobject, metaclass=ConvertToOpenGL):
    default_vertex_config: Incomplete
    vertices: Incomplete
    default_edge_config: Incomplete
    edges: Incomplete
    def __init__(self, vertices: list[Hashable], edges: list[tuple[Hashable, Hashable]], labels: bool | dict = ..., label_fill_color: str = ..., layout: str | dict = ..., layout_scale: float | tuple = ..., layout_config: dict | None = ..., vertex_type: type[Mobject] = ..., vertex_config: dict | None = ..., vertex_mobjects: dict | None = ..., edge_type: type[Mobject] = ..., partitions: list[list[Hashable]] | None = ..., root_vertex: Hashable | None = ..., edge_config: dict | None = ...) -> None: ...
    def __getitem__(self, v: Hashable) -> Mobject: ...
    def add_vertices(self, *vertices: Hashable, positions: dict | None = ..., labels: bool = ..., label_fill_color: str = ..., vertex_type: type[Mobject] = ..., vertex_config: dict | None = ..., vertex_mobjects: dict | None = ...): ...
    def remove_vertices(self, *vertices): ...
    def add_edges(self, *edges: tuple[Hashable, Hashable], edge_type: type[Mobject] = ..., edge_config: dict | None = ..., **kwargs): ...
    def remove_edges(self, *edges: tuple[Hashable]): ...
    @staticmethod
    def from_networkx(nxgraph: nx.classes.graph.Graph, **kwargs) -> Graph: ...
    def change_layout(self, layout: str | dict = ..., layout_scale: float = ..., layout_config: dict | None = ..., partitions: list[list[Hashable]] | None = ..., root_vertex: Hashable | None = ...) -> Graph: ...
