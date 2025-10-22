import numpy as np
from sklearn.datasets import load_iris

class Perceptron:
    def __init__(self, n_iter, learning_rate):
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.weights = None
        self.bias = None
    
    def activation(self, x):
        return 1 if x>0 else 0
    
    def fit(self, X,y):
        n_samples, n_features =X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iter):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights)+self.bias
                y_predicted = self.activation(linear_output)
                update = self.learning_rate * (y[idx] - y_predicted)
                self.weights += self.learning_rate*update
                self.bias += update

    def predict(self, X):
        if X.ndim == 1:
            linear_output = [np.dot(X,self.weights) + self.bias]
        else:
            linear_output = np.dot(X, self.weights)+ self.bias

        y_predicted = np.array([self.activation(val) for val in linear_output])
        return y_predicted
    
if __name__ == "__main__":
    iris=load_iris()
    X = iris.data
    y = iris.target
    y = np.where(y==0,0,1)

    p = Perceptron(learning_rate=0.01, n_iter=10)
    p.fit(X=X,y=y)
    predictions = p.predict(X)
    print(predictions)
