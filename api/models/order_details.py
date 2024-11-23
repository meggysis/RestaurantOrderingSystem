from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"
    
    order_detail_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.menu_item_id"))
    quantity = Column(Integer, default=1)
    special_instructions = Column(String(500), nullable=True)  # Added length to String
    
    # Define relationships with Order and MenuItem
    order = relationship("Order", back_populates="order_details")
    menu_item = relationship("MenuItem", back_populates="order_details")
