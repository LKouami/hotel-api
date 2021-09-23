from butler.schemas.common import schemas_base

from typing import List, Optional
from . import client

class ClientTypeBase(schemas_base.ModelBase):
    name: str 
    clients:Optional [List[client.Client]]
    space_type_id: int
    space_state_id: int
class ClientType(ClientTypeBase):
    class Config():
        orm_mode = True
