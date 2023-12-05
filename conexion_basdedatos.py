import cx_Oracle
import hashlib

# Conectar a la base de datos Oracle
connection = cx_Oracle.connect("digitlaobjetivo10@gmail.com", "Ladrondemierda21+", "host:puerto/servicio")

# Crear un cursor
cursor = connection.cursor()

# Generar un hash único para el contenido
contenido = b"mi_contenido_a_hash"
hash_contenido = hashlib.sha256(contenido).hexdigest()

# Insertar el hash en la base de datos junto con otros datos
cursor.execute("INSERT INTO tu_tabla (hash_contenido, otros_campos) VALUES (:1, :2)", (hash_contenido, "otros_valores"))

# Confirmar los cambios y cerrar la conexión
connection.commit()
cursor.close()
connection.close()
