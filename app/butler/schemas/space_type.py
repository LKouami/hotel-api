from typing import List
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
class SpaceTypeBase(schemas_base.ModelBase):
    name: str 
    class Config():
        orm_mode = True
class ShowSpaceType(SpaceTypeBase):
    spaces: List[Space]
    class Config():
        orm_mode = True
class SpaceType(SpaceTypeBase):
    class Config():
        orm_mode = True