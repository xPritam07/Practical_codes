import tensorflow as tf
from keras import layers, models, datasets
import numpy as np

(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

x_train = x_train.reshape(-1,28,28,1).astype('float32')/255.0
x_test = x_test.reshape(-1,28,28,1).astype('float32')/255.0

model = models.Sequential([
    layers.Conv2D(32, kernel_size=(3,3), input_shape=(28,28,1), activation='relu'),
    layers.MaxPool2D(pool_size=(2,2)),
    layers.Conv2D(64, activation='relu', kernel_size=(3,3)),
    layers.MaxPool2D(pool_size=(2,2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.fit(x_train, y_train, epochs=5, batch_size=32, verbose=1)

loss, acc = model.evaluate(x_test, y_test)

print(acc)

img = x_test[4]
import matplotlib.pyplot as plt
plt.imshow(img.squeeze(), cmap='grey')
plt.title('Input image')
plt.show()

pred = model.predict(np.expand_dims(img, axis=0), verbose=0)
print(f'Predicted image is {pred.argmax()}')