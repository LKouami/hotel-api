from datetime import datetime
from butler.schemas.common import schemas_base


class RoleBase(schemas_base.RoleModelBase):
    name: str

class Role(RoleBase):
    class Config():
        orm_mode = True
