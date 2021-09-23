from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from butler.schemas.common import schemas_base

from . import space

class SpaceStateBase(schemas_base.ModelBase):
    name: str 
    spaces: List[space.Space]

class SpaceState(SpaceStateBase):
    class Config():
        orm_mode = True