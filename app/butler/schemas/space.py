from butler.schemas.common import schemas_base


class SpaceBase(schemas_base.ModelBase):
    name: str 
    location: str
    price: str
    comments: str
class Space(SpaceBase):
    class Config():
        orm_mode = True
