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

##plt.figure(1)
fig,ax = plt.subplots()
ax.pcolor(x_, cmap=plt.cm.Greens, edgecolors='k')
ax.set_xticks(np.arange(0, x_.shape[1]) + 0.5)
ax.set_yticks(np.arange(0, x_.shape[0]) + 0.5)
ax.xaxis.tick_top()
ax.set_xticklabels(col_names, minor=False, fontsize=10)
ax.set_yticklabels(y_labels, minor=False, fontsize=10)



################################
x1 = x[0:50]
x2 = x[50:99]
x3 = x[100:149]

x1 = scale(x1, with_std=False)
x2 = scale(x2, with_std=False)
x3 = scale(x3, with_std=False)

fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
y_labels = range(1, 51)

ax1.set_xticks(np.arange(0, x.shape[1]) + 0.5)
ax1.set_yticks(np.arange(0, 50, 10))

ax1.xaxis.tick_bottom()
ax1.set_xticklabels(col_names, minor=False, fontsize=2)

ax1.pcolor(x1, cmap=plt.cm.Greens, edgecolors='k')
ax1.set_title(data['target_names'][0])

ax2.pcolor(x2, cmap=plt.cm.Greens, edgecolors='k')
ax2.set_title(data['target_names'][1])

ax3.pcolor(x1, cmap=plt.cm.Greens, edgecolors='k')
ax3.set_title(data['target_names'][2])

###################################
plt.show()

