from ...constants import RendererType as RendererType
from abc import ABCMeta
from manim import config as config
from manim.mobject.opengl.opengl_mobject import OpenGLMobject as OpenGLMobject
from manim.mobject.opengl.opengl_point_cloud_mobject import OpenGLPMobject as OpenGLPMobject
from manim.mobject.opengl.opengl_three_dimensions import OpenGLSurface as OpenGLSurface
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject as OpenGLVMobject

class ConvertToOpenGL(ABCMeta):
    def __new__(mcls, name, bases, namespace): ...
    def __init__(cls, name, bases, namespace) -> None: ...
