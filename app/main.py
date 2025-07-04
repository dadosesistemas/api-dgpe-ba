from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .core.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.routes.educacao import (
    nte, municipio, escola, flag_escola,
    perfil, estudante, professor, serie, turma
)

app = FastAPI(title="API DGPE BA")

# CORS (ajuste conforme necessidade)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API DGPE BA - Dados PostgreSQL via SSH"}

# Registrar rotas
app.include_router(nte.router)
app.include_router(municipio.router)
app.include_router(escola.router)
app.include_router(flag_escola.router)
app.include_router(perfil.router)
app.include_router(estudante.router)
app.include_router(professor.router)
app.include_router(serie.router)
app.include_router(turma.router)