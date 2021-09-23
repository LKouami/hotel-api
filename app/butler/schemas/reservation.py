from datetime import datetime
from butler.schemas.common import schemas_base


class ReservationBase(schemas_base.ModelBase):
    begin_date: datetime 
    end_date: datetime 
    comments: str
    reservation_state: str
    client_id: int
    space_id: int
    reduction_id: int

class Reservation(ReservationBase):
    class Config():
        orm_mode = True