import mysql.connector
from faker import Faker

# Conexión a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia si es necesario
    database="projectFinal",
    port=3307   
)
cursor = conn.cursor(dictionary=True)
fake = Faker('es_ES')   # Generador de ciudades en español

# Número de ciudades por departamento
ciudades_por_departamento = 2

# Obtener todos los departamentos con su ID
cursor.execute("SELECT depa_id, nombre FROM departamento")
departamentos = cursor.fetchall()

# Insertar ciudades
for dept in departamentos:
    depa_id = dept['depa_id']
    dept_nombre = dept['nombre']
    for i in range(ciudades_por_departamento):
        nombre_ciudad = fake.city()
        try:
            cursor.execute(
                "INSERT INTO ciudad (depa_id, nombre, estado) VALUES (%s, %s, %s)",
                (depa_id, nombre_ciudad, '1')
            )
        except mysql.connector.errors.IntegrityError:
            print(f"Ya existe la ciudad '{nombre_ciudad}' en el departamento '{dept_nombre}'")

# Guardar los cambios
conn.commit()
print("✔ Ciudades insertadas correctamente (2 por departamento).")

# Cerrar conexión
cursor.close()
conn.close()
