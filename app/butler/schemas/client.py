import datetime
from typing import List, Optional
from butler.schemas.reservation import Reservation
from butler.schemas.bill import Bill
from butler.schemas.client_type import ClientType
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

class ShowClient(schemas_base.ModelBase):
    name: str 
    email: str
    nationality: str
    id_card_num: str
    phone: str
    birth_date: datetime.datetime
    under_cover: str
    comments: str
    client_type: ClientType
    client_type_id: int
    bills: Optional [List[Bill]]
    reservations: Optional [List[Reservation]]


class Client(ClientBase):
    class Config():
        orm_mode = True
