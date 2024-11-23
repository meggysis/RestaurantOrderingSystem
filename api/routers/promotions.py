from fastapi import APIRouter, Depends, HTTPException
from api.controllers.promotions import get_promotions, apply_promotion
from api.schemas.promotions import PromotionResponse, PromotionApply
from api.dependencies.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=PromotionResponse)
def get_all_promotions(db: Session = Depends(get_db)):
    promotions = get_promotions(db=db)
    if not promotions:
        raise HTTPException(status_code=404, detail="No promotions found")
    return promotions

@router.post("/apply", response_model=PromotionResponse)
def apply_new_promotion(promotion: PromotionApply, db: Session = Depends(get_db)):
    applied_promotion = apply_promotion(db=db, promotion=promotion)
    if not applied_promotion:
        raise HTTPException(status_code=404, detail="Promotion could not be applied")
    return applied_promotion
