from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from .database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    amount = Column(Float, nullable=False)
    # We store the date so we can filter by Day, Week, or Month later
    timestamp = Column(DateTime, default=datetime.utcnow)

class Budget(Base):
    __tablename__ = "budget"

    id = Column(Integer, primary_key=True, index=True)
    # Allows you to set "Weekly" or "Monthly"
    limit_type = Column(String, default="Monthly") 
    amount = Column(Float, default=0.0)