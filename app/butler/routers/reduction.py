from butler.schemas.reduction import ShowReduction
from butler import schemas
from butler.schemas.reduction import Reduction
from butler.schemas.user import User
from typing import List
from fastapi import APIRouter
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from fastapi import status
from butler.repository import reduction
from butler.oauth2 import oauth2
router = APIRouter(
    prefix='/reduction',
    tags=['Reductions']
) 

get_db = database.get_db
@router.get('/', response_model=List[ShowReduction] )
def get_all(db: Session = Depends(get_db)):
    return reduction.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Reduction, db : Session = Depends(get_db)):
    return reduction.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return reduction.destroy(id, db)

@router.get('/{id}', status_code=200 , response_model=ShowReduction)
def get_one(id:int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return reduction.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: Reduction, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return reduction.update(id, request, db)