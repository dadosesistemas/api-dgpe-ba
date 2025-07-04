from app.schemas.base import ModelBase
from typing import Optional

class NTEBase(ModelBase):
    nome: str

class NTECreate(NTEBase):
    pass

class NTE(NTEBase):
    id: int

    class Config:
        from_attributes = True