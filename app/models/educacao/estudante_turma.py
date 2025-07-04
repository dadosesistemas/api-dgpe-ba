from sqlalchemy import Column, BigInteger, Date, ForeignKey, PrimaryKeyConstraint
from app.models.base import Base

class EstudanteTurma(Base):
    __tablename__ = "estudante_turma"
    __table_args__ = {"schema": "public"} 
    __table_args__ = (
        PrimaryKeyConstraint("estudante_id", "turma_id"),
    )

    estudante_id = Column(BigInteger, ForeignKey("public.estudante.id"), primary_key=True)
    turma_id = Column(BigInteger, ForeignKey("public.turma.id"), primary_key=True)
    data_enturmacao = Column(Date)