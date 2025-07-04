from app.schemas.base import ModelBase
from datetime import date
from typing import Optional

class ProfessorTurmaBase(ModelBase):
    professor_id: int
    turma_id: int

class ProfessorTurmaCreate(ProfessorTurmaBase):
    data_enturmacao: Optional[date] = None

class ProfessorTurma(ProfessorTurmaBase):
    data_enturmacao: Optional[date] = None

    class Config:
        from_attributes = True