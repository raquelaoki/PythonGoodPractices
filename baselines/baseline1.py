from sklearn import tree


class Baseline:
    """Baseline Method.
    This class implements the baseline method.
    input:
        none
    returns:
        predictions under self.predict()
    """

    def __init__(self):
        self.model = tree.DecisionTreeClassifier()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
