from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.models.educacao.turma import Turma
from app.schemas.educacao.turma import Turma as TurmaSchema
from app.core.database import get_db
from typing import Optional

router = APIRouter(prefix="/api/v1/turma", tags=["Turma"])

@router.get("/", response_model=list[TurmaSchema])
def list_turmas(
    db: Session = Depends(get_db),
    codigo: Optional[str] = Query(None, description="Filtrar por código da turma"),
    escola_id: Optional[int] = Query(None, description="Filtrar por ID da escola"),
    serie_id: Optional[int] = Query(None, description="Filtrar por ID da série")
):
    query = db.query(Turma)
    if codigo:
        query = query.filter(Turma.codigo.ilike(f"%{codigo}%"))
    if escola_id:
        query = query.filter(Turma.escola_id == escola_id)
    if serie_id:
        query = query.filter(Turma.serie_id == serie_id)
    return query.all()

@router.get("/{turma_id}", response_model=TurmaSchema)
def get_turma(turma_id: int, db: Session = Depends(get_db)):
    turma = db.query(Turma).filter(Turma.id == turma_id).first()
    if not turma:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return turma