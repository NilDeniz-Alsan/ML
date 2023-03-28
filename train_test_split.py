 # -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 22:58:44 2022

@author: Casper
"""

from sklearn.model_selection import KFold, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('data.xlsx',)

x_1 = df['x_1'].to_numpy()
x_2 = df['x_2'].to_numpy()
y_g = df['y_g'].to_numpy()

plt.plot(x_1, y_g)
plt.show()

x_1 = x_1.reshape(-1,1)
x_2 = x_2.reshape(-1,1)
y_g = y_g.reshape(-1,1)

print(np.shape(x_1))

x_concat = np.hstack((x_1,x_2))
#print(x_concat)

x_train_1, x_test_1, y_train_1, y_test_1 = train_test_split(x_1,y_g, test_size=0.2, shuffle=True,random_state=1)
x_train_2, x_test_2, y_train_2, y_test_2 = train_test_split(x_concat, y_g, test_size=0.2, shuffle=True, random_state=1)

print(np.shape(x_train_1), np.shape(x_test_1))
#print(x_train_1,y_train_1)

print(np.shape(x_train_2), np.shape(x_test_2))

print(x_train_1[0:2])
print(x_train_2[0:2])


linear = LinearRegression().fit(x_train_1, y_train_1)
y_test_predict = linear.predict(x_test_1)

print('MAE', mean_absolute_error(y_test_1, y_test_predict))
print('MSE', mean_squared_error(y_test_1, y_test_predict))

plt.plot(x_test_1, y_test_1, '.',label='test')
plt.plot(x_test_1, y_test_predict, '.',label='predict')
plt.legend()
plt.show()


linear = LinearRegression().fit(x_train_2, y_train_2)
y_test_predict = linear.predict(x_test_2)

print('MAE', mean_absolute_error(y_test_2, y_test_predict))
print('MSE', mean_squared_error(y_test_2, y_test_predict))

#plt.plot(x_test_2, y_test_2, '.',label='test')
#plt.plot(x_test_2, y_test_predict, '.',label='predict')
#plt.legend()
#plt.show()


"""
def get_gaussian(data):
    return np.exp(-data**2)

linear = LinearRegression().fit(get_gaussian(x_train_1), y_train_1)
y_test_predict = linear.predict(get_gaussian(x_test_1))

print('MAE', mean_absolute_error(y_test_1, y_test_predict))
print('MSE', mean_squared_error(y_test_1, y_test_predict))

plt.plot(x_test_1, y_test_1, '.',label='test')
plt.plot(x_test_1, y_test_predict, '.',label='predict')
plt.legend()
plt.show()
"""




