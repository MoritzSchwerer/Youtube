import numpy as np
from typing import Union, Tuple


def mse(y_true, y_pred) -> float:
    return ((y_true - y_pred) ** 2).mean()


def loss(y_true, y_pred, x=np.array(1)) -> float:
    return 2 * ((y_pred - y_true) * x).mean()


def line_y(x, m, b) -> Union[np.ndarray, float]:
    return m * x + b


def optimize(
    data: np.ndarray,
    m: float,
    b: float,
    learning_rate: float = 0.1,
    epochs: int = 100,
) -> Tuple[float, float]:
    for i in range(epochs):
        xs, ys = data[:, 0], data[:, 1]
        y_pred = line_y(xs, m, b)
        m -= learning_rate * loss(ys, y_pred, xs)
        b -= learning_rate * loss(ys, y_pred)
        # print(f'Epoch {i + 1}: m={m:.2f}, b={b:.2f}')
    return (m, b)


if __name__ == '__main__':
    data = np.array([[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12]])
    m = -0.1
    b = 1.2
    initial_loss = mse(data[:, 1], line_y(data[:, 0], m, b))
    print(f'Initial params: m={m:.2f}, b={b:.2f}')
    print(f'Loss before optimization: {initial_loss:.2f}')
    m, b = optimize(data, m, b, learning_rate=0.01, epochs=1000)
    final = mse(data[:, 1], line_y(data[:, 0], m, b))
    print(f'Loss after optimization: {final:.2f}')
    print(f'Final params: m={m:.2f}, b={b:.2f}')
