from butler.schemas.client import ShowClient
from butler import schemas
from butler.schemas.client import Client
from butler.schemas.user import User
from typing import List
from fastapi import APIRouter
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from fastapi import status
from butler.repository import client
from butler.oauth2 import oauth2
router = APIRouter(
    prefix='/client',
    tags=['Clients']
) 

get_db = database.get_db
@router.get('/', response_model=List[ShowClient] )
def get_all(db: Session = Depends(get_db)):
    return client.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Client, db : Session = Depends(get_db)):
    return client.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db)):
    return client.destroy(id, db)

@router.get('/{id}', status_code=200 , response_model=ShowClient)
def get_one(id:int, db: Session = Depends(get_db)):
    return client.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: Client, db: Session = Depends(get_db)):
    return client.update(id, request, db)