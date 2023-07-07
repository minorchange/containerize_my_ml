from fastapi import FastAPI
from containerizable_model import containerizable_model
from find_model import find_and_load_model
from data_models import Context


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


@app.get("/get_context/{context_name}")
def get_context(context_name: str):
    c = m.get_context(context_name)
    return f"Current Context {context_name}: {c}"


@app.delete("/clear_context/{context_name}")
def clear_context(context_name: str):
    msg = m.clear_context(context_name)
    if msg is None:
        msg = ""
    return f"Context {context_name}  cleared. {msg}"
