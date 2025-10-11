from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
from .. import models, schemas

# Lógica CRUD de productos

def get_products(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.Product]:
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate) -> schemas.Product:
    category = db.query(models.Category).filter(models.Category.id == product.category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail="La categoría no existe")
    db_product = models.Product(nombre=product.nombre, category_id=product.category_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, updated_product: schemas.ProductCreate) -> schemas.Product:
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    category = db.query(models.Category).filter(models.Category.id == updated_product.category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail="La categoría no existe")
    product.nombre = updated_product.nombre
    product.category_id = updated_product.category_id
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int) -> dict:
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(product)
    db.commit()
    return {"detail": "Producto eliminado"}
