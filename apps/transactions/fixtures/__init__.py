from apps.core.models import BaseModel


class ProductDataType(BaseModel):
    name: str
    price: float
