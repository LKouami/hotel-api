from fastapi import APIRouter
from butler.schemas.user import User
from butler.schemas.user import ShowUser
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from butler.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db

@router.post('/', response_model = ShowUser)
def create_user(request: User, db : Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model = ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.get_user(id, db)
