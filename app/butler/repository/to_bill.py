from datetime import datetime
from butler.models import models
from butler.schemas.to_bill import ToBill
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def get_all(db: Session):
    to_bills = db.query(models.ToBill).all()
    return to_bills

def create(request: ToBill, db : Session ):
    new_to_bill = models.ToBill(
        tb_date = request.tb_date, 
        tb_num = request.tb_num, 
        amount_to_be_paid = request.amount_to_be_paid,  
        client_id = request.client_id,  
        bill_id = request.bill_id,  
        reservation_id = request.reservation_id,
        created_at = datetime.utcnow(),  
        user_id = request.user_id,
        )
    db.add(new_to_bill)
    db.commit()
    db.refresh(new_to_bill)
    return new_to_bill

def destroy(id:int, db : Session):
    to_bill = db.query(models.ToBill).filter(models.ToBill.id == id)
    if not to_bill.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"ToBill with the id : {id} is not found")
    to_bill.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_one(id:int, db : Session):
    to_bill = db.query(models.ToBill).filter(models.ToBill.id == id).first()
    if not to_bill:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"ToBill with the id : {id} is not found")
    return to_bill

def update(id:int, request: ToBill, db: Session):
    to_bill = db.query(models.ToBill).filter(models.ToBill.id == id) 
    if not to_bill:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"ToBill with the id : {id} is not found")
    to_bill.update(
        tb_date = request.tb_date, 
        tb_num = request.tb_num, 
        amount_to_be_paid = request.amount_to_be_paid,  
        client_id = request.client_id,  
        bill_id = request.bill_id,  
        reservation_id = request.reservation_id,
        modified_at = datetime.utcnow(),
        modified_by = request.modified_by,
        )
    db.commit()
    return 'updated successfully'