from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"
    
    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), index=True)  # ForeignKey to customers.customer_id
    order_date = Column(DateTime, default=datetime.utcnow)
    tracking_number = Column(String(255))  # Length specified
    order_status = Column(String(50), default="Pending")  # Length specified
    total_price = Column(Float)
    
    # Define relationships
    customer = relationship("Customer", back_populates="orders")  # Added back_populates for bidirectional relationship
    order_details = relationship("OrderDetail", back_populates="order")  # Assuming you have an OrderDetail model

