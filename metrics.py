# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 01:04:37 2023

@author: Casper
"""
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error, mean_squared_error

def mean_absolute(data_x,data_y):
    return np.mean(np.abs(data_x,data_y))

def mean_squared(data_x,data_y):
    return np.mean((data_x-data_y)**2)

def root_mean_squared (data_x,data_y): #yukardaki fonksiyonu çağırıp karekökünü aldık
    return np.sqrt(mean_squared(data_x, data_y))

data_x = np.linspace(0,1,100)
data_y = data_x + np.random.random(size=data_x.shape)/5

plt.plot(data_x,data_y,'.')
print('MAE',mean_absolute(data_x, data_y))
print('MSE',mean_squared(data_x, data_y))