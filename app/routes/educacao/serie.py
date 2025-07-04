from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.models.educacao.serie import Serie
from app.schemas.educacao.serie import Serie as SerieSchema
from app.core.database import get_db
from typing import Optional

router = APIRouter(prefix="/api/v1/serie", tags=["Série"])

@router.get("/", response_model=list[SerieSchema])
def list_series(
    db: Session = Depends(get_db),
    descricao: Optional[str] = Query(None, description="Filtrar por descrição da série")
):
    query = db.query(Serie)
    if descricao:
        query = query.filter(Serie.descricao.ilike(f"%{descricao}%"))
    return query.all()

@router.get("/{serie_id}", response_model=SerieSchema)
def get_serie(serie_id: int, db: Session = Depends(get_db)):
    serie = db.query(Serie).filter(Serie.id == serie_id).first()
    if not serie:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    return serie