import datetime
from butler.schemas.common import schemas_base


class ClientBase(schemas_base.ModelBase):
    name: str 
    email: str
    nationality: str
    id_card_num: str
    phone: str
    birth_date: datetime.datetime
    under_cover: str
    comments: str
    client_type_id: int

class Client(ClientBase):
    class Config():
        orm_mode = True
