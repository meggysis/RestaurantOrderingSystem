from sqlalchemy.orm import Session
from api.models.promotions import Promotion
from api.schemas.promotions import PromotionApply, PromotionResponse

def get_promotions(db: Session) -> list[PromotionResponse]:
    return db.query(Promotion).all()

def apply_promotion(db: Session, promotion: PromotionApply) -> PromotionResponse:
    db_promotion = Promotion(**promotion.dict())
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion
