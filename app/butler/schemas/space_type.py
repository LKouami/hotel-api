from typing import List
from butler.schemas.common import schemas_base

from .space import Space

class SpaceTypeBase(schemas_base.ModelBase):
    name: str 
    spaces: List[Space]
class SpaceType(SpaceTypeBase):
    class Config():
        orm_mode = True