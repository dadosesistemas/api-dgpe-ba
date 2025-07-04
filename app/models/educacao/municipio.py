from sqlalchemy import Column, BigInteger, String, Integer
from sqlalchemy.orm import relationship
from app.models.base import Base

class Municipio(Base):
    __tablename__ = "municipio"
    __table_args__ = {"schema": "public"} 

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    codigo_ibge = Column(Integer)
    nome = Column(String, nullable=False)
    coordenadas = Column(String)

    escolas = relationship("Escola", back_populates="municipio")