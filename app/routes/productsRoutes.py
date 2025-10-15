from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database
from ..controllers import productsController

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

get_db = database.get_db

# Listar productos
@router.get("/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return productsController.get_products(db, skip, limit)

# Obtener producto por ID
@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return productsController.get_product(db, product_id)

# Crear producto
@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return productsController.create_product(db, product)

# Actualizar producto
@router.put("/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, updated_product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return productsController.update_product(db, product_id, updated_product)

# Eliminar producto
@router.delete("/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return productsController.delete_product(db, product_id)
