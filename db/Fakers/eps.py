import mysql.connector

# Conexión a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia si es necesario
    database="projectFinal",
    port=3307   
)
cursor = conn.cursor()

# EPS comunes en Colombia, y genéricas para Perú y Ecuador
lista_eps = [
    "Nueva EPS",
    "Salud Total",
    "Sanitas",
    "Coomeva",
    "Compensar",
    "SURA",
    "Aliansalud",
    "Famisanar",
    "Cajacopi",
    "EPS Generica Perú",
    "EPS Generica Ecuador"
]

# Insertar EPS
for nombre in lista_eps:
    try:
        cursor.execute(
            "INSERT INTO eps (nombre, estado) VALUES (%s, %s)",
            (nombre, '1')
        )
    except mysql.connector.errors.IntegrityError:
        print(f"La EPS '{nombre}' ya existe. Se omitió.")

# Confirmar cambios
conn.commit()
print("✔ EPS insertadas correctamente.")

# Cerrar conexión
cursor.close()
conn.close()
