import tensorflow as tf
from keras import models
from keras import layers
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

iris = load_iris()
X,y=iris.data, iris.target

scaler = StandardScaler()
X = scaler.fit_transform(X)
encoder = LabelEncoder()
y = encoder.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(X,y,random_state=42, test_size=0.2)

model = models.Sequential([
    layers.Dense(10, activation='relu', input_shape=(4,)),
    layers.Dense(3, activation='softmax')
])

model.compile(
    metrics=['accuracy'],
    loss='sparse_categorical_crossentropy',
    optimizer='adam'
)

model.fit(x_train, y_train, epochs=100, batch_size=16, verbose=1)
loss, acc = model.evaluate(x_test, y_test)

print(acc)