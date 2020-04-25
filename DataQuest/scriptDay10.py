from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

advertising = pd.read_csv('tvmarketing.csv')
# %matplotlib inline
# sns.pairplot(advertising, x_vars=['TV'], y_vars='Sales', height=7, aspect=0.7, kind='scatter')
X = advertising['TV']
X.head()
y = advertising['Sales']

y.head()
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, random_state= 100)
print(type(X_train))
print(type(X_test))
print(type(y_train))
print(type(y_test))

train_test_split

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

X_train = X_train[:, np.newaxis]
X_test = X_test[:, np.newaxis]

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
lr = LinearRegression()

lr.fit(X_train, y_train)
# Coefficient calculation
print(lr.intercept_)
print(lr.coef_)
# PREDICTION
y_pred = lr.predict(X_test)
type(y_pred)


c = [i for i in range(1,61,1)]

fig = plt.figure()
plt.plot(c,y_test, color = 'blue', linewidth = 2.5, linestyle = '-')
plt.plot(c,y_pred, color = 'red', linewidth = 2.5, linestyle = '-')
fig.suptitle('Actual and Predicted', fontsize = 20)
plt.xlabel('Index', fontsize = 18)
plt.ylabel('Sales', fontsize = 16)
# plt.show()

# Error terms
c = [i for i in range(1,61,1)]
fig = plt.figure()
plt.plot(c,y_test-y_pred, color = 'blue',linewidth = 2.3, linestyle = '-')
fig.suptitle('Error Terms', fontsize = 20)
plt.xlabel('Index', fontsize = 18)
plt.ylabel('ytest-ypred', fontsize = 16)
# plt.show()

from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test,y_pred)

print('Mean Square Error :' , mse)
print('r square value :',r_squared)

