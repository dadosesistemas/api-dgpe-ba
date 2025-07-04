from app.schemas.base import ModelBase
from typing import Optional

class EstudanteBase(ModelBase):
    rm: int
    nome: str
    email: str
    perfil_id: int

class EstudanteCreate(EstudanteBase):
    cpf: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None  # Campo sensível (não retornar na resposta!)

class Estudante(EstudanteBase):
    id: int

    class Config:
        from_attributes = True