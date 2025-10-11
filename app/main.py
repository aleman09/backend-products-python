from fastapi import FastAPI
from .routes import categoriesRoutes, productsRoutes
from . import database, models

app = FastAPI(title="API Products & Categories")

# Crear tablas si no existen
models.Base.metadata.create_all(bind=database.engine)

# Incluir routers
app.include_router(categoriesRoutes.router)
app.include_router(productsRoutes.router)
