class dummy_model:
    def __init__(self):
        pass

    @property
    def name(self):
        return "dummy model"

    def fit(self, X, y):
        return 23

    def predict(self, X):
        return 24
