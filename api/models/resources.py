from sqlalchemy import Column, Integer, String, Float
from ..dependencies.database import Base

class Resource(Base):
    __tablename__ = "resources"
    
    resource_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))  # Added length for name (e.g., 255 characters)
    amount = Column(Float)
    unit = Column(String(50))  # Added length for unit (e.g., 50 characters)
