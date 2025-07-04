from app.schemas.base import ModelBase
from typing import Optional

class ProfessorBase(ModelBase):
    rm: int
    nome: str
    email: str
    perfil_id: int

class ProfessorCreate(ProfessorBase):
    cpf: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None  # Campo sensível (não retornar na resposta!)

class Professor(ProfessorBase):
    id: int

    class Config:
        from_attributes = True