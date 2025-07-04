from datetime import date
from pydantic import BaseModel
from typing import Optional
from app.schemas.base import ModelBase

class FlagEscolaBase(ModelBase):
    tipo: str
    data_insercao: date
    valor: str
    escola_id: int

class FlagEscolaCreate(FlagEscolaBase):
    pass

class FlagEscola(FlagEscolaBase):
    id: int

    class Config:
        from_attributes = True