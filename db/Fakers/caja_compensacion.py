import mysql.connector

# Conexión a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia si es necesario
    database="projectFinal",
    port=3307   
)
cursor = conn.cursor()

# Lista de cajas de compensación
cajas = [
    "Comfama",
    "Cafam",
    "Compensar",
    "Colsubsidio",
    "Comfenalco Antioquia",
    "Comfenalco Valle",
    "Cajacopi Atlántico",
    "Caja de Compensación Perú",
    "Caja de Compensación Ecuador"
]

# Insertar cajas
for nombre in cajas:
    try:
        cursor.execute(
            "INSERT INTO caja_compensacion (nombre, estado) VALUES (%s, %s)",
            (nombre, '1')
        )
    except mysql.connector.errors.IntegrityError:
        print(f"La caja '{nombre}' ya existe. Se omitió.")

# Confirmar cambios
conn.commit()
print("✔ Tabla 'caja_compensacion' poblada correctamente.")

# Cerrar conexión
cursor.close()
conn.close()
