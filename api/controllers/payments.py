from sqlalchemy.orm import Session
from api.models.payments import Payment
from api.schemas.payments import PaymentCreate, PaymentResponse

def process_payment(db: Session, payment: PaymentCreate) -> PaymentResponse:
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_payment_status(db: Session, payment_id: int) -> PaymentResponse:
    return db.query(Payment).filter(Payment.id == payment_id).first()

def cancel_payment(db: Session, payment_id: int) -> bool:
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if db_payment:
        db.delete(db_payment)
        db.commit()
        return True
    return False
