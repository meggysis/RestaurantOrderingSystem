from sqlalchemy.orm import Session
from api.models.orders import Order
from api.schemas.orders import OrderCreate, OrderUpdate, OrderResponse

def create_order(db: Session, order: OrderCreate) -> OrderResponse:
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int) -> OrderResponse:
    return db.query(Order).filter(Order.id == order_id).first()

def update_order(db: Session, order_id: int, order: OrderUpdate) -> OrderResponse:
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        for key, value in order.dict(exclude_unset=True).items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
        return db_order
    return None

def delete_order(db: Session, order_id: int) -> bool:
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
        return True
    return False
