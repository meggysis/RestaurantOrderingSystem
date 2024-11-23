from sqlalchemy import Column, Integer, String, Float, ForeignKey
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"
    
    payment_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    card_number = Column(String(16))  # Added length for card_number (16 is typical for credit cards)
    payment_status = Column(String(50))  # Optional: Added length for payment_status
    payment_type = Column(String(50))  # Optional: Added length for payment_type
    amount = Column(Float)
