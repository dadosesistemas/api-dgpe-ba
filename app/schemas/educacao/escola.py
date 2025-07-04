from app.schemas.base import ModelBase
from typing import Optional

class EscolaBase(ModelBase):
    nte_id: int
    municipio_id: int
    codigo_sec: int
    codigo_mec: int
    nome: str
    anexo: int

class EscolaCreate(EscolaBase):
    cnpj: Optional[int] = None
    endereco_logradouro: Optional[str] = None
    endereco_numero: Optional[str] = None
    endereco_bairro: Optional[str] = None
    endereco_cep: Optional[int] = None
    latitude: Optional[int] = None
    longitude: Optional[int] = None

class Escola(EscolaBase):
    id: int
    nte: str
    municipio: str

    class Config:
        from_attributes = True