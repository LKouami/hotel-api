from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from butler.schemas.common import schemas_base

class SpaceBase(schemas_base.ModelBase):
    name: str 
    location: str
    price: str
    comments: str
    space_type_id: int
    space_state_id: int
    user_id: int

class Space(SpaceBase):
    class Config():
        orm_mode = True
class SpaceStateBase(schemas_base.ModelBase):
    name: str 

class ShowSpaceState(SpaceStateBase):
    spaces: List[Space]

class SpaceState(SpaceStateBase):
    class Config():
        orm_mode = True