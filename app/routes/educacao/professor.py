from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.models.educacao.professor import Professor
from app.schemas.educacao.professor import Professor as ProfessorSchema
from app.core.database import get_db
from typing import Optional

router = APIRouter(prefix="/api/v1/professor", tags=["Professor"])

@router.get("/", response_model=list[ProfessorSchema])
def list_professores(
    db: Session = Depends(get_db),
    nome: Optional[str] = Query(None, description="Filtrar por nome do professor"),
    rm: Optional[int] = Query(None, description="Filtrar por RM"),
):
    query = db.query(Professor)
    if nome:
        query = query.filter(Professor.nome.ilike(f"%{nome}%"))
    if rm:
        query = query.filter(Professor.rm == rm)
    return query.all()

@router.get("/{professor_id}", response_model=ProfessorSchema)
def get_professor(professor_id: int, db: Session = Depends(get_db)):
    professor = db.query(Professor).filter(Professor.id == professor_id).first()
    if not professor:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return professor