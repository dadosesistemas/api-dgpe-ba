from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

router = APIRouter(
    prefix="/api/v1",  # Prefixo para todas as rotas
    tags=["Educação"],  # Tag no Swagger UI
)