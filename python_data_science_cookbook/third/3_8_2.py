from sklearn.datasets import load_iris
from sklearn.preprocessing import Imputer
import numpy as np
import numpy.ma as ma

data = load_iris()
x = data['data']
y = data['target']

x_t = x.copy()
x_t[2,:] = np.repeat(0, x.shape[1])

imputer = Imputer(missing_values=0, strategy="mean")
x_imputed = imputer.fit_transform(x_t)

mask = np.zeros_like(x_t)
mask[2,:] = 1
x_t_m = ma.masked_array(x_t, mask)

print(np.mean(x_t_m, axis=0))
print(x_imputed[2,:])


