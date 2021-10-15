from butler.schemas.reservation import ShowReservation
from butler import schemas
from butler.schemas.reservation import Reservation
from butler.schemas.user import User
from typing import List
from fastapi import APIRouter
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from fastapi import status
from butler.repository import reservation
from butler.oauth2 import oauth2
router = APIRouter(
    prefix='/reservation',
    tags=['Reservations']
) 

get_db = database.get_db
@router.get('/', response_model=List[ShowReservation] )
def get_all(db: Session = Depends(get_db)):
    return reservation.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Reservation, db : Session = Depends(get_db)):
    return reservation.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db)):
    return reservation.destroy(id, db)

@router.get('/{id}', status_code=200 , response_model=ShowReservation)
def get_one(id:int, db: Session = Depends(get_db)):
    return reservation.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: Reservation, db: Session = Depends(get_db)):
    return reservation.update(id, request, db)