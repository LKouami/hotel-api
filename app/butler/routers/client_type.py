from butler import schemas
from butler.schemas.client_type import ClientType
from butler.schemas.client_type import ShowClientType
from butler.schemas.user import User
from typing import List
from fastapi import APIRouter
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from fastapi import status
from butler.repository import client_type
from butler.oauth2 import oauth2
router = APIRouter(
    prefix='/client_type',
    tags=['ClientTypes']
) 

get_db = database.get_db
@router.get('/', response_model=List[ShowClientType] )
def get_all(db: Session = Depends(get_db)):
    return client_type.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: ClientType, db : Session = Depends(get_db)):
    return client_type.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db)):
    return client_type.destroy(id, db)

@router.get('/{id}', status_code=200 , response_model=ShowClientType)
def get_one(id:int, db: Session = Depends(get_db)):
    return client_type.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: ClientType, db: Session = Depends(get_db)):
    return client_type.update(id, request, db)