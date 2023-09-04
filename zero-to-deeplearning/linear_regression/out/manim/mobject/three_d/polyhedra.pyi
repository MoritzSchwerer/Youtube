import numpy as np
from _typeshed import Incomplete
from manim.mobject.mobject import Mobject
from manim.mobject.types.vectorized_mobject import VGroup

class Polyhedron(VGroup):
    faces_config: Incomplete
    graph_config: Incomplete
    vertex_coords: Incomplete
    vertex_indices: Incomplete
    layout: Incomplete
    faces_list: Incomplete
    face_coords: Incomplete
    edges: Incomplete
    faces: Incomplete
    graph: Incomplete
    def __init__(self, vertex_coords: list[list[float] | np.ndarray], faces_list: list[list[int]], faces_config: dict[str, str | int | float | bool] = ..., graph_config: dict[str, str | int | float | bool] = ...) -> None: ...
    def get_edges(self, faces_list: list[list[int]]) -> list[tuple[int, int]]: ...
    def create_faces(self, face_coords: list[list[list | np.ndarray]]) -> VGroup: ...
    def update_faces(self, m: Mobject): ...
    def extract_face_coords(self) -> list[list[np.ndarray]]: ...

class Tetrahedron(Polyhedron):
    def __init__(self, edge_length: float = ..., **kwargs) -> None: ...

class Octahedron(Polyhedron):
    def __init__(self, edge_length: float = ..., **kwargs) -> None: ...

class Icosahedron(Polyhedron):
    def __init__(self, edge_length: float = ..., **kwargs) -> None: ...

class Dodecahedron(Polyhedron):
    def __init__(self, edge_length: float = ..., **kwargs) -> None: ...
