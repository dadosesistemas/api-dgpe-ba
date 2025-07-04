from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.models.educacao.estudante import Estudante
from app.schemas.educacao.estudante import Estudante as EstudanteSchema
from app.core.database import get_db
from typing import Optional

router = APIRouter(prefix="/api/v1/estudante", tags=["Estudante"])

@router.get("/", response_model=list[EstudanteSchema])
def list_estudantes(
    db: Session = Depends(get_db),
    nome: Optional[str] = Query(None, description="Filtrar por nome do estudante"),
    rm: Optional[int] = Query(None, description="Filtrar por RM"),
    perfil_id: Optional[int] = Query(None, description="Filtrar por ID do perfil")
):
    query = db.query(Estudante)
    if nome:
        query = query.filter(Estudante.nome.ilike(f"%{nome}%"))
    if rm:
        query = query.filter(Estudante.rm == rm)
    if perfil_id:
        query = query.filter(Estudante.perfil_id == perfil_id)
    return query.all()

@router.get("/{estudante_id}", response_model=EstudanteSchema)
def get_estudante(estudante_id: int, db: Session = Depends(get_db)):
    estudante = db.query(Estudante).filter(Estudante.id == estudante_id).first()
    if not estudante:
        raise HTTPException(status_code=404, detail="Estudante não encontrada")
    return estudante