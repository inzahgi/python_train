from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

data = load_iris()
x = data['data']
plt.close("all")

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.boxplot(x)
ax.set_xticklabels(data['feature_names'])


######################
y = data['target']
class_labels = data['target_names']

fig = plt.figure(2, figsize=(18, 10))
sub_plt_count = 321
for t in range(0, 3):
    ax = fig.add_subplot(sub_plt_count)
    y_index = np.where(y == t)[0]
    x_ = x[y_index, :]
    ax.boxplot(x_)
    ax.set_title(class_labels[t])
    ax.set_xticklabels(data['feature_names'])
    sub_plt_count += 1


##########################

plt.show()