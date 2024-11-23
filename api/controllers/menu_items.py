from sqlalchemy.orm import Session
from api.models.menu_items import MenuItem
from api.schemas.menu_items import MenuItemCreate, MenuItemUpdate, MenuItemResponse

def create_menu_item(db: Session, menu_item: MenuItemCreate) -> MenuItemResponse:
    db_menu_item = MenuItem(**menu_item.dict())
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

def get_menu_item(db: Session, item_id: int) -> MenuItemResponse:
    return db.query(MenuItem).filter(MenuItem.id == item_id).first()

def update_menu_item(db: Session, item_id: int, menu_item: MenuItemUpdate) -> MenuItemResponse:
    db_menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if db_menu_item:
        for key, value in menu_item.dict(exclude_unset=True).items():
            setattr(db_menu_item, key, value)
        db.commit()
        db.refresh(db_menu_item)
        return db_menu_item
    return None

def delete_menu_item(db: Session, item_id: int) -> bool:
    db_menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if db_menu_item:
        db.delete(db_menu_item)
        db.commit()
        return True
    return False
