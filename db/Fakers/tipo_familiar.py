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

# Tipos de familiares comunes
tipos_familiares = [
    "Padre",
    "Madre",
    "Hermano",
    "Hermana",
    "Hijo",
    "Hija",
    "Abuelo",
    "Abuela",
    "Tío",
    "Tía",
    "Primo",
    "Prima",
    "Cónyuge",
    "Pareja",
    "Tutor Legal"
]

# Insertar datos
for tipo in tipos_familiares:
    try:
        cursor.execute(
            "INSERT INTO tipo_familiar (nombre, estado) VALUES (%s, %s)",
            (tipo, '1')
        )
    except mysql.connector.errors.IntegrityError:
        print(f"Tipo '{tipo}' ya existe.")

# Confirmar y cerrar
conn.commit()
print("✔ Tipos de familiar insertados correctamente.")
cursor.close()
conn.close()
