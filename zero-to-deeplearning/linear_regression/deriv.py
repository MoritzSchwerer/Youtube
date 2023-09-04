from manim import *
from typing import List


class TexTransform:
    def __init__(self, scene, first, second, mapping: List[int]) -> None:
        self.scene = scene
        self.first: VGroup = VGroup(*[MathTex(x) for x in first])
        self.second: VGroup = VGroup(*[MathTex(x) for x in second])
        self.mapping: List[int] = mapping
        assert len(self.first) >= len(self.second)
        assert max(self.mapping) < len(self.second)

    def create(self, **kwargs) -> None:
        self.scene.play(Write(self.first), **kwargs)

    def arrange(self, direction=RIGHT, **kwargs) -> None:
        self.first.arrange(direction, **kwargs)   # type: ignore
        for i_f, i_s in enumerate(self.mapping):
            if i_s == -1:
                continue
            self.second[i_s].move_to(self.first[i_f])

    def transition(self, lag_ratio: float = 1) -> None:
        self.scene.play(
            LaggedStart(
                *[
                    ReplacementTransform(f, self.second[s_i])
                    if s_i != -1
                    else FadeOut(f)
                    for f, s_i in zip(self.first, self.mapping)
                ],
                lag_ratio=lag_ratio,
            ),
        )

    def compress(self, buff=0.2) -> None:
        comp: VGroup = self.second.copy()
        comp.arrange(RIGHT, buff=buff)   # type: ignore
        self.scene.play(ReplacementTransform(self.second, comp))


class EquationTransform(Scene):
    def construct(self) -> None:
        # Set the initial position of the equations

        tt = TexTransform(
            self,
            [r'f =', r'x^2', '-', '7', '+', 'y^3'],
            [r'f =', r'2x', '+', '3y^2'],
            [0, 1, -1, -1, 2, 3],
        )

        tt.arrange(direction=RIGHT, buff=0.2)
        tt.create()
        self.wait(1)
        tt.transition(lag_ratio=0.2)
        self.wait(1)
        tt.compress()
        self.wait(1)
