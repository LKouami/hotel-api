from butler.schemas.role import Role
from butler.schemas.role import ShowRole
from butler.schemas.user import User
from typing import List
from fastapi import APIRouter
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from fastapi import status
from butler.repository import role
from butler.oauth2 import oauth2
router = APIRouter(
    prefix='/role',
    tags=['Roles']
) 

get_db = database.get_db
@router.get('/', response_model=List[ShowRole] )
def get_all(db: Session = Depends(database.get_db)):
    return role.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Role, db : Session = Depends(database.get_db)):
    return role.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(database.get_db), current_user: User = Depends(oauth2.get_current_user)):
    return role.destroy(id, db)

@router.get('/{id}', status_code=200 , response_model=Role)
def get_one(id:int, db: Session = Depends(database.get_db), current_user: User = Depends(oauth2.get_current_user)):
    return role.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: Role, db: Session = Depends(database.get_db)):
    return role.update(id, request, db)