from manim import *
from utils import get_dataset, ScatterPlot

LIVE = 1
TEST = 0.1
SPEED = TEST


class GoodnessOfFit2(Scene):
    def construct(self) -> None:
        m = 0.8
        b = 1.5
        self.m = m
        self.b = b

        eText = Text('E = ?')
        self.play(Write(eText), run_time=SPEED * 2)
        self.play(FadeOut(eText, shift=UP * 3), run_time=SPEED * 2)

        scatter = ScatterPlot(*get_dataset(), point_scale=1.5)
        axes = scatter.axes
        points = scatter.points

        self.play(Write(axes), run_time=SPEED * 1)
        self.play(Create(points), run_time=SPEED * 1)
        self.wait(SPEED * 1)

        line = self.get_line(axes, m, b, GREEN)
        self.play(Create(line), run_time=SPEED * 1)
        self.wait(SPEED * 2)

        self._get_error_lines(axes)
        for line in self.error_lines:
            self.play(Create(line), run_time=SPEED * 0.2)

        # self.error_eq1.next_to(axes, DOWN)
        self.error_eq1.scale(0.5)
        self.play(Write(self.error_eq1), run_time=SPEED * 1)

        # self.error_eq2.move_to(self.error_eq1)
        self.error_eq2.scale(0.5)
        self.play(
            Succession(
                *[
                    ReplacementTransform(self.error_eq1[i], self.error_eq2[i])
                    for i in range(len(self.error_eq2))
                ],
                lag_ratio=SPEED * 0.5,
            )
        )

        self.res1.next_to(axes, DOWN)
        self.res1.scale(0.5)
        self.wait(SPEED * 2)
        self.play(
            ReplacementTransform(self.error_eq2, self.res1), run_time=SPEED * 2
        )
        self.wait(SPEED * 2)

    def _get_error_lines(self, axes) -> None:
        xs, ys = get_dataset()
        ctp = axes.coords_to_point
        lines = []
        equations1 = []
        equations2 = []
        res = 0
        for x, y1 in zip(xs, ys):
            y2 = self.equation(x, self.m, self.b)
            equations1.append('({} - {})'.format(round(y1, 2), round(y2, 2)))
            equations2.append('{}'.format(round(y1 - y2, 2)))
            res += y1 - y2
            lines.append(
                Line(
                    ctp(x, y1),
                    ctp(x, y2),
                    color=RED,
                )
            )
        string1 = []
        for eq in equations1:
            string1.append(eq)
            string1.append('+')
        string1 = string1[:-1]
        string2 = []
        for eq in equations2:
            string2.append(eq)
            string2.append('+')
        string2 = string2[:-1]

        print('E = ', *string1)
        print(string2)
        self.error_eq1 = VGroup(*[Tex(a) for a in ('E = ', *string1)])
        self.error_eq1.arrange(RIGHT, buff=0.2)
        self.error_eq2 = VGroup(*[Tex(a) for a in ('E = ', *string2)])
        self.error_eq2.arrange(RIGHT, buff=0.2)
        self.res1 = Tex('E = ', str(round(res, 2)))
        self.error_lines = Group(*lines)

    def get_line(self, axes, m, b, color) -> Mobject:
        return axes.plot(lambda x: m * x + b, color=color)

    def equation(self, x, m, b) -> float:
        return m * x + b


class GoodnessOfFit1(Scene):
    def construct(self) -> None:
        scatter = ScatterPlot(*get_dataset())
        axes, points = scatter.axes, scatter.points
        labels = axes.get_axis_labels(x_label='x', y_label='y')
        self.play(
            Succession(Create(axes), Create(points), Write(labels)),
            run_time=SPEED * 2,
        )
        self.wait(SPEED)

        def get_line(m, b, color) -> Mobject:
            return axes.plot(lambda x: m * x + b, color=color)

        lines = []
        ms = [0.5, 1.1, -1]
        bs = [1, -1, 5]
        colors = [RED, GREEN, BLUE]
        for m, b, c in zip(ms, bs, colors):
            lines.append(get_line(m, b, c))
        lines = Group(*lines)
        for line in lines:
            self.play(Create(line), run_time=SPEED * 1)
        ax_group = VGroup(axes, points, labels, *lines)
        self.wait(SPEED * 2)
        self.play(ax_group.animate.scale(0.6))
        self.play(ax_group.animate.move_to(LEFT * 2))

        def get_eq(e, color) -> MathTex:
            t = Text(f'E = {round(e, 1)}', color=color)
            t.scale(0.4)
            return t

        eqs = []
        results = [0.5, 0.2, 0.8]
        for res, color in zip(results, colors):
            eqs.append(get_eq(res, color))
        eqs = Group(*eqs)
        eqs.arrange(DOWN)
        eqs.next_to(axes, RIGHT)
        self.add(eqs)
        self.wait(2)


