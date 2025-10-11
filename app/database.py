# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()
# Forzar que PyMySQL se comporte como MySQLdb
pymysql.install_as_MySQLdb()

# -----------------------------
# Configuración de la base de datos desde .env
# -----------------------------
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# -----------------------------
# Crear motor de conexión
# -----------------------------
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# -----------------------------
# Crear sesión local
# -----------------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# -----------------------------
# Base para los modelos
# -----------------------------
Base = declarative_base()

# -----------------------------
# Dependencia para FastAPI (inyección de sesión por request)
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()