from pydantic import BaseModel
from typing import Optional, Union

class ModelBase(BaseModel):
    class Config:
        from_attributes = True  # Equivalente a `orm_mode = True` (v2 do Pydantic)