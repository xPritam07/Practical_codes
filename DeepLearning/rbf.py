import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def rbf(x,c,gamma=0.1):
    return np.exp(-gamma*(x-c)**2)

time = np.array([6,9,12,15,18,21]).reshape(-1,1)
temp = np.array([15,20,30,32,25,18])

centers = time.flatten()
gamma = 0.1

x_rbf = np.zeros((len(time),len(centers)))
for i, c in enumerate(centers):
    x_rbf[:,i] = rbf(time.flatten(), c, gamma)

model = LinearRegression()
model.fit(x_rbf, temp)

time_test = np.linspace(0,24,100)
x_rbf_test = np.zeros((len(time_test), len(centers)))
for i, c in enumerate(centers):
    x_rbf_test[:,i]=rbf(time_test.flatten(), c, gamma)

temp_pred = model.predict(x_rbf_test)

plt.scatter(time, temp, color='red', label='Actual')
plt.plot(time_test, temp_pred, color='blue', label='Predictions')
plt.show()