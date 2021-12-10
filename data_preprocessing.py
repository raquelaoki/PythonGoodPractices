from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


def make_dataset(params):
    """Make the simulated dataset.
    Args:
        params: dictionary with parameters
    Returns:
        X_train, X_test, y_train, y_test datasets
    """
    X, y = make_classification(n_samples=params['n_samples'],
                               n_features=params['n_features'],
                               random_state=params['seed'],
                               n_classes=2,
                               n_clusters_per_class=1)
    return train_test_split(X, y, test_size=params.get('test_size', 0.33))
