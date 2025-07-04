from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Perfil(Base):
    __tablename__ = "perfil"
    __table_args__ = {"schema": "public"} 

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)

    # Relacionamentos
    professores = relationship("Professor", back_populates="perfil")
    estudantes = relationship("Estudante", back_populates="perfil")