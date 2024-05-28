from sqlalchemy.orm import Session
from app import models, schemas

# Создание курьера
def create_courier(db: Session, courier: schemas.CourierCreate):
    db_courier = models.Courier(name=courier.name, districts=courier.districts)
    db.add(db_courier)
    db.commit()
    db.refresh(db_courier)
    return db_courier

# Получение всех курьеров
def get_couriers(db: Session):
    return db.query(models.Courier).all()

# Получение курьера по ID
def get_courier(db: Session, courier_id: str):
    return db.query(models.Courier).filter(models.Courier.id == courier_id).first()

# Создание заказа
def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(name=order.name, district=order.district)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Получение заказа по ID
def get_order(db: Session, order_id: str):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

# Назначение заказа курьеру
def assign_order_to_courier(db: Session, order_id: str):
    order = get_order(db, order_id)
    couriers = db.query(models.Courier).all()
    for courier in couriers:
        if order.district in courier.districts:
            order.courier_id = courier.id
            db.commit()
            db.refresh(order)
            return order
    return None

# Завершение заказа
def complete_order(db: Session, order_id: str):
    order = get_order(db, order_id)
    if order and order.status == 1:
        order.status = 2
        db.commit()
        db.refresh(order)
        return order
    return None
