import numpy as np
import matplotlib.pyplot as plt
from manim import *
from typing import Tuple, List


def get_dataset() -> Tuple[list, list]:
    xs = list(range(10))
    ys = [2, 3.5, 6.9, 4.9, 6.5, 7.9, 5.2, 9.1, 10.5, 10.2]
    return xs, ys


if __name__ == '__main__':
    xs, ys = get_dataset()
    plt.scatter(xs, ys)
    plt.show()


class ScatterPlot:
    def __init__(
        self, xs: List[float], ys: List[float], point_scale: float = 1
    ) -> None:
        self.xs = xs
        self.ys = ys
        self.point_scale = point_scale
        self.axes = self.get_axes()
        self.points = self.get_points()

    def get_axes(
        self,
        x_range=[0, 11, 1],
        y_range=[0, 11, 2],
        include_numbers=True,
        scale=0.9,
    ) -> Axes:
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            axis_config={
                'include_numbers': include_numbers,
                'include_ticks': True,
            },
        )
        axes.scale(scale)
        axes.set_color(BLUE)
        return axes

    def get_points(self) -> VGroup:
        axes = self.axes
        points = []
        for x, y in zip(self.xs, self.ys):
            p = Dot(color=RED_D)
            p.move_to(axes.coords_to_point(x, y))
            p.scale(self.point_scale)
            points.append(p)
        points = VGroup(*points)
        return points
