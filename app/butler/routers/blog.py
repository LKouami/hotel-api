from typing import List
from fastapi import APIRouter
from butler.schemas import schemas
from butler.database import database
from fastapi.params import Depends 
from sqlalchemy.orm import Session
from fastapi import status
from butler.repository import blog
from butler.oauth2 import oauth2
router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
) 

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog] )
def get_all(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    return blog.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

@router.get('/{id}', status_code=200 , response_model=schemas.ShowBlog)
def get_one(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_one(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)