class LineEquation(Scene):
    def construct(self) -> None:
        mv = ValueTracker(0.50)
        ms = ValueTracker(0.50)
        bv = ValueTracker(1.00)
        bs = ValueTracker(1.00)

        axes1 = ScatterPlot([], []).axes
        axes2 = ScatterPlot([], []).axes
        axes2.scale(1 / 1.6)

        def get_equation1() -> MathTex:
            text = Text(
                f'y = {round(mv.get_value(), 2)} x + {round(bs.get_value(), 2)}'
            )
            text.next_to(axes1, DOWN)
            text.scale(0.4)
            return text

        def get_equation2() -> MathTex:
            text = Text(
                f'y = {round(ms.get_value(), 2)} x + {round(bv.get_value(), 2)}'
            )
            text.next_to(axes2, DOWN)
            text.scale(0.4)
            return text

        def get_line1() -> Mobject:
            return axes1.plot(
                lambda x: mv.get_value() * x + bs.get_value(), color=RED
            )

        def get_line2() -> Mobject:
            return axes2.plot(
                lambda x: ms.get_value() * x + bv.get_value(), color=RED
            )

        axes2.move_to(RIGHT * 4)
        line1 = always_redraw(get_line1)
        line2 = always_redraw(get_line2)
        eq1 = always_redraw(get_equation1)
        eq2 = always_redraw(get_equation2)

        self.play(
            Succession(Create(axes1), Create(line1), Write(eq1)),
            run_time=SPEED * 2,
        )
        self.play(mv.animate.set_value(1.1), run_time=SPEED * 1)
        self.play(mv.animate.set_value(0), run_time=SPEED * 1)
        self.play(axes1.animate.scale(1 / 1.6), run_time=SPEED * 1)
        self.play(axes1.animate.move_to(LEFT * 4), run_time=SPEED * 1)

        self.play(
            Succession(Create(axes2), Create(line2), Write(eq2)),
            run_time=SPEED * 2,
        )
        self.play(bv.animate.set_value(4), run_time=SPEED * 1)
        self.play(bv.animate.set_value(-2), run_time=SPEED * 1)

        self.wait(2)


class WhatIsLr(Scene):
    def construct(self) -> None:
        scatter = ScatterPlot(*get_dataset(), point_scale=1.5)
        axes = scatter.axes
        points = scatter.points

        labels = axes.get_axis_labels(x_label='year', y_label='revenue(M)')
        self.play(Succession(Create(axes), Create(points), Write(labels)))
        self.wait(SPEED * 2)

        m = ValueTracker(0.5)
        b = ValueTracker(1)

        def get_line() -> Mobject:
            return axes.plot(
                lambda x: m.get_value() * x + b.get_value(), color=RED
            )

        def get_equation() -> MathTex:
            text = Text(
                f'y = {round(m.get_value(), 2)} x + {round(b.get_value(), 2)}'
            )
            text.next_to(axes, DOWN)
            return text

        line = always_redraw(get_line)
        equation = always_redraw(get_equation)

        self.play(Create(line), Create(equation), run_time=SPEED * 1)

        self.wait(SPEED)
        self.play(
            m.animate.set_value(1.5),
            b.animate.set_value(2),
            run_time=SPEED * 3,
        )
        self.play(
            m.animate.set_value(1.3),
            b.animate.set_value(3),
            run_time=SPEED * 3,
        )
        self.wait(SPEED * 2)
