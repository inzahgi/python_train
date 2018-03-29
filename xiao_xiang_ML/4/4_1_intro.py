#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from scipy.optimize import leastsq
from scipy import stats
import scipy.optimize as opt
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import CubicSpline
import math


def residual(t, x, y):
    return y-(t[0] * x ** 2 + t[1]*x + t[2])

def residual2(t, x, y):
    print(t[0], t[1])
    return y - (t[0]* np.sin(t[1]*x) + t[2])

def f(x):
    y = np.ones_like(x)
    i = x > 0
    y[i] = np.power(x[i], x[i])
    i = x < 0
    y[i] = np.power(-x[i], -x[i])
    return y

if __name__=="__main__":
#     a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
#     print(a)
#
#     L = [1,2,3,4,5,6]
#     print("L = ", L)
#     a = np.array(L)
#     print("a = ", a)
#     print(type(a), type(L))
#
#     b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#     print("b = ", b)
#
#     print("a.shape = ", a.shape)
#     print("b.shape = ", b.shape)
#
#     b.shape = 4, 3
#     print("b = ",b)
#     print("new b.shape = ", b.shape)
#
#     b.shape = 2, -1
#     print("b = ", b)
#     print("b.shape = ", b.shape)
#
#     c = b.reshape((4, -1))
#     print("b = \n", b)
#     print("c = \n", c)
#
#     b[0][1] = 200
#     print("b = \n", b)
#     print("c = \n", c)
#
#     print("a.dtype = ", a.dtype)
#     print("b.dtype = ", b.dtype)
#
#     d = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]],dtype=np.float)
#     f = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]],dtype=np.complex)
#     print("d = \n",d)
#     print("f = \n",f)
#
#     f = d.astype(np.int)
#     print("f = \n", f)
#
#     d.dtype = np.int
#     print("d = \n", d)
#
# ## 2
#     a = np.arange(1, 10, 0.5)
#     print("a = ", a)
#
#     b = np.linspace(1, 10, 10)
#     print("b = ", b)
#
#     c = np.linspace(1, 10, 10, endpoint=False)
#     print("c = ", c)
#
#     d = np.logspace(1,2,9, endpoint=True)
#     print("d = ", d)
#
#     f = np.logspace(0, 10, 11, endpoint=True, base=2)
#     print("f = ", f)
#
#     s = "abcdz"
#     g = np.fromstring(s,dtype=np.int8)
#     print("g = ", g)
#
#
# ## 3
# ## 3.1
#     a = np.arange(10)
#     print("a = ", a)
#
#     print("a[3] = ", a[3])
#     print("a[3:6] = ", a[3:6])
#     print("a[:5] = ", a[:5])
#     print("a[3:] = ", a[3:])
#     print("a[1:9:2] = ", a[1:9:2])
#     print("a[::-1] = ", a[::-1])
#     a[1:4] = 10,20,30
#     print("a = ", a)
#     b = a[2:5]
#     b[0] = 200
#     print("a = ", a)
#
#
#
# #### 3.2
# #  3.2.1
#     a = np.logspace(0, 9, 10, base=2)
#     print("a = ", a)
#     i = np.arange(0, 10, 2)
#     print("i = ",i)
#     b = a[i]
#     print("b = ", b)
#     b[2] = 1.6
#     print("b = ", b)
#     print("a = ", a)
#
#
# ## 3.2.2
#     print("\n\n")
#     a = np.random.rand(10)
#     print("a = ", a)
#     print(a > 0.5)
#     b = a[a > 0.5]
#     print("b = ", b)
#     a[a > 0.5] = 0.5
#     print("a = ", a)
#     print("b = ", b)
#
# ## 3.3
#     print("\n\n")
#     a = np.arange(0, 60, 10)
#     print("a = ", a)
#     b = a.reshape((-1, 1))
#     print("b = ", b)
#     c = np.arange(6)
#     print("c = ", c)
#     f = b + c
#     print("f = \n", f)
#     a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
#     print("a = \n", a)
#     print("a[[0,1,2], [2,3,4]] = ", a[[0,1,2],[2,3,4]])
#     print("a[4, [2,3,4]] = ", a[4, [2,3,4]])
#     print("a[4:,[2,3,4]] = ", a[4:,[2,3,4]])
#     i = np.array([True, False, True, False, False, True])
#     print("a[i] = ", a[i])
#     print("a[i,3] = ", a[i,3])
#
#

