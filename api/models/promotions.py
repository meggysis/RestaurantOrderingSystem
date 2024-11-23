from sqlalchemy import Column, Integer, String, DateTime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"
    
    promotion_id = Column(Integer, primary_key=True, index=True)
    promotion_code = Column(String(100))  # Added length for promotion_code (e.g., 100 characters)
    expiration_date = Column(DateTime)
