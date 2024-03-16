from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func

from .base import BaseTable

class Order(BaseTable):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String, unique=True, index=True)
    order_type = Column(String)
    status = Column(String)
    is_active = Column(Boolean, default=True)
    updated_on = Column(DateTime, default=func.now())