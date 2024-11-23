from fastapi import APIRouter, Depends, HTTPException
from api.controllers.orders import create_order, get_order, update_order, delete_order
from api.schemas.orders import OrderCreate, OrderUpdate, OrderResponse
from api.dependencies.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=OrderResponse)
def create_new_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db=db, order=order)

@router.get("/{order_id}", response_model=OrderResponse)
def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    order = get_order(db=db, order_id=order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=OrderResponse)
def update_existing_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    updated_order = update_order(db=db, order_id=order_id, order=order)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order

@router.delete("/{order_id}")
def delete_existing_order(order_id: int, db: Session = Depends(get_db)):
    success = delete_order(db=db, order_id=order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}
