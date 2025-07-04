from app.schemas.base import ModelBase

class SerieBase(ModelBase):
    descricao: str

class SerieCreate(SerieBase):
    pass

class Serie(SerieBase):
    id: int

    class Config:
        from_attributes = True