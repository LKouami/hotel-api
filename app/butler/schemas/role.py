from butler.schemas.user import User
from datetime import datetime
from typing import List, Optional
from butler.schemas.common import schemas_base


class RoleBase(schemas_base.RoleModelBase):
    name: str
    class Config():
        orm_mode = True

class ShowRole(schemas_base.RoleModelBase):
    name: Optional[str]
    users: List[User]
    class Config():
        orm_mode = True

class Role(RoleBase):
    class Config():
        orm_mode = True
