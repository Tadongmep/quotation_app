from fastapi import FastAPI
from app.models.product import Product
from app.database import engine, Base
from app.routers import product

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(product.router)
