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

class Client(schemas_base.ModelBase):
    name: str 
    email: str
    nationality: str
    id_card_num: str
    phone: str
    birth_date: datetime
    under_cover: str
    comments: str
    client_type_id: int
    class Config():
        orm_mode = True

class Space(schemas_base.ModelBase):
    name: str 
    location: str
    price: float
    comments: str
    space_type_id: int
    space_state_id: int
    class Config():
        orm_mode = True

class Reduction(schemas_base.ModelBase):
    name: str 
    rate: float
    class Config():
        orm_mode = True

class ShowReservation(BaseModel):
    begin_date: datetime 
    end_date: datetime 
    comments: str
    reservation_state: str
    client: Client
    space: Space
    reduction: Reduction
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