# ###   4.1
#     print("\n\n")
#     for j in np.logspace(0,7,10):
#         j = int(j)
#         x = np.linspace(0, 10, j)
#         start = time.clock()
#         y = np.sin(x)
#         t1 = time.clock() - start
#
#         x = x.tolist()
#         start = time.clock()
#         for i, t in enumerate(x):
#             x[i] = math.sin(t)
#         t2 = time.clock() - start
#         print(j, ":", t1, t2, t2/t1)
#
#
# ##  4.2
# ###   4.2.1
#     print("\n\n")
#     a = np.array((1,2,3,4,5,5,7,3,2,2,8,8))
#     print("origin array = ", a)
#     b = np.unique(a)
#     print("after unique :", b)
#     c = np.array(((1,2),(3,4),(5,6),(1,3),(3,4),(7,6)))
#     print("two-dimensional array : \n", c)
#     print("after unique : ", np.unique(c))
#
#
#     r,i = np.split(c, (1,), axis=1)
#     x = r + i*1j
#     x = x[:,0] + c[:,1]*1j
#     print("Into the imaginary :", x)
#     print("after unique for imaginary : \n", np.unique(x))
#     print(np.unique(x, return_index=True))
#     idx = np.unique(x, return_index=True)[1]
#     print("after unique for two-dimensional array : \n", c[idx])
#
#     ##  use set to unique
#     print("use set to unique :\n", np.array(list(set([tuple(t) for t in c]))))
#
#
#
# ### 4.3
#
#     a = np.arange(1, 10).reshape((3,3))
#     b = np.arange(11, 20).reshape((3,3))
#     c = np.arange(101, 110).reshape((3,3))
#     print("a = \n", a)
#     print("b = \n", b)
#     print("c = \n", c)
#     print("axis = 0\n", np.stack((a,b,c), axis=0))
#     print("axis = 1\n", np.stack((a,b,c), axis=1))
#     print("axis = 2\n", np.stack((a,b,c), axis=2))
#
#     a = np.arange(1, 10).reshape(3,3)
#     print("a = \n", a)
#     b = a + 10
#     print("b = \n", b)
#     print("a dot b = \n", np.dot(a, b))
#     print("a*b = ", a*b)
#     a = np.arange(1, 10)
#     print("a = \n", a)
#     b = np.arange(20, 25)
#     print("b = \n", b)
#     print(np.concatenate((a,b)))



###  5
###  5.1
    # mpl.rcParams['font.sans-serif']=['SimHei']
    # mpl.rcParams['axes.unicode_minus']=False
    # mu = 0
    # sigma = 1
    # x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 51)
    # y = np.exp(-(x-mu)**2/(2*sigma**2))/(math.sqrt(2 * math.pi)*sigma)
    # print("x.shape = ", x.shape)
    # print("x = \n", x)
    # print("y.shape = ", y.shape)
    # print("y = \n", y)
    # plt.figure(facecolor='w')
    # plt.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8)
    # plt.xlabel('X', fontsize=15)
    # plt.ylabel('Y', fontsize=15)
    # plt.title('Gaussian distribution', fontsize=18)
    # plt.grid(True)
    # plt.show()


