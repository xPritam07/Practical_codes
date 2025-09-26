import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV

# XOR input and expected output
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
expected_output = np.array([[0], [1], [1], [0]])

# Set random seed
tf.random.set_seed(42)

# Model builder function
def build_model(hidden_units=4, activation='relu', learning_rate=0.01):
    model = Sequential([
        Flatten(input_shape=(2,)),
        Dense(hidden_units, activation=activation),
        Dense(1, activation='sigmoid')
    ])
    model.compile(
        loss='binary_crossentropy',
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        metrics=['accuracy']
    )
    return model

# Wrap with KerasClassifier
model = KerasClassifier(build_fn=build_model, verbose=0)

# Define hyperparameter grid
param_grid = {
    'hidden_units': [2, 4, 8],
    'activation': ['relu', 'tanh'],
    'learning_rate': [0.01, 0.1],
    'epochs': [50, 100],
    'batch_size': [1, 2]
}

# Grid search
grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=2)
grid_result = grid.fit(inputs, expected_output)

# Best configuration
print("Best Parameters:", grid_result.best_params_)
print("Best Accuracy:", grid_result.best_score_)