from datetime import datetime
from butler.schemas.common import schemas_base


class ToBillBase(schemas_base.ModelBase):
    tb_date : datetime
    tb_num : str
    amount_to_be_paid : float
    bill_id: int
    reservation_id:int

class ToBill(ToBillBase):
    class Config():
        orm_mode = True