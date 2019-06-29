import numpy as np
import matplotlib.pyplot as plt


class ArtificialDataSet:
    # ToDo Add noise to dataset
    # ToDo Implement other border fuctnions
    def __init__(self, n_samples, border_function='linear', dim=2):
        """
        Generates n_samples points of a data set, each sample in dim-dimensional vectorial space, and to each sample X
        we associate a label y such that y=1 if border_function(X) > 0, and 0 otherwise
        :param n_samples: (int) The number of samples to be generated
        :param dim: (int) the dimension of generated samples
        :param border_function: Border function takes as input an array of shape (d,) and returns a float.
               Possible values are 'linear', 'quadratic' ...
        :return:
        """
        self.n_samples = n_samples
        self.dim = dim
        self.border_function = border_function

        # Generation of samples and their labels
        self.X = np.random.uniform(low=-1, high=1, size=(n_samples, dim))

        if border_function == 'linear':
            self.y = (self.X.sum(axis=1) > 0).astype(np.uint8)

        else:
            raise NotImplementedError("Error Only linear border implemented for now")

    def __len__(self):
        return self.n_samples

    def __getitem__(self, item):
        return self.X[item], self.y[item]

    def get_train_validation_split(self, split_ratio=0.25):
        """
        Returns a tuple of 4 arrays representing train and validation samples and there labels
        :param split_ratio: the ration of samples to be used as validation
        :return: (X_train, y_train, X_val, y_val)
        """
        val_indexes = np.random.choice(np.arange(self.__len__()), size=int(self.__len__()*split_ratio))
        X_train = np.delete(self.X, val_indexes, axis=0)
        y_train = np.delete(self.y, val_indexes)

        X_val = self.X[val_indexes]
        y_val = self.y[val_indexes]

        return X_train, y_train, X_val, y_val

    def visualize(self):
        # ToDo Add the border line to the plot
        # ToDo add the possibility to save the data visualisation
        """
        Scatter plot of the dataset
        :return: None
        """
        if self.dim != 2:
            raise Exception("Can only be used for 2D dataset")

        plt.scatter(self.X[:, 0], self.X[:, 1], c=self.y)
        plt.show()



