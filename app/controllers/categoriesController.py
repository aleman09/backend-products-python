from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
from .. import models, schemas

# Lógica CRUD de categorías

def get_categories(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.Category]:
    return db.query(models.Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: schemas.CategoryCreate) -> schemas.Category:
    existing = db.query(models.Category).filter(models.Category.nombre == category.nombre).first()
    if existing:
        raise HTTPException(status_code=400, detail="La categoría ya existe")
    db_category = models.Category(nombre=category.nombre)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, updated_category: schemas.CategoryCreate) -> schemas.Category:
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    category.nombre = updated_category.nombre
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int) -> dict:
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    db.delete(category)
    db.commit()
    return {"detail": "Categoría eliminada"}
