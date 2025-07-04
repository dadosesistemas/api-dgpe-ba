from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.models.educacao.municipio import Municipio
from app.schemas.educacao.municipio import Municipio as MunicipioSchema
from app.core.database import get_db
from typing import Optional

router = APIRouter(prefix="/api/v1/municipio", tags=["Município"])

@router.get("/", response_model=list[MunicipioSchema])
def list_municipios(
    db: Session = Depends(get_db),
    nome: Optional[str] = Query(None, description="Filtrar por nome do município"),
    codigo_ibge: Optional[int] = Query(None, description="Filtrar por código IBGE"),
    coordenadas: Optional[str] = Query(None, description="Passar 'on' para incluir coordenadas")
):
    query = db.query(Municipio)
    
    if nome:
        query = query.filter(Municipio.nome.ilike(f"%{nome}%"))
    if codigo_ibge:
        query = query.filter(Municipio.codigo_ibge == codigo_ibge)    
    
    municipios = query.all()
    
    response = []
    for m in municipios:
        item = {
            "id": m.id,
            "codigo_ibge": m.codigo_ibge,
            "nome": m.nome
        }
        if coordenadas == "on":
            item["coordenadas"] = m.coordenadas
        response.append(item)
    
    return response

@router.get("/{codigo_ibge}", response_model=MunicipioSchema)
def get_municipio(
    codigo_ibge: int, 
    db: Session = Depends(get_db),
    coordenadas: Optional[str] = Query(None, description="Passar 'on' para incluir coordenadas")
):
    municipio = db.query(Municipio).filter(Municipio.codigo_ibge == codigo_ibge).first()
    if not municipio:
        raise HTTPException(status_code=404, detail="Município não encontrado")

    item = {
        "id": municipio.id,
        "codigo_ibge": municipio.codigo_ibge,
        "nome": municipio.nome
    }
    if coordenadas == "on":
        item["coordenadas"] = municipio.coordenadas
    
    return item