from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import product as product_schema
from app.crud import product as product_crud

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[product_schema.Product])
def read_products(db: Session = Depends(get_db)):
    return product_crud.get_products(db)

@router.post("/", response_model=product_schema.Product)
def create_new_product(product: product_schema.ProductCreate, db: Session = Depends(get_db)):
    return product_crud.create_product(db, product)
