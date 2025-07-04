from app.schemas.base import ModelBase
from datetime import date
from typing import Optional

class EstudanteTurmaBase(ModelBase):
    estudante_id: int
    turma_id: int

class EstudanteTurmaCreate(EstudanteTurmaBase):
    data_enturmacao: Optional[date] = None

class EstudanteTurma(EstudanteTurmaBase):
    data_enturmacao: Optional[date] = None

    class Config:
        from_attributes = True