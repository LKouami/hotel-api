from datetime import datetime
from butler.models import models
from butler.schemas.space_type import SpaceType
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def get_all(db: Session):
    space_types = db.query(models.SpaceType).all()
    return space_types

def create(request: SpaceType, db : Session ):
    new_space_type = models.SpaceType(
        name = request.name, 
        created_at = datetime.utcnow(),  
        user_id = request.user_id,
        )
    db.add(new_space_type)
    db.commit()
    db.refresh(new_space_type)
    return new_space_type

def destroy(id:int, db : Session):
    space_type = db.query(models.SpaceType).filter(models.SpaceType.id == id)
    if not space_type.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"SpaceType with the id : {id} is not found")
    space_type.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_one(id:int, db : Session):
    space_type = db.query(models.SpaceType).filter(models.SpaceType.id == id).first()
    if not space_type:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"SpaceType with the id : {id} is not found")
    return space_type

def update(id:int, request: SpaceType, db: Session):
    space_type = db.query(models.SpaceType).filter(models.SpaceType.id == id) 
    if not space_type:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"SpaceType with the id : {id} is not found")
    space_type.update(
        name = request.name,
        modified_at = datetime.utcnow(),
        modified_by = request.modified_by,
        )
    db.commit()
    return 'updated successfully'