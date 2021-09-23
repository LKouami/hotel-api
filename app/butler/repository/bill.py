from datetime import datetime
from butler.models import models
from butler.schemas.bill import Bill
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def get_all(db: Session):
    bills = db.query(models.Bill).all()
    return bills

def create(request: Bill, db : Session ):
    new_bill = models.Bill(
        b_date = request.b_date, 
        b_num = request.b_num, 
        client_id = request.client_id, 
        created_at = datetime.utcnow(),  
        user_id = request.user_id,
        )
    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)
    return new_bill

def destroy(id:int, db : Session):
    bill = db.query(models.Bill).filter(models.Bill.id == id)
    if not bill.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Bill with the id : {id} is not found")
    bill.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_one(id:int, db : Session):
    bill = db.query(models.Bill).filter(models.Bill.id == id).first()
    if not bill:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Bill with the id : {id} is not found")
    return bill

def update(id:int, request: Bill, db: Session):
    bill = db.query(models.Bill).filter(models.Bill.id == id) 
    if not bill:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Bill with the id : {id} is not found")
    bill.update(
        b_date = request.b_date, 
        b_num = request.b_num,
        client_id = request.client_id, 
        modified_at = datetime.utcnow(),
        modified_by = request.modified_by,
        )
    db.commit()
    return 'updated successfully'