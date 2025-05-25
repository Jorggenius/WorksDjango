import mysql.connector

# Conectar a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia si es necesario
    database="projectFinal",
    port=3307   
)
cursor = conn.cursor()

# Lista de países a insertar
paises = [
    ("Colombia", "1"),
    ("Perú", "1"),
    ("Ecuador", "1")
]

# Insertar los países
for nombre, estado in paises:
    try:
        cursor.execute(
            "INSERT INTO pais (nombre, estado) VALUES (%s, %s)",
            (nombre, estado)
        )
    except mysql.connector.errors.IntegrityError:
        print(f"Ya existe el país: {nombre}")

# Confirmar cambios
conn.commit()
print("✔ Tabla 'pais' poblada correctamente.")

# Cerrar conexión
cursor.close()
conn.close()
