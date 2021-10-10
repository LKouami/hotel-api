from datetime import datetime
from butler.models import models
from butler.schemas.space import Space
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def get_all(db: Session):
    spaces = db.query(models.Space).all()
    return spaces

def create(request: Space, db : Session ):
    new_space = models.Space(
        name = request.name, 
        location = request.location, 
        price = request.price,  
        comments = request.comments,  
        created_at = datetime.utcnow(),  
        user_id = request.user_id,
        space_type_id = request.space_type_id,
        space_state_id = request.user_id,
        )
    db.add(new_space)
    db.commit()
    db.refresh(new_space)
    return new_space

def destroy(id:int, db : Session):
    space = db.query(models.Space).filter(models.Space.id == id)
    if not space.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Space with the id : {id} is not found")
    space.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_one(id:int, db : Session):
    space = db.query(models.Space).filter(models.Space.id == id).first()
    if not space:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Space with the id : {id} is not found")
    return space

def update(id:int, request: Space, db: Session):
    space = db.query(models.Space).filter(models.Space.id == id) 
    if not space:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Space with the id : {id} is not found")
    space.update(
        request.dict(exclude_unset= True)
        )
    db.commit()
    return 'updated successfully'