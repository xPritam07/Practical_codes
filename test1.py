import numpy as np
import matplotlib.pyplot as plt

x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[1]])

w1, w2, b = 0.0
lr = 0.01

for  _ in range(10):
    for i in range(4):
        z1 = 