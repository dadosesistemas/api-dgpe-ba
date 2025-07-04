from sqlalchemy import Column, BigInteger, Date, ForeignKey, PrimaryKeyConstraint
from app.models.base import Base

class ProfessorTurma(Base):
    __tablename__ = "professor_turma"
    __table_args__ = {"schema": "public"} 
    __table_args__ = (
        PrimaryKeyConstraint("professor_id", "turma_id"),
    )

    professor_id = Column(BigInteger, ForeignKey("public.professor.id"), primary_key=True)
    turma_id = Column(BigInteger, ForeignKey("public.turma.id"), primary_key=True)
    data_enturmacao = Column(Date)