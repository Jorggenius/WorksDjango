import mysql.connector

# Conectar a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia si es necesario
    database="projectFinal",
    port=3307   
)
cursor = conn.cursor(dictionary=True)

# Mapear países a sus departamentos
estructura_departamentos = {
    "Colombia": ["Antioquia", "Cundinamarca", "Valle del Cauca"],
    "Perú": ["Lima", "Cusco", "Arequipa"],
    "Ecuador": ["Pichincha", "Guayas", "Manabí"]
}

# Obtener los IDs reales de los países desde la tabla
cursor.execute("SELECT pais_id, nombre FROM pais")
paises_db = {row['nombre']: row['pais_id'] for row in cursor.fetchall()}

# Insertar departamentos
for pais_nombre, lista_departamentos in estructura_departamentos.items():
    pais_id = paises_db.get(pais_nombre)
    if not pais_id:
        print(f"El país '{pais_nombre}' no se encontró en la base de datos.")
        continue
    for depa in lista_departamentos:
        try:
            cursor.execute(
                "INSERT INTO departamento (pais_id, nombre, estado) VALUES (%s, %s, %s)",
                (pais_id, depa, '1')
            )
        except mysql.connector.errors.IntegrityError:
            print(f"Ya existe el departamento '{depa}' para el país '{pais_nombre}'")

# Guardar cambios
conn.commit()
print("✔ Departamentos insertados correctamente.")

# Cerrar conexión
cursor.close()
conn.close()
