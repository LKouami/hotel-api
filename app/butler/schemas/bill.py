from datetime import datetime
from butler.schemas.common import schemas_base


class BillBase(schemas_base.ModelBase):
    b_date: datetime
    b_num: str
    client_id: int
    

class Bill(BillBase):
    class Config():
        orm_mode = True