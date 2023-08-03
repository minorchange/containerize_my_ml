from fastapi import Body, FastAPI, Request
from containerizable_model import containerizable_model
from find_model import find_and_load_model, inspect_model_instance
from pydantic import BaseModel
import inspect


app = FastAPI()

m = find_and_load_model()()
m_info = inspect_model_instance(m)


@app.get("/")
def read_root():
    return {f"Hi. I am {m.name}"}


# @app.get("/predict/{x}")
# def predict(x: m_info["pred_arg_type"]):
#     y = m.predict(x)
#     return {"prediction": y}


@app.post("/predict")
def predict(x: m_info["pred_arg_type"]):
    y = m.predict(x)
    return y


@app.put("/add_context")
def add_context(c: m_info["addc_arg_type"]):
    m.add_context(c)
    return f"context {c.context_name} added."
