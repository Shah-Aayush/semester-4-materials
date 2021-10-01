from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns


def pearson_correlation(arr1, arr2=None, rowvar=True):
    correlation = np.cov(arr1, arr2, rowvar)
    try:
        d = np.diag(correlation)
    except ValueError:
        return correlation / correlation
    stddev = np.sqrt(d.real)
    correlation /= stddev[:, None]
    correlation /= stddev[None, :]
    np.clip(correlation.real, -1, 1, out=correlation.real)
    return correlation


if __name__ == '__main__':
    array = np.random.rand(10, 12)
    print(array)
    correlation_array = pearson_correlation(array)
    print(correlation_array)
    fig = plt.figure(figsize=(10, 10))
    sns.heatmap(correlation_array, annot=True, fmt='0.2f', cmap='flare')
    plt.show()
