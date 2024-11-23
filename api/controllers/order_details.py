from sqlalchemy.orm import Session
from api.models.order_details import OrderDetail
from api.schemas.order_details import OrderDetailCreate
from api.models.orders import Order
from api.models.menu_items import MenuItem

def create_order_detail(db: Session, order_detail: OrderDetailCreate, order_id: int) -> OrderDetail:
    db_order_detail = OrderDetail(**order_detail.dict(), order_id=order_id)
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def get_order_details(db: Session, order_id: int):
    return db.query(OrderDetail).filter(OrderDetail.order_id == order_id).all()

def update_order_detail(db: Session, order_detail_id: int, order_detail: OrderDetailCreate) -> OrderDetail:
    db_order_detail = db.query(OrderDetail).filter(OrderDetail.order_detail_id == order_detail_id).first()
    if db_order_detail:
        for key, value in order_detail.dict(exclude_unset=True).items():
            setattr(db_order_detail, key, value)
        db.commit()
        db.refresh(db_order_detail)
        return db_order_detail
    return None

def delete_order_detail(db: Session, order_detail_id: int) -> bool:
    db_order_detail = db.query(OrderDetail).filter(OrderDetail.order_detail_id == order_detail_id).first()
    if db_order_detail:
        db.delete(db_order_detail)
        db.commit()
        return True
    return False
