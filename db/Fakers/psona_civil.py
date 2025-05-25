import mysql.connector
import random
from faker import Faker

fake = Faker('es_ES')

# Conexión
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia si es necesario
    database="projectFinal",
    port=3307   
)
cursor = conn.cursor(dictionary=True)

# Obtener todas las personas que aún NO están en persona_civil
cursor.execute("""
    SELECT p.pers_id
    FROM persona p
    LEFT JOIN persona_civil pc ON p.pers_id = pc.pers_id
    WHERE pc.pers_id IS NULL
""")
personas_sin_civil = [p["pers_id"] for p in cursor.fetchall()]

# Obtener EPS y cajas
cursor.execute("SELECT eps_id FROM eps")
eps_ids = [e["eps_id"] for e in cursor.fetchall()]

cursor.execute("SELECT caco_id FROM caja_compensacion")
cajas_ids = [c["caco_id"] for c in cursor.fetchall()]

# Datos posibles
estratos = ['1', '2', '3', '4', '5', '6']
categorias_sisben = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'Desconocido']
estados_civiles = ['Soltero', 'Casado', 'Divorciado', 'Unión libre', 'Viudo', 'Desconocido']

# Insertar datos coherentes
for pers_id in personas_sin_civil:
    caco_id = random.choice(cajas_ids)
    eps_id = random.choice(eps_ids)
    estrato = random.choice(estratos)
    sisben = random.choice(categorias_sisben)
    estado_civil = random.choice(estados_civiles)

    t1 = fake.phone_number()
    t2 = fake.phone_number()
    t3 = fake.phone_number()
    telefonos = ", ".join([t1, t2, t3])

    try:
        cursor.execute("""
            INSERT INTO persona_civil (
                pers_id, caco_id, eps_id,
                estrato_socioeconomico, sisben_categoria, estado_civil,
                telefono, telefono2, telefono3, telefonos
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (pers_id, caco_id, eps_id, estrato, sisben, estado_civil, t1, t2, t3, telefonos))
    except mysql.connector.errors.IntegrityError as e:
        print(f"Error con persona {pers_id}: {e}")

# Confirmar cambios
conn.commit()
print("✔ Registros insertados correctamente en 'persona_civil'.")
cursor.close()
conn.close()

