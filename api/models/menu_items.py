from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"
    
    menu_item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))  # Added length to the String type
    price = Column(Float)
    calories = Column(Integer)
    food_category = Column(String(100))  # Added length to the String type
    
    # Define the relationship with OrderDetail
    order_details = relationship("OrderDetail", back_populates="menu_item")
