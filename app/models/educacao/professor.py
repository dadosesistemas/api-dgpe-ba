from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Professor(Base):
    __tablename__ = "professor"
    __table_args__ = {"schema": "public"} 

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    rm = Column(Integer, unique=True, nullable=False)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    cpf = Column(Integer)
    login = Column(String)
    password = Column(String)
    perfil_id = Column(BigInteger, ForeignKey("public.perfil.id"), unique=True, nullable=False)

    # Relacionamentos
    perfil = relationship("Perfil", back_populates="professores")