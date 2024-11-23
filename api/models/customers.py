from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"
    
    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Added length to String
    email = Column(String(255), unique=True, index=True)  # Added length to String
    phone_number = Column(String(20))  # Added length for phone number
    address = Column(String(500))  # Added length for address
    
    # Define relationship to orders
    orders = relationship("Order", back_populates="customer")  # This links to the orders relationship in the Order model
