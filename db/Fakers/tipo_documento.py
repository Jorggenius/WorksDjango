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

# Tipos de documento estándar
tipos_documento = [
    "Cédula de ciudadanía",
    "Cédula de extranjería",
    "Tarjeta de identidad",
    "Pasaporte",
    "Registro civil de nacimiento",
    "Permiso especial de permanencia",
    "Documento nacional de identidad",
    "Licencia de conducción"
]

# Insertar los tipos en la tabla
for tipo in tipos_documento:
    try:
        cursor.execute(
            "INSERT INTO tipo_documento (nombre, estado) VALUES (%s, %s)",
            (tipo, '1')
        )
    except mysql.connector.errors.IntegrityError as e:
        print(f"❌ Ya existe: {tipo} - {e}")

# Confirmar cambios
conn.commit()
print("✔ Tabla 'tipo_documento' poblada correctamente.")

# Cerrar conexiones
cursor.close()
conn.close()
