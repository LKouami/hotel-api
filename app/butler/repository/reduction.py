from datetime import datetime
from butler.models import models
from butler.schemas.reduction import Reduction
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def get_all(db: Session):
    reductions = db.query(models.Reduction).all()
    return reductions

def create(request: Reduction, db : Session ):
    new_reduction = models.Reduction(
        name = request.name, 
        rate = request.rate, 
        created_at = datetime.utcnow(),  
        user_id = request.user_id,
        )
    db.add(new_reduction)
    db.commit()
    db.refresh(new_reduction)
    return new_reduction

def destroy(id:int, db : Session):
    reduction = db.query(models.Reduction).filter(models.Reduction.id == id)
    if not reduction.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Reduction with the id : {id} is not found")
    reduction.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_one(id:int, db : Session):
    reduction = db.query(models.Reduction).filter(models.Reduction.id == id).first()
    if not reduction:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Reduction with the id : {id} is not found")
    return reduction

def update(id:int, request: Reduction, db: Session):
    reduction = db.query(models.Reduction).filter(models.Reduction.id == id) 
    if not reduction:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Reduction with the id : {id} is not found")
    reduction.update(
        name = request.name, 
        rate = request.rate,
        modified_at = datetime.utcnow(),
        modified_by = request.modified_by,
        )
    db.commit()
    return 'updated successfully'