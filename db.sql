DROP TABLE products;
DROP TABLE categories;

-- Crear tabla de categorías
CREATE TABLE categories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

-- Crear tabla de productos con relación a categorías
CREATE TABLE products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  category_id INT,
  FOREIGN KEY (category_id) REFERENCES categories(id)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);

-- Insertar 3 categorías
INSERT INTO categories (name)
VALUES 
('Electrónica'),
('Ropa'),
('Hogar');

-- Insertar 3 productos, cada uno asociado a una categoría
INSERT INTO products (name, category_id)
VALUES
('Televisor', 1),   -- Electrónica
('Camiseta', 2),    -- Ropa
('Cafetera', 3);    -- Hogar