from copy import deepcopy
from test import test


# ToDo impalement train
def train(model, X_train, y_train, X_val=None, y_val=None, lr=0.01, verbosity=1):
    """
    Train a model on (X_train, y_val) using gradient descent
    :param model: network.NeuralNetwork object
    :param X_train: np.array of shape (n_samples, d)
    :param y_train: np.array of shape (n_samples,)
    :param X_val: (Optional) np.array of shape (n_samples, d)
    :param y_val: (Optional) np.array of shape (n_samples,)
    :param lr: learning rate to be used by gradient descent
    :param verbosity: control the verbosity of the training process
    :return: network.NeuralNetwork object, representing the trained neural network
    """
    trained_model = deepcopy(model)
    return trained_model
