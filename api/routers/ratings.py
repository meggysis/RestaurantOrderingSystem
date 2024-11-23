from fastapi import APIRouter, Depends, HTTPException
from api.controllers.ratings import create_rating, get_rating_by_order, update_rating, delete_rating
from api.schemas.ratings import RatingCreate, RatingUpdate, RatingResponse
from api.dependencies.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=RatingResponse)
def create_new_rating(rating: RatingCreate, db: Session = Depends(get_db)):
    return create_rating(db=db, rating=rating)

@router.get("/{order_id}", response_model=RatingResponse)
def get_rating_for_order(order_id: int, db: Session = Depends(get_db)):
    rating = get_rating_by_order(db=db, order_id=order_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating

@router.put("/{order_id}", response_model=RatingResponse)
def update_existing_rating(order_id: int, rating: RatingUpdate, db: Session = Depends(get_db)):
    updated_rating = update_rating(db=db, order_id=order_id, rating=rating)
    if not updated_rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return updated_rating

@router.delete("/{order_id}")
def delete_existing_rating(order_id: int, db: Session = Depends(get_db)):
    success = delete_rating(db=db, order_id=order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Rating not found")
    return {"message": "Rating deleted successfully"}
