from butler import schemas
from butler.schemas.space import Space
from butler.schemas.user import User
from typing import List
from fastapi import APIRouter
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from fastapi import status
from butler.repository import space
from butler.oauth2 import oauth2
router = APIRouter(
    prefix='/space',
    tags=['Spaces']
) 

get_db = database.get_db
@router.get('/', response_model=List[Space] )
def get_all(db: Session = Depends(get_db)):
    return space.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Space, db : Session = Depends(get_db)):
    return space.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return space.destroy(id, db)

@router.get('/{id}', status_code=200 , response_model=Space)
def get_one(id:int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return space.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: Space, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return space.update(id, request, db)