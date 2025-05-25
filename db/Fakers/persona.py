import mysql.connector
from faker import Faker
import random

# Conexión a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia si es necesario
    database="projectFinal",
    port=3307   
)
cursor = conn.cursor(dictionary=True)
fake = Faker('es_ES')

# Obtener IDs válidos de tipo_documento
cursor.execute("SELECT tido_id FROM tipo_documento")
tipos_doc = [row['tido_id'] for row in cursor.fetchall()]

# Obtener IDs válidos de ciudad
cursor.execute("SELECT ciud_id FROM ciudad")
ciudades = [row['ciud_id'] for row in cursor.fetchall()]

# Insertar 30 personas
for _ in range(30):
    tido_id = random.choice(tipos_doc)
    ciud_nacimiento = random.choice(ciudades)
    ciud_residencia = random.choice(ciudades)
    
    nombre = fake.first_name()
    apellido = fake.last_name()
    documento = fake.unique.random_number(digits=8)
    fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=60).strftime("%Y-%m-%d")
    
    try:
        cursor.execute(
            """
            INSERT INTO persona 
            (tido_id, ciud_id_nacimiento, ciud_id_residencia, nombre, apellido, documento, fecha_nacimiento, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (tido_id, ciud_nacimiento, ciud_residencia, nombre, apellido, str(documento), fecha_nacimiento, '1')
        )
    except mysql.connector.errors.IntegrityError as e:
        print("Error al insertar persona:", e)

# Guardar cambios
conn.commit()
print("✔ Se insertaron 30 personas correctamente.")

# Cerrar conexión
cursor.close
