import datetime
from typing import Optional

from pydantic import BaseModel


class ModelBase(BaseModel):
    user_id: int
    created_at: datetime.datetime
    modified_by: Optional[int]
    modified_at: Optional[datetime.datetime]
    class Config():
        orm_mode = True

class RoleModelBase(BaseModel):
    created_at: Optional[datetime.datetime]
    modified_at: Optional[datetime.datetime]
    class Config():
        orm_mode = True

class UserModelBase(BaseModel):
    created_at: datetime.datetime
    modified_at: Optional[datetime.datetime]
    class Config():
        orm_mode = True
