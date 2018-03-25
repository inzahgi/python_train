from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import itertools

data = load_iris()
x = data['data']
y = data['target']
col_names = data['feature_names']

plt.close('all')
plt.figure(1)
subplot_start = 321
col_numbers = range(0, 4)
col_pairs = itertools.combinations(col_numbers, 2)
plt.subplots_adjust(wspace = 0.5)

for col_pairs in col_pairs:
    plt.subplot(subplot_start)
    plt.scatter(x[:,col_pairs[0]], x[:, col_pairs[1]], c=y)
    plt.xlabel(col_names[col_pairs[0]])
    plt.ylabel(col_names[col_pairs[1]])
    subplot_start += 1

plt.show()


