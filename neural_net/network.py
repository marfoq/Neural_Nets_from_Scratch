import numpy as np


class NeuralNetwork:
    def __init__(self, input_dim, hidden_dim=10, output_dim=1):
        # ToDo random initialisation of the wieghts instead of zero initialisation to break symmetry
        """
        Neural netwok object, with one hidden layer
        :param input_dim: The dimension of the input to be considered by the network
        :param hidden_dim: Number on neurons in the hidden layer
        :param output_dim: the dimension of the output
        """
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim

        # Weight Initialisation
        self.W1 = np.zeros((hidden_dim, input_dim))  # Weights of the hidden layer
        self.b1 = np.zeros(hidden_dim)  # Bias of the hidden layer

        self.W2 = np.zeros((output_dim, hidden_dim))  # Weights of the output layer
        self.b2 = np.zeros(output_dim)  # Bias of the output layer

    def forward_propagate(self, x):
        pass

    def backward_propagate(self, x):
        pass


