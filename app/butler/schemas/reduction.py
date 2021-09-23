from typing import List
from butler.schemas.common import schemas_base

from . import reservation

class ReductionBase(schemas_base.ModelBase):
    name: str 
    rate: float
    reservations: List[reservation.Reservation]

class Reduction(ReductionBase):
    class Config():
        orm_mode = True