from sqlalchemy import Column, Integer, String, ForeignKey
from ..dependencies.database import Base

class Rating(Base):
    __tablename__ = "ratings"
    
    rating_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.menu_item_id"))
    score = Column(Integer)
    review_text = Column(String(500))  # Added length for review_text (e.g., 500 characters)
