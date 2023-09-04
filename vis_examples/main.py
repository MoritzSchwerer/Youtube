import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from tqdm import tqdm
from matplotlib.animation import FuncAnimation
from scipy.interpolate import interp1d

FRAME_DOWNSAMPLING = 1


def animate_line_collections(
    line_collections, fig, fills=None, only_fills=False, frame_downsampling=1
):
    """
    Creates an animation of multiple LineCollections being drawn

    Optionally can animate fills under the lines in sync
    """
    x_datas = []
    y_datas = []

    for lc in line_collections:
        segments = lc.get_segments()
        x_datas.append(np.array([seg[0, 0] for seg in segments]))
        y_datas.append(np.array([seg[0, 1] for seg in segments]))

    def anim_func(playhead_t):
        for k, lc in enumerate(line_collections):
            lc.set_alpha(x_datas[k] <= playhead_t)

        if fills is None:
            return (line_collections,)

        mask = x_datas[0] >= playhead_t
        x_masked = np.ma.masked_where(mask, x_datas[0])
        ax.collections.clear()

        for k, fill in enumerate(fills):

            y_masked = np.ma.masked_where(mask, y_datas[k])
            fills[k] = ax.fill_between(
                x_masked,
                0,
                y_masked,
                color=fill.get_facecolor(),
                alpha=fill.get_alpha(),
            )

        if not only_fills:
            ax.add_collection(lc)
        return line_collections, fills

    return matplotlib.animation.FuncAnimation(
        fig,
        anim_func,
        frames=tqdm(x_datas[0][::frame_downsampling]),
        interval=30,
    )


def make_segments(x, y):
    """Make segments for LineCollection"""
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    return np.concatenate([points[:-1], points[1:]], axis=1)


def setup_time_axes():
    """
    Setup a black Figure and Axes
    """
    fig, ax = plt.subplots(1, 1, figsize=(20, 4), dpi=300)
    fig.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_xlim(t_start - 0.1, t_end + 0.1)
    ax.set_ylim(-1.1, 1.1)
    ax.grid(color='white', linewidth=0.4, alpha=0.3, zorder=0)
    return fig, ax


def plot_LineCollection_on_axis(ax, x, y, colors='white', alphas=1, **kwargs):
    """
    Plot a LineCollection on a specified axis.

    ax - Axes object
    x - array of x points
    y - array of y points
    colors - array of colors for each point
    alphas - array of opacity for each point
    """
    lc = matplotlib.collections.LineCollection(make_segments(x, y), **kwargs)
    lc.set_colors(colors)
    lc.set_alpha(alphas)
    lc.set_capstyle('round')
    ax.add_collection(lc)
    return lc


def get_wave_with_variable_frequency(time, freq_array):
    """Returns a array sin(f(t) * t)"""
    dt = np.full_like(time, time[1] - time[0])
    phases = (freq_array * 2 * np.pi * dt).cumsum()
    return np.sin(phases), ((phases + np.pi) % (2 * np.pi) - np.pi)


phase_cmap = sns.color_palette('hls', as_cmap=True)


def angle2color(angle):
    return phase_cmap((angle % (2 * np.pi)) / (2 * np.pi))


if __name__ == '__main__':
    N_points = 5000
    t_start = 0
    t_end = 5

    time = np.linspace(t_start, t_end, N_points)   # Array of time points

    # Generating a random frequency modulation pattern
    generator = np.random.default_rng(seed=322)
    x_samples = np.linspace(t_start, t_end, 10)
    freq_samples = generator.random(x_samples.shape) * 6
    interpolation = interp1d(x_samples, freq_samples, kind='quadratic')

    freq = interpolation(time)

    wave, phase = get_wave_with_variable_frequency(time, freq)
    fig, ax = setup_time_axes()

    lc = plot_LineCollection_on_axis(
        ax,
        time,
        wave,
        angle2color(phase[:-1]),
        linewidths=6,
    )

    anim = animate_line_collections(
        [lc], fig, frame_downsampling=FRAME_DOWNSAMPLING
    )
    anim.save('temp.mp4')
