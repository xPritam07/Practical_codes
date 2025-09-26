import math

class LVQ:
    # Function to compute the winning vector by Euclidean distance
    def winner(self, weights, sample):
        D0, D1 = 0, 0
        for i in range(len(sample)):
            D0 += (sample[i] - weights[0][i]) ** 2
            D1 += (sample[i] - weights[1][i]) ** 2
        if D0 > D1:
            return 0
        else:
            return 1

    # Function to update the winning vector
    def update(self, weights, sample, J, alpha, actual):
        if actual == J:  # corrected condition
            for i in range(len(weights[J])):
                weights[J][i] = weights[J][i] + alpha * (sample[i] - weights[J][i])
        else:
            for i in range(len(weights[J])):
                weights[J][i] = weights[J][i] - alpha * (sample[i] - weights[J][i])


# Driver code
def main():
    # Training Samples (m, n) with their class vector
    X = [
        [0, 0, 1, 1],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
    ]
    Y = [0, 1, 0, 1, 1, 1]

    m, n = len(X), len(X[0])

    # weight initialization (take first two samples as initial weights)
    weights = []
    weights.append(X.pop(0))
    weights.append(X.pop(0))

    # remove corresponding labels
    m = m - 2
    Y.pop(0)
    Y.pop(0)

    # training
    ob = LVQ()
    epochs = 3
    alpha = 0.1

    for i in range(epochs):
        for j in range(m):
            # Sample selection
            T = X[j]
            # Compute winner
            J = ob.winner(weights, T)
            # Update weights
            ob.update(weights, T, J, alpha, Y[j])

    # classify new input sample
    T = [0, 0, 1, 0]
    J = ob.winner(weights, T)
    print("Sample T belongs to class:", J)
    print("Trained weights:", weights)


if __name__ == "__main__":
    main()
