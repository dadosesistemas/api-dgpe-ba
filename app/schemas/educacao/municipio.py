from app.schemas.base import ModelBase
from pydantic import model_validator
from typing import Optional, Dict, Any

class MunicipioBase(ModelBase):
    codigo_ibge: int
    nome: str
    coordenadas: Optional[str] = None

class Municipio(MunicipioBase):
    id: int

    @model_validator(mode="after")
    def remove_coordenadas_if_none(self) -> Dict[str, Any]:
        # Remove o campo 'coordenadas' se for None
        data = self.model_dump(exclude_none=True)
        if "coordenadas" in data and data["coordenadas"] is None:
            del data["coordenadas"]
        return data

    class Config:
        from_attributes = True