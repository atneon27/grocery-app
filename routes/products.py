from db import get_db
from fastapi import APIRouter, Depends, HTTPException
from models import ProductBase, ProductBody
from services.product_service import insert_product, fetch_products, fetch_product, find_and_update_product

router = APIRouter(prefix="/product", tags=["Product"])

@router.get(
    "/", 
    status_code=200, 
    response_model=list[ProductBase],
    description="Get all existing products"
)
def get_products(db=Depends(get_db)):
    all_products: list[ProductBase] = fetch_products(db)
    return all_products

@router.post(
    "/", 
    status_code=201,
    description="Create a new product"
)
def create_product(product: ProductBody, db=Depends(get_db)):
    try:
        insert_product(db, product)
        return {
            "msg": "Product created",
            "product": product
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/{product_id}", 
    status_code=200, 
    response_model=ProductBase,
    description="Get a single product"
)
def get_product(product_id: int, db=Depends(get_db)):
    single_product: ProductBase = fetch_product(db, product_id)
    return single_product

@router.put(
    "/{product_id}", 
    status_code=200,
    description="Update a product"
)
def update_product(product_id: int, product: ProductBody, db=Depends(get_db)):
    try:
        find_and_update_product(db, product_id, product)
        return {
            "msg": "Product updated",
            "product": product
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))