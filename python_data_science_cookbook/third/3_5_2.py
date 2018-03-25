from sklearn.datasets import load_iris
from sklearn.preprocessing import scale
import numpy as np
import matplotlib.pyplot as plt

data = load_iris()
x = data['data']
y = data['target']
col_names = data['feature_names']

x = scale(x, with_std=False)
x_ = x[1:26]
y_labels = range(1, 26)

plt.close('all')

plt.figure(1)
fig,ax = plt.subplots()
ax.pcolor(x_, cmap=plt.cm.Greens, edgecolors='k')
ax.set_xticks(np.arange(0, x_.shape[1]) + 0.5)
ax.set_yticks(np.arange(0, x_.shape[0]) + 0.5)
ax.xaxis.tick_top()
ax.set_xticklabels(col_names, minor=False, fontsize=10)
ax.set_yticklabels(y_labels, minor=False, fontsize=10)



################################


###################################
plt.show()

