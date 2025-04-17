from db import get_db
from fastapi import APIRouter, Depends, HTTPException
from models import OrderBody, OrderBase
from services.order_service import insertOrder, fetch_orders, fetch_order

router = APIRouter(prefix="/order", tags=["Order"])

@router.get("/", status_code=200, response_model=list[OrderBase])
def get_orders(db=Depends(get_db)):
    try:
        orders = fetch_orders(db)
        return orders
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 

@router.post("/", status_code=201)
def create_order(order: OrderBody, db=Depends(get_db)):
    try:
        insertOrder(db, order)
        return {
            "msg": "Order created",
            "order": order
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{order_id}", status_code=200, response_model=OrderBase)
def get_order(order_id: str, db=Depends(get_db)):
    try:
        order = fetch_order(db, order_id)
        return order
    except Exception as e:    
        raise HTTPException(status_code=400, detail=str(e))
