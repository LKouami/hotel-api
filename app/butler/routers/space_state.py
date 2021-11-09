from butler.schemas.space_type import ShowSpaceType
from butler import schemas
from butler.schemas.space_state import SpaceState
from butler.schemas.user import User
from typing import List
from fastapi import APIRouter
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from fastapi import status
from butler.repository import space_state
from butler.oauth2 import oauth2
router = APIRouter(
    prefix='/space_state',
    tags=['SpaceStates']
) 

get_db = database.get_db
@router.get('/', response_model=List[ShowSpaceType] )
def get_all(db: Session = Depends(get_db)):
    return space_state.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: SpaceState, db : Session = Depends(get_db)):
    return space_state.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db)):
    return space_state.destroy(id, db)

@router.get('/{id}', status_code=200 , response_model=ShowSpaceType)
def get_one(id:int, db: Session = Depends(get_db)):
    return space_state.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: SpaceState, db: Session = Depends(get_db)):
    return space_state.update(id, request, db)