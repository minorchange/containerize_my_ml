from fastapi import Body, FastAPI, Request
from find_model import find_and_load_model, inspect_model_instance


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


if hasattr(m, "set_context"):

    @app.put("/set_context")
    def set_context(c: m_info["setc_arg_type"]):
        c = m.set_context(c)
        return dict(c)


if hasattr(m, "get_context"):

    @app.get("/get_context")
    def get_context():
        c = m.get_context()
        return dict(c)


if hasattr(m, "reset_context"):

    @app.delete("/reset_context")
    def reset_context():
        c = m.reset_context()
        return dict(c)
