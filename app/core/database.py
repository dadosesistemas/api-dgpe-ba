from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sshtunnel import SSHTunnelForwarder
from .config import settings
import logging

Base = declarative_base()
# logging.basicConfig(level=logging.DEBUG)

def get_engine():
    if settings.SSH_HOST:  # Se usar SSH Tunnel
        tunnel = SSHTunnelForwarder(
            (settings.SSH_HOST, settings.SSH_PORT),
            ssh_username=settings.SSH_USERNAME,
            ssh_pkey=settings.SSH_PRIVATE_KEY_PATH,
            remote_bind_address=(settings.DB_HOST, settings.DB_PORT)
        )
        tunnel.start()
        db_url = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@localhost:{tunnel.local_bind_port}/{settings.DB_NAME}"
    else:  # Conexão direta
        db_url = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

    return create_engine(db_url)

engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()