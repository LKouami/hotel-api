import datetime
from typing import Optional

from pydantic import BaseModel


class ModelBase(BaseModel):
    id: Optional[int]
    user_id: int
    created_at: datetime.datetime
    modified_by: Optional[int]
    modified_at: Optional[datetime.datetime]
    class Config():
        orm_mode = True

class RoleModelBase(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime.datetime]
    modified_at: Optional[datetime.datetime]
    class Config():
        orm_mode = True

class UserModelBase(BaseModel):
    id: Optional[int] 
    created_at: datetime.datetime
    modified_at: Optional[datetime.datetime]
    class Config():
        orm_mode = True
