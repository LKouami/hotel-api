from datetime import datetime
from typing import List, Optional
from butler.schemas.to_bill import ToBill
from butler.schemas.common import schemas_base


class BillBase(schemas_base.ModelBase):
    b_date: datetime
    b_num: str
    client_id: int

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

class ShowBill(schemas_base.ModelBase):
    b_date: datetime
    b_num: str
    client_id: int
    client: Client
    to_bills: Optional [List[ToBill]]

class Bill(BillBase):
    class Config():
        orm_mode = True