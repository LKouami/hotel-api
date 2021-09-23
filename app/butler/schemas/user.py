from butler.schemas.client import Client
from typing import List
from pydantic import BaseModel
from butler.schemas.common import schemas_base



class User(schemas_base.UserModelBase):
    name: str
    email:str
    password:str
    role_id: int

class ShowUser(BaseModel):
    name : str
    email : str
    clients : List[Client] 
    class Config():
        orm_mode = True