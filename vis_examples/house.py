import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pf
import seaborn as sns

from tqdm import tqdm
from matplotlib.animation import FuncAnimation
from scipy.interpolate import interp1d

from sklearn.linear_model import SGDRegressor
from sklearn import preprocessing
import numpy as np


def main():
    data = pf.read_csv('./kc_house_data.csv')
    data = data[0:-1:30]
    x = data['sqft_living']
    y = data['price']
    fig, ax = plt.subplots()
    ax.set_xlim(0, 6000)
    xs = np.arange(0, 6000, 10)
    ax.set_ylim(0, 3000000)
    x = x.values.reshape(-1, 1)
    y = y.values.reshape(-1)
    # x = preprocessing.StandardScaler().fit(x)
    reg = SGDRegressor(
        max_iter=1000,
    )
    for _ in range(10):
        reg.fit(x, y.ravel())

        def linear(x, intercept, coef):
            return intercept + coef * x

        ys = linear(xs, reg.intercept_, reg.coef_)
        plt.scatter(x, y, color='blue')
        plt.plot(xs, ys, color='red')
        plt.show()

        plt.pause(0.5)
    # plt.scatter(x, y)


if __name__ == '__main__':
    main()
