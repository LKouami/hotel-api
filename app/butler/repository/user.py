from sqlalchemy.orm import Session
from butler.models import models
from butler.schemas.user import User
from fastapi import status, HTTPException
from datetime import datetime
from butler.hashing import hashing

def get_all(db: Session):
    users = db.query(models.User).all()
    return users

def create_user(request: User, db : Session):
    new_user = models.User(
        name=request.name, 
        email= request.email, 
        role_id= request.role_id,
        created_at = datetime.utcnow(), 
        password = hashing.Hash.bcrypt(request.password)
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def destroy(id:int, db : Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"User with the id : {id} is not found")
    user.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_one(id:int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"User with the id : {id} is not found")
    return user

def update(id:int, request: User, db: Session):
    user = db.query(models.User).filter(models.User.id == id) 
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"User with the id : {id} is not found")
    user.update(
        request.dict(exclude_unset= True)
        )
    db.commit()
    return 'updated successfully'