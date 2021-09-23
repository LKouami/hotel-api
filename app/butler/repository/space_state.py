from datetime import datetime
from butler.models import models
from butler.schemas.space_state import SpaceState
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def get_all(db: Session):
    space_states = db.query(models.SpaceState).all()
    return space_states

def create(request: SpaceState, db : Session ):
    new_space_state = models.SpaceState(
        name = request.name,  
        created_at = datetime.utcnow(),  
        user_id = request.user_id,
        )
    db.add(new_space_state)
    db.commit()
    db.refresh(new_space_state)
    return new_space_state

def destroy(id:int, db : Session):
    space_state = db.query(models.SpaceState).filter(models.SpaceState.id == id)
    if not space_state.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"SpaceState with the id : {id} is not found")
    space_state.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_one(id:int, db : Session):
    space_state = db.query(models.SpaceState).filter(models.SpaceState.id == id).first()
    if not space_state:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"SpaceState with the id : {id} is not found")
    return space_state

def update(id:int, request: SpaceState, db: Session):
    space_state = db.query(models.SpaceState).filter(models.SpaceState.id == id) 
    if not space_state:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"SpaceState with the id : {id} is not found")
    space_state.update(
        name = request.name,
        modified_at = datetime.utcnow(),
        modified_by = request.modified_by,
        )
    db.commit()
    return 'updated successfully'