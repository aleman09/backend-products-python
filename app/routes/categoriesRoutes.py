from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database
from ..controllers import categoriesController

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

# Dependencia para la sesión
get_db = database.get_db

# Endpoints
@router.get("/", response_model=List[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return categoriesController.get_categories(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return categoriesController.create_category(db, category)

@router.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, updated_category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return categoriesController.update_category(db, category_id, updated_category)

@router.delete("/{category_id}", response_model=dict)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return categoriesController.delete_category(db, category_id)
