from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int
    special_instructions: Optional[str] = None

class OrderCreate(BaseModel):
    customer_id: int
    items: List[OrderItem]  # List of order items (each item represents a menu item in the order)
    status: str  # The order's status, e.g., "Pending", "Completed"
    total_price: float  # Total price of the order
    order_time: datetime  # When the order was placed
    delivery_address: Optional[str] = None  # Optional address for delivery

class OrderUpdate(BaseModel):
    status: Optional[str] = None  # Optionally update the status
    total_price: Optional[float] = None  # Optionally update the total price
    delivery_address: Optional[str] = None  # Optionally update the delivery address

class OrderResponse(OrderCreate):
    id: int  # The ID of the order in the database

    class Config:
        orm_mode = True  # This is essential for automatic conversion between Pydantic models and SQLAlchemy models
