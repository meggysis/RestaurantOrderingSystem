from fastapi import APIRouter, Depends, HTTPException
from api.controllers.payments import process_payment, get_payment_status, cancel_payment
from api.schemas.payments import PaymentCreate, PaymentResponse
from api.dependencies.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=PaymentResponse)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return process_payment(db=db, payment=payment)

@router.get("/{payment_id}", response_model=PaymentResponse)
def get_payment_by_id(payment_id: int, db: Session = Depends(get_db)):
    payment = get_payment_status(db=db, payment_id=payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.delete("/{payment_id}")
def cancel_payment_transaction(payment_id: int, db: Session = Depends(get_db)):
    success = cancel_payment(db=db, payment_id=payment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"message": "Payment cancelled successfully"}
