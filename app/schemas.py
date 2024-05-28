from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class CourierCreate(BaseModel):
    name: str
    districts: List[str]

class Courier(BaseModel):
    id: str
    name: str
    districts: List[str]

    model_config = ConfigDict(from_attributes=True)

class OrderCreate(BaseModel):
    name: str
    district: str

class Order(BaseModel):
    id: str
    name: str
    district: str
    courier_id: Optional[str]
    status: int

    model_config = ConfigDict(from_attributes=True)

class CourierDetail(BaseModel):
    id: str
    name: str
    active_order: Optional[Order]
    avg_order_complete_time: Optional[int]
    avg_day_orders: Optional[int]

    model_config = ConfigDict(from_attributes=True)
