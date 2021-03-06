#!/usr/bin/python
#-*-cpdong:utf-8 -*-

import operator
import functools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def c(n, k):
    return functools.reduce(operator.mul, range(n-k+1, n+1))/ functools.reduce(operator.mul, range(1, k+1))

def bagging(n, p):
    s = 0
    for i in range(n/2+1, n+1):
        s += c(n, i)*p ** i *(1-p) ** (n-i)
    return s


if __name__ == "__main__":
    n = 100
    x = np.arange(1, n, 2)
    ##x.astype(np.int64)
    y = np.empty_like(x, dtype=np.float)
    for i, t in enumerate(x):
        print("t = ", t)
        y[i] = bagging(t, 0.6)
        if t%10 == 9:
            print(t, " Correct rate of sub sampling :", y[i])
    mpl.rcParams['font.sans-serif']='SimHei'
    mpl.rcParams['axes.unicode_minus']=False
    plt.figure(facecolor='w')
    plt.plot(x, y, 'ro-', lw=2)
    plt.xlim(0, 100)
    plt.ylim(0.55, 1)
    plt.xlabel('sampling cnt', fontsize=16)
    plt.ylabel('correct rate', fontsize=16)
    plt.title('Bagging', fontsize=20)
    plt.grid(b=True)
    plt.show()
