from sqlalchemy.orm import Session
from api.models.resources import Resource
from api.schemas.resources import ResourceResponse

def get_resources(db: Session) -> list[ResourceResponse]:
    return db.query(Resource).all()
