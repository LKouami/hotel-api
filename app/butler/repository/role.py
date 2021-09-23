from datetime import datetime
from butler.models import models
from butler.schemas.role import Role
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def get_all(db: Session):
    roles = db.query(models.Role).all()
    return roles

def create(request: Role, db : Session ):
    new_role = models.Role(
        name = request.name, 
        created_at = datetime.utcnow(),
        )
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def destroy(id:int, db : Session):
    role = db.query(models.Role).filter(models.Role.id == id)
    if not role.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Role with the id : {id} is not found")
    role.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_one(id:int, db : Session):
    role = db.query(models.Role).filter(models.Role.id == id).first()
    if not role:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Role with the id : {id} is not found")
    return role

def update(id:int, request: Role, db: Session):
    role = db.query(models.Role).filter(models.Role.id == id) 
    if not role:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Role with the id : {id} is not found")
    role.update(  
        name = request.name, 
        modified_at = datetime.utcnow(),
        modified_by = request.modified_by,
        )
    db.commit()
    db.refresh()
    return 'updated successfully'