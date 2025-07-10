from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class FlagEscola(Base):
    __tablename__ = "flag_escola"
    __table_args__ = {"schema": "public"} 

    id = Column(Integer, primary_key=True, autoincrement=True)
    escola_id = Column(Integer, ForeignKey("public.escola.id"), unique=True, nullable=False)
    series_avaliacao_diagnostica = Column(Integer, nullable=False, default=0)
    rpp = Column(Integer, nullable=False, default=0)
    militar = Column(Integer, nullable=False, default=0)
    efa = Column(Integer, nullable=False, default=0)
    cemit = Column(Integer, nullable=False, default=0)
    prioritaria = Column(Integer, nullable=False, default=0)
    motivo_prioritaria = Column(String)