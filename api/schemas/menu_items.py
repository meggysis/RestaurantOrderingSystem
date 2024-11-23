from pydantic import BaseModel
from typing import Optional

class MenuItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    availability: bool

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    availability: Optional[bool] = None

class MenuItemResponse(MenuItemCreate):
    id: int

    class Config:
        orm_mode = True
