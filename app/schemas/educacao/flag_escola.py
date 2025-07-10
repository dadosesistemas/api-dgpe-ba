from datetime import date
from typing import Optional
from app.schemas.base import ModelBase

class FlagEscolaBase(ModelBase):
    escola_id: int
    series_avaliacao_diagnostica: int
    rpp: int
    militar: int
    efa: int
    cemit: int
    prioritaria: int
    motivo_prioritaria: str

class FlagEscola(FlagEscolaBase):
    id: int

    class Config:
        from_attributes = True

    