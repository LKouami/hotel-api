from datetime import datetime
from butler.models import models
from butler.schemas.reservation import Reservation
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def get_all(db: Session):
    reservations = db.query(models.Reservation).all()
    return reservations

def create(request: Reservation, db : Session ):
    new_reservation = models.Reservation(
        begin_date = request.begin_date, 
        end_date = request.end_date, 
        comments = request.comments,  
        reservation_state = request.reservation_state,  
        client_id = request.client_id,  
        space_id = request.space_id,  
        reduction_id = request.reduction_id,   
        created_at = datetime.utcnow(),
        )
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation

def destroy(id:int, db : Session):
    reservation = db.query(models.Reservation).filter(models.Reservation.id == id)
    if not reservation.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Reservation with the id : {id} is not found")
    reservation.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_one(id:int, db : Session):
    reservation = db.query(models.Reservation).filter(models.Reservation.id == id).first()
    if not reservation:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Reservation with the id : {id} is not found")
    return reservation

def update(id:int, request: Reservation, db: Session):
    reservation = db.query(models.Reservation).filter(models.Reservation.id == id) 
    if not reservation:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Reservation with the id : {id} is not found")
    reservation.update(
        request.dict(exclude_unset= True)
        )
    db.commit()
    return 'updated successfully'