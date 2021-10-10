from datetime import datetime
from butler.schemas.common import schemas_base
from typing import Optional

from pydantic import BaseModel

class ReservationBase(BaseModel):
    begin_date: datetime 
    end_date: datetime 
    comments: str
    reservation_state: str
    client_id: int
    space_id: int
    reduction_id: int
    created_at: datetime
    modified_by: Optional[int]
    modified_at: Optional[datetime]
    class Config():
        orm_mode = True

class ShowReservationBase(BaseModel):
    begin_date: datetime 
    end_date: datetime 
    comments: str
    reservation_state: str
    client_id: int
    space_id: int
    reduction_id: int
    created_at: datetime
    modified_by: Optional[int]
    modified_at: Optional[datetime]
    class Config():
        orm_mode = True

class Reservation(ReservationBase):
    class Config():
        orm_mode = True