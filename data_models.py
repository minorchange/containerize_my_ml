from pydantic import BaseModel


class Context(BaseModel):
    context_name: str
    context_values: list
