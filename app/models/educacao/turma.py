from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Turma(Base):
    __tablename__ = "turma"
    __table_args__ = {"schema": "public"} 

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    escola_id = Column(Integer, ForeignKey("public.escola.id"), unique=True, nullable=False)
    serie_id = Column(Integer, ForeignKey("public.serie.id"), unique=True, nullable=False)

    # Relacionamentos
    serie = relationship("Serie", back_populates="turmas")