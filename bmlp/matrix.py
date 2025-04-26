import numpy as np 

a=np.array([[2,3,4],
            [4,2,6],
            [6,7,8]])

b=np.array([[5,2,7],
            [8,3,9],
            [1,4,9]])

mat_add = np.add(a,b)
print("Matrix addition :\n",mat_add)

mat_sub = np.subtract(a,b)
print("Matrix subtraction :\n",mat_sub)

c=int(input("Enter any scaler valeu: "))
scaler_mul = c * a
print("Scaler multiplication:\n",scaler_mul)

mat_mul = np.matmul(a,b)
print("Matrix multiplication :\n",mat_mul)

mat_div = a/b
print("Elementwise division :\n",mat_div)