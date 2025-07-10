from app.schemas.base import ModelBase
from app.schemas.educacao.flag_escola import FlagEscola as FlagEscolaSchema
from typing import Optional

class EscolaBase(ModelBase):
    nte: str
    municipio: str
    codigo_sec: int
    codigo_mec: int
    nome: str
    anexo: int
    cnpj: Optional[int] = None
    endereco_logradouro: Optional[str] = None
    endereco_numero: Optional[str] = None
    endereco_bairro: Optional[str] = None
    endereco_cep: Optional[int] = None
    latitude: Optional[int] = None
    longitude: Optional[int] = None
    series_avaliacao_diagnostica: int = None
    rpp: Optional[int] = None
    militar: Optional[int] = None
    efa: Optional[int] = None
    cemit: Optional[int] = None
    prioritaria: Optional[int] = None
    motivo_prioritaria: Optional[str] = None

class Escola(EscolaBase):
    id: int

    class Config:
        from_attributes = True