
from butler.schemas.client import Client
from typing import List, Optional
from pydantic import BaseModel
from butler.schemas.common import schemas_base


class User(schemas_base.UserModelBase):
    name: str
    email:str
    password:str
    role_id: int
    class Config():
        orm_mode = True

class ShowRole(schemas_base.RoleModelBase):
    name: Optional[str]
    users: Optional[List[User]]
    class Config():
        orm_mode = True

class ShowUser(schemas_base.UserModelBase):
    name : str
    email : str
    clients : List[Client]
    role: ShowRole
    class Config():
        orm_mode = True