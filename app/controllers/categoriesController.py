from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
from .. import models, schemas

# -----------------------------
# Obtener todas las categorías
# -----------------------------
def get_categories(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.Category]:
    return db.query(models.Category).offset(skip).limit(limit).all()

# -----------------------------
# Obtener categoría por ID
# -----------------------------
def get_category(db: Session, category_id: int) -> schemas.Category:
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return category

# -----------------------------
# Crear nueva categoría
# -----------------------------
def create_category(db: Session, category: schemas.CategoryCreate) -> schemas.Category:
    existing = db.query(models.Category).filter(models.Category.name == category.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="La categoría ya existe")
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# -----------------------------
# Actualizar categoría
# -----------------------------
def update_category(db: Session, category_id: int, updated_category: schemas.CategoryCreate) -> schemas.Category:
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    category.name = updated_category.name
    db.commit()
    db.refresh(category)
    return category
