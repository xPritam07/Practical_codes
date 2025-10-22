import tensorflow as tf
from keras import models, layers, optimizers, losses
import numpy as np

inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
actual_output = np.array([[0],[1],[1],[0]])

model = models.Sequential([
    layers.Flatten(input_shape=(2,)),
    layers.Dense(4, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer=optimizers.Adam(learning_rate=0.01),
    loss=losses.BinaryCrossentropy(),
    metrics=['accuracy']
)

model.fit(inputs, actual_output, epochs=50, verbose=1)
model.evaluate(inputs, actual_output)

print(np.round(model.predict(np.array([[0,0]]))))
print(model.summary())