from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.types.vectorized_mobject import VMobject

class _BooleanOps(VMobject, metaclass=ConvertToOpenGL):
    def __init__(self, *args, **kwargs) -> None: ...

class Union(_BooleanOps):
    def __init__(self, *vmobjects: VMobject, **kwargs) -> None: ...

class Difference(_BooleanOps):
    def __init__(self, subject, clip, **kwargs) -> None: ...

class Intersection(_BooleanOps):
    def __init__(self, *vmobjects, **kwargs) -> None: ...

class Exclusion(_BooleanOps):
    def __init__(self, subject, clip, **kwargs) -> None: ...
