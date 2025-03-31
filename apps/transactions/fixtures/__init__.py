from pydantic import BaseModel


class ProductDataType(BaseModel):
    name: str
    price: float
