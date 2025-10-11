# test_connection.py
from app.database import engine

try:
    with engine.connect() as connection:
        print("✅ Conexión exitosa a MySQL!")
except Exception as e:
    print("❌ Error al conectar:", e)