from sqlalchemy import Column, BigInteger, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class NTE(Base):
    __tablename__ = "nte"
    __table_args__ = {"schema": "public"} 

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    codigo_sec = Column(Integer, unique=True, nullable=False)
    nome = Column(String, unique=True, nullable=False)

    escolas = relationship("Escola", back_populates="nte")