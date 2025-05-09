from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    unit: str = "Chiếc"
    category: str | None = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    product_id: int

    class Config:
        orm_mode = True
