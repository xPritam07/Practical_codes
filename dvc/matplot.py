import matplotlib.pyplot as plt
import numpy as np 

x=np.linspace(0,10,100)
y=np.sin(x)
z=np.cos(x)

print(x[:10])
print(y[:10])

plt.scatter(x,y)
plt.xlabel('X values')
plt.ylabel("Y values")
plt.title("Sine Curve")
plt.grid(True)
plt.show()


plt.plot(x,y,color='red',linestyle="--")
plt.plot(x,z,color='blue',linestyle='-')
plt.xlabel('X values')
plt.ylabel("Transformed values")
plt.title("Trigonometric Curve Plotting")
plt.grid(True)
plt.show()

labels = ['Apple', 'Banana', 'Grapes', 'Orange', 'Mango']
sizes = [25, 15, 30, 10, 20]
explode = (0, 0, 0.1, 0, 0) 
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%',explode=explode, startangle=140, shadow=True)
plt.title("Fruit Distribution", fontsize=14)
plt.show()

categories = ["A", "B", "C", "D", "E"]
values = [23, 45, 56, 78, 34]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
plt.bar(categories, values, color=colors, edgecolor='black', linewidth=0.5)
plt.show()