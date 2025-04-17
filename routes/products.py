from db import get_db
from fastapi import APIRouter, Depends, HTTPException
from models import ProductBase, ProductBody
from services.product_service import insert_product, fetch_products, fetch_product

router = APIRouter(prefix="/product", tags=["Product"])

@router.get("/", status_code=200, response_model=list[ProductBase])
def get_products(db=Depends(get_db)):
    all_products: list[ProductBase] = fetch_products(db)
    return all_products

@router.post("/", status_code=201)
def create_product(product: ProductBody, db=Depends(get_db)):
    try:
        insert_product(db, product)
        return {
            "msg": "Product created",
            "product": product
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{product_id}", status_code=200, response_model=ProductBase)
def get_product(product_id: int, db=Depends(get_db)):
    single_product: ProductBase = fetch_product(db, product_id)
    return single_product