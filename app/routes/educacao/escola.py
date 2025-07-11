from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import text 
from sqlalchemy.orm import Session
from app.schemas.educacao.escola import Escola as EscolaSchema
from app.core.database import get_db
from typing import Optional

router = APIRouter(prefix="/api/v1/escola", tags=["Escola"])

@router.get("/", response_model=list[EscolaSchema])
def list_escolas(
    db: Session = Depends(get_db),
    codigo_sec: Optional[int] = Query(None, description="Filtrar por código SEC"),
    nome: Optional[str] = Query(None, description="Filtrar por nome da escola"),
    nte: Optional[str] = Query(None, description="Filtrar por NTE"),
    series_avaliacao_diagnostica: Optional[int] = Query(None, description="Filtrar por série de avaliação diagnóstica"),
    rpp: Optional[int] = Query(None, description="Filtrar por RPP"),
    militar: Optional[str] = Query(None, description="Filtrar por Escolas Militares"),
    efa: Optional[str] = Query(None, description="Filtrar por EFA"),
    cemit: Optional[str] = Query(None, description="Filtrar por CEMIT"),
    prioritaria: Optional[str] = Query(None, description="Filtrar por escolas prioritárias")
):
    filter_conditions = []
    params = {}
    
    if codigo_sec:
        filter_conditions.append("e.codigo_sec = :codigo_sec")
        params["codigo_sec"] = codigo_sec
    if nome:
        filter_conditions.append("unaccent(e.nome) ILIKE :nome")
        params["nome"] = f"%{nome}%"
    if nte:
        filter_conditions.append("unaccent(n.nome) ILIKE :nte")
        params["nte"] = f"%{nte}%"

    if series_avaliacao_diagnostica:
        filter_conditions.append("f.series_avaliacao_diagnostica = :series_avaliacao_diagnostica")
        params["series_avaliacao_diagnostica"] = series_avaliacao_diagnostica
    
    if rpp:
        filter_conditions.append("f.rpp = :rpp")
        params["rpp"] = rpp
    
    if militar:
        filter_conditions.append("f.militar = :militar")
        params["militar"] = militar

    if efa:
        filter_conditions.append("f.efa = :efa")
        params["efa"] = efa

    if cemit:
        filter_conditions.append("f.cemit = :cemit")
        params["cemit"] = cemit

    if prioritaria:
        filter_conditions.append("f.prioritaria = :prioritaria")
        params["prioritaria"] = prioritaria
    
    where_clause = f"WHERE {' AND '.join(filter_conditions)}" if filter_conditions else ""
    
    query = text(f"""
        SELECT e.*,
               n.nome AS nte,
               m.nome AS municipio,
               f.series_avaliacao_diagnostica,
               f.rpp,
               f.militar,
               f.efa,
               f.cemit,
               f.prioritaria,
               f.motivo_prioritaria
        FROM escola e
        LEFT JOIN nte n ON e.nte_id = n.id
        LEFT JOIN municipio m ON e.municipio_id = m.id
        LEFT JOIN flag_escola f ON e.id = f.escola_id
        {where_clause}
    """)

    results = db.execute(query, params).mappings().all()

    return [dict(row) for row in results]