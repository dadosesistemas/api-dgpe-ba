from sqlalchemy import Column, BigInteger, Integer, String, CHAR, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Escola(Base):
    __tablename__ = "escola"
    __table_args__ = {"schema": "public"} 

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nte_id = Column(BigInteger, ForeignKey("public.nte.id"), unique=True, nullable=False)
    municipio_id = Column(BigInteger, ForeignKey("public.municipio.id"), unique=True, nullable=False)
    codigo_sec = Column(BigInteger, nullable=False)
    codigo_mec = Column(BigInteger, nullable=False)
    cnpj = Column(BigInteger)
    nome = Column(String, nullable=False)
    anexo = Column(Integer, nullable=False, default=0)
    endereco_logradouro = Column(String)
    endereco_numero = Column(String)
    endereco_bairro = Column(String)
    endereco_cep = Column(Integer)
    latitude = Column(Integer)
    longitude = Column(Integer)

    nte = relationship("NTE", back_populates="escolas")
    municipio = relationship("Municipio", back_populates="escolas")