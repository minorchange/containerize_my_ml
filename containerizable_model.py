from pydantic import BaseModel


class PredictArgDummyModel(BaseModel):
    x: int


class ContextDummy(BaseModel):
    context_name: str
    context_values: list


class containerizable_model:
    def __init__(self):
        pass

    @property
    def name(self):
        return "dummy model"

    def fit(self, X: int, y: float):
        return 23

    def predict(self, x: PredictArgDummyModel):
        return 24

    def add_context(self, c: ContextDummy):
        pass

    def cache_model(self):
        pass
