from fastapi import APIRouter, Depends, HTTPException
from api.controllers.menu_items import create_menu_item, get_menu_item, update_menu_item, delete_menu_item
from api.schemas.menu_items import MenuItemCreate, MenuItemUpdate, MenuItemResponse
from api.dependencies.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=MenuItemResponse)
def create_new_menu_item(menu_item: MenuItemCreate, db: Session = Depends(get_db)):
    return create_menu_item(db=db, menu_item=menu_item)

@router.get("/{item_id}", response_model=MenuItemResponse)
def get_menu_item_by_id(item_id: int, db: Session = Depends(get_db)):
    item = get_menu_item(db=db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item

@router.put("/{item_id}", response_model=MenuItemResponse)
def update_existing_menu_item(item_id: int, menu_item: MenuItemUpdate, db: Session = Depends(get_db)):
    updated_item = update_menu_item(db=db, item_id=item_id, menu_item=menu_item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return updated_item

@router.delete("/{item_id}")
def delete_existing_menu_item(item_id: int, db: Session = Depends(get_db)):
    success = delete_menu_item(db=db, item_id=item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return {"message": "Menu item deleted successfully"}
