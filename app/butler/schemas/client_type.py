from datetime import datetime
from butler.schemas.common import schemas_base

from typing import List, Optional

class ClientTypeBase(schemas_base.ModelBase):
    name: str 
    class Config():
        orm_mode = True

class Client(schemas_base.ModelBase):
    name: str 
    email: str
    nationality: str
    id_card_num: str
    phone: str
    birth_date: datetime
    under_cover: str
    comments: str
    client_type_id: int
    class Config():
        orm_mode = True

class ShowClientType(schemas_base.ModelBase):
    name: str 
    clients:Optional [List[Client]]
    class Config():
        orm_mode = True
class ClientType(ClientTypeBase):
    class Config():
        orm_mode = True
