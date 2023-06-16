from fastapi import FastAPI
from containerizable_model import containerizable_model
from find_model import find_and_load_model


app = FastAPI()


m = find_and_load_model()()


@app.get("/")
def read_root():
    return {f"Hi. I am {m.name}"}


@app.get("/predict/{param1}")
def predict(param1: str):
    y = m.predict(param1)

    return {"prediction": y}
