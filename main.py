from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app import models, schemas, crud, test2
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

models.Base.metadata.create_all(bind=test2.engine)

templates = Jinja2Templates(directory="templates")

@app.post("/couriers", response_model=schemas.Courier)
def create_courier(courier: schemas.CourierCreate, db: Session = Depends(test2.get_db)):
    return crud.create_courier(db=db, courier=courier)

@app.get("/couriers", response_model=List[schemas.Courier])
def read_couriers(db: Session = Depends(test2.get_db)):
    return crud.get_couriers(db)

@app.get("/couriers/{courier_id}", response_model=schemas.CourierDetail)
def read_courier(courier_id: str, db: Session = Depends(test2.get_db)):
    db_courier = crud.get_courier(db, courier_id=courier_id)
    if db_courier is None:
        raise HTTPException(status_code=404, detail="Courier not found")
    return db_courier

@app.post("/orders", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(test2.get_db)):
    db_order = crud.create_order(db=db, order=order)
    assigned_order = crud.assign_order_to_courier(db=db, order_id=db_order.id)
    if assigned_order is None:
        raise HTTPException(status_code=400, detail="No suitable courier found")
    return assigned_order


@app.get("/orders/{order_id}", response_model=schemas.Order)
def read_order(order_id: str, db: Session = Depends(test2.get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.post("/orders/{order_id}/complete", response_model=schemas.Order)
def complete_order(order_id: str, db: Session = Depends(test2.get_db)):
    db_order = crud.complete_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=400, detail="Order already completed or not found")
    return db_order

# Маршрут для отображения главной страницы
@app.get("/", response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
