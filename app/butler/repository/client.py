from datetime import datetime
from butler.models import models
from butler.schemas.client import Client
from sqlalchemy.orm import Session
from fastapi import status, HTTPException


def get_all(db: Session):
    clients = db.query(models.Client).all()
    return clients


def create(request: Client, db: Session):
    new_client = models.Client(
        name=request.name,
        email=request.email,
        nationality=request.nationality,
        id_card_num=request.id_card_num,
        phone=request.phone,
        birth_date=request.birth_date,
        under_cover=request.under_cover,
        comments=request.comments,
        client_type_id=request.client_type_id,
        created_at=datetime.utcnow(),
        user_id=request.user_id,
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client


def destroy(id: int, db: Session):
    client = db.query(models.Client).filter(models.Client.id == id)
    if not client.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Client with the id : {id} is not found")
    client.delete(synchronize_session=False)
    db.commit()
    return 'done'


def get_one(id: int, db: Session):
    client = db.query(models.Client).filter(models.Client.id == id).first()
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Client with the id : {id} is not found")
    return client


def update(id: int, request: Client, db: Session):
    client = db.query(models.Client).filter(models.Client.id == id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Client with the id : {id} is not found")
    client.update(
        request.dict(exclude_unset= True)
    )
    db.commit()
    return 'updated successfully'
