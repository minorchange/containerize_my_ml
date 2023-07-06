from fastapi import FastAPI
from containerizable_model import containerizable_model
from find_model import find_and_load_model
from pydantic import BaseModel

class Context(BaseModel):
    context_name: str
    context_values: list



app = FastAPI()

m = find_and_load_model()()

@app.get("/")
def read_root():
    return {f"Hi. I am {m.name}"}

@app.get("/predict/{param1}")
def predict(param1: str):
    y = m.predict(param1)
    return {"prediction": y}

@app.put("/add_context")
def add_context(c: Context):
    m.add_context(c)
    return f"context {c.context_name} added."