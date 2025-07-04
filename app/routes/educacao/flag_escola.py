from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.models.educacao.flag_escola import FlagEscola
from app.schemas.educacao.flag_escola import FlagEscola as FlagEscolaSchema
from app.core.database import get_db
from typing import Optional

router = APIRouter(prefix="/api/v1/flag-escola", tags=["Flag Escola"])

@router.get("/", response_model=list[FlagEscolaSchema])
def list_flags(
    db: Session = Depends(get_db),
    escola_id: Optional[int] = Query(None, description="Filtrar por ID da escola")
):
    query = db.query(FlagEscola)
    if escola_id:
        query = query.filter(FlagEscola.escola_id == escola_id)
    return query.all()

@router.get("/{flag_id}", response_model=FlagEscolaSchema)
def get_flag(flag_id: int, db: Session = Depends(get_db)):
    flag_escola = db.query(FlagEscola).filter(FlagEscola.id == flag_id).first()
    if not flag_escola:
        raise HTTPException(status_code=404, detail="Flag Escola não encontrada")
    return flag_escola