from pydantic import BaseModel
from typing import Optional

class PromotionApply(BaseModel):
    order_id: int
    promotion_code: str

class PromotionResponse(PromotionApply):
    discount_amount: float

    class Config:
        orm_mode = True
