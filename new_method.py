from sklearn.linear_model import LogisticRegression


class NewMethod:
    """New Method.
    This class implements the new method.
    input:
        n_cluster: number of clusters
        random_state: random seed
    returns:
        predictions under self.predict()
    """

    def __init__(self):
        self.model = LogisticRegression()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
