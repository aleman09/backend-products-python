from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database
from ..controllers import categoriesController

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

get_db = database.get_db

# Listar categorías
@router.get("/", response_model=List[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return categoriesController.get_categories(db, skip, limit)

# Obtener categoría por ID
@router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    return categoriesController.get_category(db, category_id)

# Crear categoría
@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return categoriesController.create_category(db, category)

# Actualizar categoría
@router.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, updated_category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return categoriesController.update_category(db, category_id, updated_category)

# Eliminar categoría
@router.delete("/{category_id}", response_model=dict)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return categoriesController.delete_category(db, category_id)
