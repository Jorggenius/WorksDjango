import mysql.connector
import random

# Conexión a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia si es necesario
    database="projectFinal",
    port=3307   
)
cursor = conn.cursor(dictionary=True)

# Obtener todas las personas disponibles
cursor.execute("SELECT pers_id FROM persona")
personas = [row["pers_id"] for row in cursor.fetchall()]

# Obtener tipos de familiar
cursor.execute("SELECT tifa_id FROM tipo_familiar")
tipos_familiar = [row["tifa_id"] for row in cursor.fetchall()]

# Insertar relaciones familiares
for pers_id in personas:
    # Elegir un familiar diferente
    posibles_familiares = [pid for pid in personas if pid != pers_id]
    if not posibles_familiares:
        continue  # Evitar si no hay suficientes personas

    pers_id_familiar = random.choice(posibles_familiares)
    tifa_id = random.choice(tipos_familiar)

    try:
        cursor.execute("""
            INSERT INTO familia (
                pers_id, pers_id_familiar, tifa_id
            ) VALUES (%s, %s, %s)
        """, (pers_id, pers_id_familiar, tifa_id))
    except mysql.connector.errors.IntegrityError as e:
        print(f"Error para pers_id {pers_id} → {pers_id_familiar}: {e}")

# Confirmar y cerrar
conn.commit()
print("✔ Tabla 'familia' poblada correctamente con relaciones familiares.")
cursor.close()
conn.close()
