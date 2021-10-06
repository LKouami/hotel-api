from butler.schemas.common import schemas_base

from typing import List, Optional
from . import client

class ClientTypeBase(schemas_base.ModelBase):
    name: str 
    class Config():
        orm_mode = True

class ShowClientType(schemas_base.ModelBase):
    name: str 
    clients:Optional [List[client.Client]]
    class Config():
        orm_mode = True
class ClientType(ClientTypeBase):
    class Config():
        orm_mode = True
