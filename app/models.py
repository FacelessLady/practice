from sqlalchemy import Column, String, Integer, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from app.test2 import Base
import uuid

class Courier(Base):
    __tablename__ = "couriers"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    districts = Column(ARRAY(String))  # Используем массив строк для хранения районов
    avg_order_complete_time = Column(Integer, default=0)  # Среднее время выполнения заказа (в минутах)
    avg_day_orders = Column(Integer, default=0)  # Среднее количество завершенных заказов в день

    orders = relationship("Order", back_populates="courier")

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    district = Column(String)
    courier_id = Column(String, ForeignKey("couriers.id"), nullable=True)
    status = Column(Integer, default=1)  # 1 - в работе, 2 - завершен

    courier = relationship("Courier", back_populates="orders")
