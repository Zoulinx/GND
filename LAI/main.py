import numpy as np
from scipy.stats import norm, pearsonr
import statsmodels.api as sm
from osgeo import gdal
from draw import draw_multiple_plots


def sr(red, nir):
    return nir / red


def ndvi(red, nir):
    return (nir - red) / (nir + red)


def mndvi(red, nir):
    sigma1 = np.std(nir, ddof=1)
    sigma2 = np.std(red, ddof=1)
    a1 = 0.2146 / (sigma1 ** 2)
    a2 = 0.2146 / (sigma2 ** 2)
    lamda = a1 / a2
    c = np.sqrt(lamda)
    print(1 / c)
    return (c * nir - red) / (c * nir + red)


def kndvi_naive(red, nir):
    return np.tanh((ndvi(red, nir)) ** 2)


def kndvi_rbf(red, nir):
    sigma = np.average(nir - red)
    return np.tanh(((nir - red) / (2 * sigma)) ** 2)


def gnd(red, nir):
    rvi = nir / red
    mu, std = norm.fit(rvi)
    print(mu)
    return (rvi - mu) / (rvi + mu)


def gen_sr(cover, num):
    if cover == 'all':
        # All cases of vegetation coverage are simulated using a uniform distribution.
        SR_sim = np.random.uniform(1.85, 19, num)
    elif cover == 'low':
        # Situations with low vegetation coverage are simulated using a normal distribution.
        SR_sim = np.random.normal(2.425, 0.575, num)
    elif cover == 'median':
        # Situations with median vegetation coverage are simulated using a normal distribution.
        SR_sim = np.random.normal(4.33, 1.33, num)
    elif cover == 'high':
        # Situations with high vegetation coverage are simulated using a normal distribution.
        SR_sim = np.random.normal(12.33, 6.67, num)
    else:
        raise Exception("press cover in [all, high, median, low]")
    return SR_sim


def get_stat(x, y):
    pearson_r, _ = pearsonr(x, y)  # Pearson coefficient

    X = sm.add_constant(x)
    model = sm.OLS(y, X).fit()
    b0, b1 = model.params  # intercept b0 and regression coefficient b1

    r_squared = model.rsquared  # R²

    sx = np.std(x, ddof=1)  # x_std
    sy = np.std(y, ddof=1)  # y_std

    beta = b1 * (sy / sx)  # beta coefficient

    print(f"Pearson: {pearson_r:.4f}")
    print(f"regression: {b1:.4f}")
    print(f"x_std: {sx:.4f}")
    print(f"y_std: {sy:.4f}")
    print(f"std_ratio: {(sy / sx):.4f}")
    print(f"R²: {r_squared:.4f}")
    print(f"Beta: {beta:.4f}")


def print_result(dv, red, nir):
    print('---ndvi---')
    get_stat(dv, ndvi(red, nir))
    print('---kndvi_naive---')
    get_stat(dv, kndvi_naive(red, nir))
    print('---kndvi_rbf---')
    get_stat(dv, kndvi_rbf(red, nir))
    print('---mndvi---')
    get_stat(dv, mndvi(red, nir))
    print('---gnd---')
    get_stat(dv, gnd(red, nir))


def draw_result(dv, red, nir):
    x_label = 'LAI'
    y_labels = ['NDVI', 'KNDVI_naive', 'KNDVI_rbf', 'MNDVI',
                'GND']
    draw_multiple_plots(dv,
                        [ndvi(red, nir), kndvi_naive(red, nir), kndvi_rbf(red, nir), mndvi(red, nir), gnd(red, nir)],
                        x_label, y_labels)


if __name__ == '__main__':
    red_path = 'data/Sentinel_RED/Point15.tif'
    nir_path = 'data/Sentinel_NIR/Point15.tif'
    lai_path = 'data/LAI/LAI_Point15.dat'

    red_data = gdal.Open(red_path).ReadAsArray().flatten()
    nir_data = gdal.Open(nir_path).ReadAsArray().flatten()
    lai_data = gdal.Open(lai_path).ReadAsArray().flatten()

    draw_result(lai_data, red_data, nir_data)
