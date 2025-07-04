from app.schemas.base import ModelBase

class PerfilBase(ModelBase):
    descricao: str

class PerfilCreate(PerfilBase):
    pass

class Perfil(PerfilBase):
    id: int

    class Config:
        from_attributes = True