from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.models.educacao.nte import NTE
from app.schemas.educacao.nte import NTE as NTESchema
from app.core.database import get_db
from typing import Optional

router = APIRouter(prefix="/api/v1/nte", tags=["NTE"])

@router.get("/", response_model=list[NTESchema])
def list_nte(
    db: Session = Depends(get_db),
    nome: Optional[str] = Query(None, description="Filtrar por nome do NTE")
):
    query = db.query(NTE)
    if nome:
        query = query.filter(NTE.nome.ilike(f"%{nome}%"))
    return query.all()

@router.get("/{nte_id}", response_model=NTESchema)
def get_nte(nte_id: int, db: Session = Depends(get_db)):
    nte = db.query(NTE).filter(NTE.id == nte_id).first()
    if not nte:
        raise HTTPException(status_code=404, detail="NTE não encontrado")
    return nte