## 5.2
    # x=np.array(np.linspace(start=-2,stop=3,num=1001,dtype=np.float))
    # y_logit = np.log(1 + np.exp(-x)) / math.log(2)
    # y_boost = np.exp(-x)
    # y_01 = x < 0
    # y_hinge = 1.0 -x
    # y_hinge[y_hinge < 0] = 0
    # plt.plot(x, y_logit, 'r-', label='Logistic Loss', linewidth=2)
    # plt.plot(x, y_01, 'g-',label='0/1 Loss', linewidth=2)
    # plt.plot(x, y_hinge, 'b-', label='Hinge Loss', linewidth=2)
    # plt.plot(x, y_boost, 'm-', label='AdaBoost Loss', linewidth=2)
    # plt.grid()
    # plt.legend(loc='upper right')
    # ###plt.savefig('1.png')
    # plt.show()
    #


### 5.3
    # x = np.linspace(-1.3, 1.3, 101)
    # y = f(x)
    # plt.plot(x, y, 'g-', label='x^x', linewidth=2)
    # plt.grid()
    # plt.legend(loc='upper left')
    # plt.show()



### 5.4
    # x = np.arange(1, 0, -0.001)
    # y = (-3 * x * np.log(x) + np.exp(-(40 *(x -1 /np.e)) ** 4) /25) /2
    # plt.figure(figsize=(5, 7),facecolor='w')
    # plt.plot(y, x, 'r-', linewidth=2)
    # plt.grid(True)
    # plt.title('breast line', fontsize=20)
    # ##plt.savefig('breast.png')
    # plt.show()


### 5.5
    # t = np.linspace(0, 2*np.pi, 100)
    # x = 16*np.sin(t)**3
    # y = 13*np.cos(t)-5*np.cos(2*t) - 2*np.cos(3*t)-np.cos(4*t)
    # plt.plot(x, y, 'r-', linewidth=2)
    # plt.grid(True)
    # plt.show()

### 5.6
    # t = np.linspace(0, 50, num=1000)
    # x = t*np.sin(t) + np.cos(t)
    # y = np.sin(t)-t*np.cos(t)
    # plt.plot(x, y, 'r-', linewidth=2)
    # plt.grid()
    # plt.show()


### bar
    # x = np.arange(0, 10, 0.1)
    # y = np.sin(x)
    # plt.bar(x, y,width=0.04, linewidth=0.2)
    # plt.plot(x, y, 'r-', linewidth=2)
    # plt.title('sin')
    # plt.xticks(rotation=-60)
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.grid()
    # plt.show()


### 6
### 6.1
    # x = np.random.rand(1000)
    # t = np.arange(len(x))
    # plt.hist(x, 30, color='m', alpha=0.1, label='uniform distribution')
    # ##plt.plot(t, x,'r-', label='uniform distribution')
    # plt.legend(loc='upper left')
    # plt.grid()
    # plt.show()

### 6.2
    # t = 1000
    # a = np.zeros(10000)
    # for i in range(t):
    #     a += np.random.uniform(-5, 5, 10000)
    # a /=t
    # plt.hist(a, bins=30, color='g', alpha=0.9, normed=True, label='')
    # plt.legend(loc='upper left')
    # plt.grid()
    # plt.show()


###  6.2.1
    # lamda = 10
    # p = stats.poisson(lamda)
    # y = p.rvs(size=1000)
    # mx=30
    # r=(0,mx)
    # bins=r[1]-r[0]
    # plt.figure(figsize=(10, 8), facecolor='w')
    # plt.subplot(121)
    # plt.hist(y, bins=bins,range=r,color='g', alpha=0.8, normed=True)
    # t=np.arange(0, mx+1)
    # plt.plot(t, p.pmf(t), 'ro-', lw=2)
    # plt.grid(True)
    #
    # N=1000
    # M=10000
    # plt.subplot(122)
    # a=np.zeros(M, dtype=np.float)
    # p = stats.poisson(lamda)
    # for i in np.arange(N):
    #     y=p.rvs(size=M)
    #     a+=y
    # a/=N
    # plt.hist(a, bins=20,color='g',alpha=0.8,normed=True)
    # plt.grid(b=True)
    # plt.show()


### 6.3
    # x=np.random.poisson(lam=5,size=10000)
    # print("x = ", x)
    # pillar = 15
    # a=plt.hist(x, bins=pillar,density=True, range=[0,pillar], color='g', alpha=0.5)
    # plt.grid()
    # plt.show()
    # print("a = ", a)
    # print("a[0].sum() = ", a[0].sum())


