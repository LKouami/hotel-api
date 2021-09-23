import datetime
from typing import Optional

from pydantic import BaseModel


class ModelBase(BaseModel):
    id: Optional[str]
    user_id: int
    created_at: datetime.datetime
    modified_by: Optional[int]
    modified_at: Optional[datetime.datetime]

class RoleModelBase(BaseModel):
    id: Optional[str]
    created_at: Optional[datetime.datetime]
    modified_by: Optional[int]
    modified_at: Optional[datetime.datetime]

class UserModelBase(BaseModel):
    id: Optional[str]
    creation_at: datetime.datetime
    modified_at: Optional[datetime.datetime]
