from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.educacao.escola import Escola
from app.models.educacao.nte import NTE
from app.models.educacao.municipio import Municipio
from app.schemas.educacao.escola import Escola as EscolaSchema
from app.core.database import get_db
from typing import Optional

router = APIRouter(prefix="/api/v1/escola", tags=["Escola"])

@router.get("/", response_model=list[EscolaSchema])
def list_escolas(
    db: Session = Depends(get_db),
    nome: Optional[str] = Query(None, description="Filtrar por nome da escola"),
    nte: Optional[str] = Query(None, description="Filtrar por NTE")
):
    query = db.query(
        Escola,
        NTE.nome.label('nte'),
        Municipio.nome.label('municipio')
    ).join(
        NTE, Escola.nte_id == NTE.id
    ).join(
        Municipio, Escola.municipio_id == Municipio.id
    ).all()

    if nome:
        query = query.filter(Escola.nome.ilike(f"%{nome}%"))
    if nte:
        query = query.filter(Escola.nte == nte)
    
    return [{
        **escola.__dict__,
        'nte': nte,
        'municipio': municipio
    } for escola, nte, municipio in query]

@router.get("/{codigo_sec}", response_model=EscolaSchema)
def get_escola(
    codigo_sec: int,
    db: Session = Depends(get_db)
):
    query = db.query(
        Escola,
        NTE.nome.label('nte'),
        Municipio.nome.label('municipio')
    ).join(
        NTE, Escola.nte_id == NTE.id
    ).join(
        Municipio, Escola.municipio_id == Municipio.id
    ).filter(
        Escola.codigo_sec == codigo_sec
    ).first()

    if not query:
        raise HTTPException(status_code=404, detail="Escola não encontrada")
    
    escola, nte, municipio = query
    return {
        **escola.__dict__,
        'nte': nte,
        'municipio': municipio
    }