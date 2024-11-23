from pydantic import BaseModel
from typing import Optional

class OrderDetailBase(BaseModel):
    menu_item_id: int
    quantity: int
    special_instructions: Optional[str] = None

class OrderDetailCreate(OrderDetailBase):
    pass  # Use this model when creating order details

class OrderDetailResponse(OrderDetailBase):
    order_detail_id: int  # This will be returned after an order detail is created

    class Config:
        orm_mode = True  # This makes sure SQLAlchemy models can be automatically converted to Pydantic models
