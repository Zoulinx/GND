import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import pearsonr
import numpy as np
from PIL import Image

plt.rcParams['font.family'] = 'Times New Roman'
font = FontProperties()
font.set_family('Times New Roman')
font.set_size(12)


def draw_subplot(x, y, x_label, y_label, ax):
    pearson_r, _ = pearsonr(x, y)
    X = sm.add_constant(x)
    model = sm.OLS(y, X).fit()
    b0, b1 = model.params
    r_squared = model.rsquared
    sy = np.std(y, ddof=1)  # y_std

    data = pd.DataFrame({x_label: x, y_label: y})

    sampled_data = data.sample(frac=0.2, random_state=42)

    sns.set(style="darkgrid")

    sns.regplot(x=x_label, y=y_label, data=sampled_data,
                scatter_kws={'alpha': 0.3,
                             'color': 'green',
                             's': 5},
                line_kws={'color': 'orange',
                          'label': f'{y_label}'},
                ax=ax)

    ax.set_xlabel(x_label, fontsize=14)
    ax.set_ylabel('', fontsize=8)

    ax.legend(loc='upper left', prop=font)

    ax.text(0.95, 0.05,
            f'slope: {b1:.4f}\n'
            f'Std.y: {sy:.4f}\n'
            f'R²: {r_squared:.4f}\n'
            f'Pearson: {pearson_r:.4f}',
            transform=ax.transAxes, fontsize=14,
            verticalalignment='bottom',
            horizontalalignment='right',
            fontproperties=font)


def draw_multiple_plots(x, ys, x_label, y_labels):
    fig, axes = plt.subplots(1, 6, figsize=(20, 3))
    axes = axes.flatten()
    fig.subplots_adjust(hspace=0.15, wspace=0.2, bottom=0.15, top=0.98, left=0.05, right=0.98)

    for i, (y, y_label) in enumerate(zip(ys, y_labels)):
        draw_subplot(x, y, x_label, y_label, axes[i + 1])

    img = Image.open('')
    axes[0].imshow(img)
    axes[0].axis('off')

    plt.show()
    fig.savefig("", dpi=300)
