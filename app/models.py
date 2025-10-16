from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime, func
from sqlalchemy.orm import relationship
from .database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    price = Column(Integer, nullable=True)
    category = relationship("Category", back_populates="products")

# ///////////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////////

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    permissions = Column(JSON, nullable=False, default=list)
    users = relationship("User", back_populates="role")
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    # Relación con Role
    role = relationship("Role", backref="users")