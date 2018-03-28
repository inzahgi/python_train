#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
import matplotlib.pyplot as plt
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
    a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    print(a)

    L = [1,2,3,4,5,6]
    print("L = ", L)
    a = np.array(L)
    print("a = ", a)
    print(type(a), type(L))

    b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print("b = ", b)

    print("a.shape = ", a.shape)
    print("b.shape = ", b.shape)

    b.shape = 4, 3
    print("b = ",b)
    print("new b.shape = ", b.shape)

    b.shape = 2, -1
    print("b = ", b)
    print("b.shape = ", b.shape)

    c = b.reshape((4, -1))
    print("b = \n", b)
    print("c = \n", c)

    b[0][1] = 200
    print("b = \n", b)
    print("c = \n", c)

    print("a.dtype = ", a.dtype)
    print("b.dtype = ", b.dtype)

    d = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]],dtype=np.float)
    f = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]],dtype=np.complex)
    print("d = \n",d)
    print("f = \n",f)

    f = d.astype(np.int)
    print("f = \n", f)

    d.dtype = np.int
    print("d = \n", d)

## 2
    a = np.arange(1, 10, 0.5)
    print("a = ", a)

    b = np.linspace(1, 10, 10)
    print("b = ", b)

    c = np.linspace(1, 10, 10, endpoint=False)
    print("c = ", c)

    d = np.logspace(1,2,9, endpoint=True)
    print("d = ", d)

    f = np.logspace(0, 10, 11, endpoint=True, base=2)
    print("f = ", f)

    s = "abcdz"
    g = np.fromstring(s,dtype=np.int8)
    print("g = ", g)


## 3
## 3.1
    a = np.arange(10)
    print("a = ", a)

    print("a[3] = ", a[3])
    print("a[3:6] = ", a[3:6])
    print("a[:5] = ", a[:5])
    print("a[3:] = ", a[3:])
    print("a[1:9:2] = ", a[1:9:2])
    print("a[::-1] = ", a[::-1])
    a[1:4] = 10,20,30
    print("a = ", a)
    b = a[2:5]
    b[0] = 200
    print("a = ", a)



#### 3.2
#  3.2.1
    a = np.logspace(0, 9, 10, base=2)
    print("a = ", a)
    i = np.arange(0, 10, 2)
    print("i = ",i)
    b = a[i]
    print("b = ", b)
    b[2] = 1.6
    print("b = ", b)
    print("a = ", a)


## 3.2.2
    print("\n\n")
    a = np.random.rand(10)
    print("a = ", a)
    print(a > 0.5)
    b = a[a > 0.5]
    print("b = ", b)
    a[a > 0.5] = 0.5
    print("a = ", a)
    print("b = ", b)

## 3.3
    print("\n\n")
    a = np.arange(0, 60, 10)
    print("a = ", a)
    b = a.reshape((-1, 1))
    print("b = ", b)
    c = np.arange(6)
    print("c = ", c)
    f = b + c
    print("f = \n", f)
    a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    print("a = \n", a)
    print("a[[0,1,2], [2,3,4]] = ", a[[0,1,2],[2,3,4]])
    print("a[4, [2,3,4]] = ", a[4, [2,3,4]])
    print("a[4:,[2,3,4]] = ", a[4:,[2,3,4]])
    i = np.array([True, False, True, False, False, True])
    print("a[i] = ", a[i])
    print("a[i,3] = ", a[i,3])



###   4.1
    print("\n\n")
    for j in np.logspace(0,7,10):
        j = int(j)
        x = np.linspace(0, 10, j)
        start = time.clock()
        y = np.sin(x)
        t1 = time.clock() - start

        x = x.tolist()
        start = time.clock()
        for i, t in enumerate(x):
            x[i] = math.sin(t)
        t2 = time.clock() - start
        print(j, ":", t1, t2, t2/t1)


##  4.2
###   4.2.1
    print("\n\n")
    a = np.array((1,2,3,4,5,5,7,3,2,2,8,8))
    print("origin array = ", a)
    b = np.unique(a)
    print("after unique :", b)
    c = np.array(((1,2),(3,4),(5,6),(1,3),(3,4),(7,6)))
    print("two-dimensional array : \n", c)
    print("after unique : ", np.unique(c))


    r,i = np.split(c, (1,), axis=1)
    x = r + i*1j
    x = x[:,0] + c[:,1]*1j
    print("Into the imaginary :", x)
    print("after unique for imaginary : \n", np.unique(x))
    print(np.unique(x, return_index=True))
    idx = np.unique(x, return_index=True)[1]
    print("after unique for two-dimensional array : \n", c[idx])

    ##  use set to unique
    print("use set to unique :\n", np.array(list(set([tuple(t) for t in c]))))



### 4.3

    a = np.arange(1, 10).reshape((3,3))
    b = np.arange(11, 20).reshape((3,3))
    c = np.arange(101, 110).reshape((3,3))
    print("a = \n", a)
    print("b = \n", b)
    print("c = \n", c)
    print("axis = 0\n", np.stack((a,b,c), axis=0))
    print("axis = 1\n", np.stack((a,b,c), axis=1))
    print("axis = 2\n", np.stack((a,b,c), axis=2))

    a = np.arange(1, 10).reshape(3,3)
    print("a = \n", a)
    b = a + 10
    print("b = \n", b)
    print("a dot b = \n", np.dot(a, b))
    print("a*b = ", a*b)
    a = np.arange(1, 10)
    print("a = \n", a)
    b = np.arange(20, 25)
    print("b = \n", b)
    print(np.concatenate((a,b)))








