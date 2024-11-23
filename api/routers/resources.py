from fastapi import APIRouter, Depends, HTTPException
from api.controllers.resources import get_resources
from api.schemas.resources import ResourceResponse
from api.dependencies.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=ResourceResponse)
def get_all_resources(db: Session = Depends(get_db)):
    resources = get_resources(db=db)
    if not resources:
        raise HTTPException(status_code=404, detail="No resources found")
    return resources
