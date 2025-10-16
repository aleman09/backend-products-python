import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# ⚙️ 1. Asegurar que Alembic encuentre el paquete 'app'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ⚙️ 2. Cargar variables de entorno
load_dotenv()

# ⚙️ 3. Config base
config = context.config
fileConfig(config.config_file_name)

# ⚙️ 4. Construir la URL de la DB
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# ⚙️ 5. Importar todos los modelos aquí
from app.models import Base, Category, Product, Role

# ⚙️ 6. Asignar metadata
target_metadata = Base.metadata

# --- Modo offline ---
def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True
    )
    with context.begin_transaction():
        context.run_migrations()

# --- Modo online ---
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
