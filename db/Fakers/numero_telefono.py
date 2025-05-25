import mysql.connector
from faker import Faker

fake = Faker('es_CO')  # Puedes usar 'es_ES' si prefieres

# Conexión a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Cambia si es necesario
    database="projectFinal",
    port=3307   
)
cursor = conn.cursor()

# Cantidad de números a insertar
cantidad_numeros = 60
numeros_generados = set()

print("Generando números telefónicos únicos...")

while len(numeros_generados) < cantidad_numeros:
    numero = fake.unique.phone_number()
    numeros_generados.add(numero)

# Insertar en la tabla
for numero in numeros_generados:
    try:
        cursor.execute(
            "INSERT INTO numero_telefono (numero, estado) VALUES (%s, %s)",
            (numero, '1')
        )
    except mysql.connector.errors.IntegrityError:
        print(f"Número duplicado (omitido): {numero}")

# Confirmar cambios
conn.commit()
print(f"✔ Se insertaron {len(numeros_generados)} números telefónicos.")
cursor.close()
conn.close()
