from pydantic import BaseModel

# pydnactic models for type validationj
# BaseModels
class ProductBase(BaseModel):
    product_id: int
    name: str
    price_per_unit: float
    unit: str

class ItemBase(BaseModel):
    product_id: int
    product_name: str
    quantity: int  
    price: float 

class OrderBase(BaseModel):
    order_id: int
    customer_name: str
    items: list[ItemBase]
    total_price: float

# Body models
class ProductBody(BaseModel):
    name: str
    price_per_unit: float
    unit: str

class ItemBody(BaseModel):
    product_id: int
    quantity: int

class OrderBody(BaseModel):
    customer_name: str
    items: list[ItemBody]
    