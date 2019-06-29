from datasets.binary_dataset import ArtificialDataSet


if __name__ == "__main__":
    dataset = ArtificialDataSet(n_samples=100)
    dataset.visualize()

