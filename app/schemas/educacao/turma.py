from app.schemas.base import ModelBase

class TurmaBase(ModelBase):
    codigo: str
    descricao: str
    escola_id: int
    serie_id: int

class TurmaCreate(TurmaBase):
    pass

class Turma(TurmaBase):
    id: int

    class Config:
        from_attributes = True