from datetime import datetime
from butler.models import models
from butler.schemas.client_type import ClientType
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def get_all(db: Session):
    client_types = db.query(models.ClientType).all()
    return client_types

def create(request: ClientType, db : Session ):
    new_client_type = models.ClientType(
        name = request.name, 
        created_at = datetime.utcnow(),  
        user_id = request.user_id,
        )
    db.add(new_client_type)
    db.commit()
    db.refresh(new_client_type)
    return new_client_type

def destroy(id:int, db : Session):
    client_type = db.query(models.ClientType).filter(models.ClientType.id == id)
    if not client_type.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"ClientType with the id : {id} is not found")
    client_type.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_one(id:int, db : Session):
    client_type = db.query(models.ClientType).filter(models.ClientType.id == id).first()
    if not client_type:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"ClientType with the id : {id} is not found")
    return client_type

def update(id:int, request: ClientType, db: Session):
    client_type = db.query(models.ClientType).filter(models.ClientType.id == id) 
    if not client_type:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"ClientType with the id : {id} is not found")
    client_type.update(
        name = request.name,
        user_id = request.user_id,
        modified_at = datetime.utcnow(),
        modified_by = request.modified_by,
        )
    db.commit()
    return 'updated successfully'