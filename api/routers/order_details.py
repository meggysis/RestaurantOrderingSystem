from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.controllers.order_details import create_order_detail, get_order_details, update_order_detail, delete_order_detail
from api.schemas.order_details import OrderDetailCreate, OrderDetailResponse
from api.dependencies.database import get_db
from typing import List

router = APIRouter()

@router.post("/{order_id}/details", response_model=OrderDetailResponse)
def create_order_detail_for_order(order_id: int, order_detail: OrderDetailCreate, db: Session = Depends(get_db)):
    return create_order_detail(db=db, order_detail=order_detail, order_id=order_id)

@router.get("/{order_id}/details", response_model=List[OrderDetailResponse])
def get_order_details_by_order(order_id: int, db: Session = Depends(get_db)):
    return get_order_details(db=db, order_id=order_id)

@router.put("/details/{order_detail_id}", response_model=OrderDetailResponse)
def update_order_detail_for_order(order_detail_id: int, order_detail: OrderDetailCreate, db: Session = Depends(get_db)):
    updated_order_detail = update_order_detail(db=db, order_detail_id=order_detail_id, order_detail=order_detail)
    if not updated_order_detail:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return updated_order_detail

@router.delete("/details/{order_detail_id}")
def delete_order_detail_for_order(order_detail_id: int, db: Session = Depends(get_db)):
    success = delete_order_detail(db=db, order_detail_id=order_detail_id)
    if not success:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return {"message": "Order Detail deleted successfully"}
