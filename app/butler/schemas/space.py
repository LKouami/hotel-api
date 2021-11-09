from pydantic import BaseModel
from butler.schemas.space_state import ShowSpaceState
from butler.schemas.space_type import ShowSpaceType
from butler.schemas.reservation import Reservation
from butler.schemas.common import schemas_base
from typing import List, Optional

class SpaceBase(schemas_base.ModelBase):
    name: str 
    location: str
    price: float
    comments: str
    space_type_id: int
    space_state_id: int

class ShowSpace(schemas_base.ModelBase):
    name: str 
    location: str
    price: float
    comments: str
    space_type_id: int
    space_state_id: int
    space_type : ShowSpaceType
    space_state : ShowSpaceState
    reservations : List[Reservation]
    class Config():
        orm_mode = True
class Space(SpaceBase):
    class Config():
        orm_mode = True
