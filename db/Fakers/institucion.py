import mysql.connector
from faker import Faker
import random

fake = Faker('es_ES')  # 'es_CO' si lo tienes bien instalado, o usa 'es_ES'

# Conexión
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia si es necesario
    database="projectFinal",
    port=3307   
)
cursor = conn.cursor(dictionary=True)

# Obtener todas las ciudades disponibles
cursor.execute("SELECT ciud_id FROM ciudad")
ciudades = [row["ciud_id"] for row in cursor.fetchall()]

if not ciudades:
    print("❌ No hay ciudades en la base de datos. Inserta primero registros en la tabla `ciudad`.")
    cursor.close()
    conn.close()
    exit()

cantidad = 30
print(f"🏫 Generando {cantidad} instituciones académicas...")

insertadas = 0

for _ in range(cantidad):
    nombre = f"{fake.company()} Instituto Educativo"
    nit = str(fake.unique.random_number(digits=9))
    ciud_id = random.choice(ciudades)

    try:
        cursor.execute("""
            INSERT INTO institucion (ciud_id, nombre, nit, estado)
            VALUES (%s, %s, %s, %s)
        """, (ciud_id, nombre, nit, '1'))
        insertadas += 1
        print(f"✅ Insertada: {nombre} - NIT: {nit} - Ciudad ID: {ciud_id}")
    except mysql.connector.errors.IntegrityError as e:
        print(f"⚠️ No insertada (duplicado o error): {e}")

# Confirmar e informar
conn.commit()
print(f"✔ Se insertaron {insertadas} instituciones correctamente.")
cursor.close()
conn.close()
