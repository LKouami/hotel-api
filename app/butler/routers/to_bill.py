from butler.schemas.user import User
from butler.schemas.to_bill import ToBill
from typing import List
from fastapi import APIRouter
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from fastapi import status
from butler.repository import to_bill
from butler.oauth2 import oauth2
router = APIRouter(
    prefix='/to_bill',
    tags=['ToBills']
) 

get_db = database.get_db
@router.get('/', response_model=List[ToBill] )
def get_all(db: Session = Depends(get_db)):
    return to_bill.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: ToBill, db : Session = Depends(get_db)):
    return to_bill.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return to_bill.destroy(id, db)

@router.get('/{id}', status_code=200 , response_model=ToBill)
def get_one(id:int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return to_bill.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: ToBill, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return to_bill.update(id, request, db)