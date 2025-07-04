from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.models.educacao.perfil import Perfil
from app.schemas.educacao.perfil import Perfil as PerfilSchema
from app.core.database import get_db
from typing import Optional

router = APIRouter(prefix="/api/v1/perfil", tags=["Perfil"])

@router.get("/", response_model=list[PerfilSchema])
def list_perfis(
    db: Session = Depends(get_db),
    descricao: Optional[str] = Query(None, description="Filtrar por descrição do perfil")
):
    query = db.query(Perfil)
    if descricao:
        query = query.filter(Perfil.descricao.ilike(f"%{descricao}%"))
    return query.all()

@router.get("/{perfil_id}", response_model=PerfilSchema)
def get_perfil(perfil_id: int, db: Session = Depends(get_db)):
    perfil = db.query(Perfil).filter(Perfil.id == perfil_id).first()
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")
    return perfil