### 6.4
    # mu = 2
    # sigma=3
    # data=mu+sigma*np.random.randn(1000)
    # h=plt.hist(data,30,density=True,color='#a0a0ff')
    # x=h[1]
    # y=norm.pdf(x, loc=mu, scale=sigma)
    # plt.plot(x, y, 'r-', x, y, 'ro', linewidth=2, markersize=4)
    # plt.grid()
    # plt.show()


### 6.5   ????
    # mu = 2
    # sigma=3
    # data=mu+sigma*np.random.randn(1000)
    # h=plt.hist(data,30,density=True,color='#a0a0ff')
    # x=h[1]
    # rv = poisson(5)
    # M=10000
    # a = np.zeros(M, dtype=np.float)
    # x1 = a[1]
    # y1 = rv.pmf(x1)
    # itp = BarycentricInterpolator(x1,y1)
    # x2 = np.linspace(x.min(), x.max(), 50)
    # y2 = itp(x2)
    #
    # cs = CubicSpline.scipy.interpolate.CubicSpline(x1, y1)
    # plt.plot(x2,cs(x2),'m-',linewidth=5,label='CubicSpine')
    # plt.plot(x2,y2,'g-', linewidth=3,label='Barycentriclnterpolator')
    # plt.plot(x1, y1, 'r-', linewidth=1, label='Actural Value')
    # plt.legend(loc='upper right')
    # plt.grid()
    # plt.show()


### 7
    # x,y = np.ogrid[-3:3:100j, -3:3:100j]
    # u = np.linspace(-3, 3, 101)
    # x, y = np.meshgrid(u, u)
    # z = x*y*np.exp(-(x**2+y**2)/2)/math.sqrt(2*math.pi)
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=cm.coolwarm,linewidth=0.1)
    # ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=cm.Accent, linewidth=0.5)
    # plt.show()

# # cmaps = [('Perceptually Uniform Sequential',
# #           ['viridis', 'inferno', 'plasma', 'magma']),
# #          ('Sequential', ['Blues', 'BuGn', 'BuPu',
# #                          'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
# #                          'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
# #                          'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
# #          ('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool',
# #                              'copper', 'gist_heat', 'gray', 'hot',
# #                              'pink', 'spring', 'summer', 'winter']),
# #          ('Diverging', ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
# #                         'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
# #                         'seismic']),
# #          ('Qualitative', ['Accent', 'Dark2', 'Paired', 'Pastel1',
# #                           'Pastel2', 'Set1', 'Set2', 'Set3']),
# #          ('Miscellaneous', ['gist_earth', 'terrain', 'ocean', 'gist_stern',
# #                             'brg', 'CMRmap', 'cubehelix',
# #                             'gnuplot', 'gnuplot2', 'gist_ncar',
# #                             'nipy_spectral', 'jet', 'rainbow',
# #                             'gist_rainbow', 'hsv', 'flag', 'prism'])]

### 8.1
    # x = np.linspace(-2, 2, 50)
    # A, B, C = 2,3,-1
    # y = (A * x ** 2 + B * x + C) + np.random.rand(len(x))*0.75
    # t = leastsq(residual, [0,0,0], args=(x,y))
    # theta=t[0]
    # print("actual value : ", A, B, C)
    # print("'predicted value : ", theta)
    # y_hat = theta[0]*x ** 2 + theta[1]*x + theta[2]
    # plt.plot(x, y, 'r-', linewidth=2, label='Actual')
    # plt.plot(x, y_hat, 'g-', linewidth=2, label='Predict')
    # plt.legend(loc='upper left')
    # plt.grid()
    # plt.show()




### 8.2
    a = opt.fmin(f, 1)
    b = opt.fmin_cg(f, 1)
    c = opt.fmin_bfgs(f, 1)
    print(a, 1/a, math.e)
    print(b)
    print(c)









