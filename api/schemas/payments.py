from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentCreate(BaseModel):
    order_id: int
    amount: float
    payment_method: str
    payment_time: datetime
    payment_status: str

class PaymentResponse(PaymentCreate):
    id: int

    class Config:
        orm_mode = True
