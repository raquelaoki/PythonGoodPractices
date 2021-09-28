from sklearn import tree


def _help_with_something():
    print("I'm only used inside the class")


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
        _help_with_something()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
