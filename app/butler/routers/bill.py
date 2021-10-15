from butler.schemas.bill import ShowBill
from butler import schemas
from butler.schemas.bill import Bill
from butler.schemas.user import User
from typing import List
from fastapi import APIRouter
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from fastapi import status
from butler.repository import bill
from butler.oauth2 import oauth2
router = APIRouter(
    prefix='/bill',
    tags=['Bills']
) 

get_db = database.get_db
@router.get('/', response_model=List[ShowBill] )
def get_all(db: Session = Depends(get_db)):
    return bill.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Bill, db : Session = Depends(get_db)):
    return bill.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db)):
    return bill.destroy(id, db)

@router.get('/{id}', status_code=200 , response_model=ShowBill)
def get_one(id:int, db: Session = Depends(get_db)):
    return bill.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: Bill, db: Session = Depends(get_db)):
    return bill.update(id, request, db)