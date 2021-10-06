from typing import List
from fastapi import APIRouter
from starlette.status import HTTP_200_OK
from butler.schemas.user import User
from butler.schemas.user import ShowUser
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from butler.repository import user
from fastapi import status
from butler.oauth2 import oauth2

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db

@router.get('/', response_model=List[User] )
def get_all(db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return user.get_all(db)
    
@router.post('/', response_model = ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: User, db : Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return user.create_user(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return user.destroy(id, db)

@router.get('/{id}', response_model = ShowUser, status_code= HTTP_200_OK)
def get_user(id:int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return user.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: User, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return user.update(id, request, db)
