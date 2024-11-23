from sqlalchemy.orm import Session
from api.models.ratings import Rating
from api.schemas.ratings import RatingCreate, RatingUpdate, RatingResponse

def create_rating(db: Session, rating: RatingCreate) -> RatingResponse:
    db_rating = Rating(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def get_rating_by_order(db: Session, order_id: int) -> RatingResponse:
    return db.query(Rating).filter(Rating.order_id == order_id).first()

def update_rating(db: Session, order_id: int, rating: RatingUpdate) -> RatingResponse:
    db_rating = db.query(Rating).filter(Rating.order_id == order_id).first()
    if db_rating:
        for key, value in rating.dict(exclude_unset=True).items():
            setattr(db_rating, key, value)
        db.commit()
        db.refresh(db_rating)
        return db_rating
    return None

def delete_rating(db: Session, order_id: int) -> bool:
    db_rating = db.query(Rating).filter(Rating.order_id == order_id).first()
    if db_rating:
        db.delete(db_rating)
        db.commit()
        return True
    return False
