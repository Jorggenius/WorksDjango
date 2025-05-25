import mysql.connector

# Conexión a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia si es necesario
    database="projectFinal",
    port=3307   
)
cursor = conn.cursor(dictionary=True)

# Obtener personas civiles SIN línea telefónica
cursor.execute("""
    SELECT pc.pers_id
    FROM persona_civil pc
    LEFT JOIN linea_telefonica lt ON pc.pers_id = lt.pers_id
    WHERE lt.pers_id IS NULL
""")
personas_disponibles = [row["pers_id"] for row in cursor.fetchall()]

# Obtener números de teléfono NO asignados
cursor.execute("""
    SELECT nt.nute_id
    FROM numero_telefono nt
    LEFT JOIN linea_telefonica lt ON nt.nute_id = lt.nute_id
    WHERE lt.nute_id IS NULL
""")
numeros_disponibles = [row["nute_id"] for row in cursor.fetchall()]

# Determinar cuántos pares se pueden hacer
cantidad = min(len(personas_disponibles), len(numeros_disponibles))
print(f"🔗 Asignando {cantidad} líneas telefónicas...")

# Poblar la tabla
for i in range(cantidad):
    pers_id = personas_disponibles[i]
    nute_id = numeros_disponibles[i]
    try:
        cursor.execute("""
            INSERT INTO linea_telefonica (pers_id, nute_id)
            VALUES (%s, %s)
        """, (pers_id, nute_id))
    except mysql.connector.errors.IntegrityError as e:
        print(f"❌ Error con persona {pers_id} y número {nute_id}: {e}")

# Confirmar
conn.commit()
print("✔ Tabla 'linea_telefonica' poblada correctamente con", cantidad, "registros.")

# Cerrar conexión
cursor.close()
conn.close()
