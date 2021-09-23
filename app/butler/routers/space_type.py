from butler import schemas
from butler.schemas.space_type import SpaceType
from butler.schemas.user import User
from typing import List
from fastapi import APIRouter
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from fastapi import status
from butler.repository import space_type
from butler.oauth2 import oauth2
router = APIRouter(
    prefix='/space_type',
    tags=['SpaceTypes']
) 

get_db = database.get_db
@router.get('/', response_model=List[SpaceType] )
def get_all(db: Session = Depends(get_db)):
    return space_type.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: SpaceType, db : Session = Depends(get_db)):
    return space_type.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return space_type.destroy(id, db)

@router.get('/{id}', status_code=200 , response_model=SpaceType)
def get_one(id:int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return space_type.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: SpaceType, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return space_type.update(id, request, db)