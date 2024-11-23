from pydantic import BaseModel
from typing import Optional

class RatingCreate(BaseModel):
    order_id: int
    rating: int
    review: Optional[str] = None

class RatingUpdate(BaseModel):
    rating: Optional[int] = None
    review: Optional[str] = None

class RatingResponse(RatingCreate):
    id: int

    class Config:
        orm_mode = True
