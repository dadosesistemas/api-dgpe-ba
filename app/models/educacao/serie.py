from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Serie(Base):
    __tablename__ = "serie"
    __table_args__ = {"schema": "public"} 

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)

    # Relacionamentos
    turmas = relationship("Turma", back_populates="serie")