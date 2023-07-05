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

# @app.put("/set_model_param/{param1}")
# def predict(param1: str):
#     y = m.predict(param1)

#     return {"prediction": y}


# class Item(BaseModel):
#     param_name: str | None
#     param_value: str | None
    

# @app.put("/set_model_param/{item_id}", response_model=Item)
# async def update_item(item_id: str, item: Item):
#     update_item_encoded = jsonable_encoder(item)
#     items[item_id] = update_item_encoded
#     return update_item_encoded