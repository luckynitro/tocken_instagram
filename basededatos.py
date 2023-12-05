import sqlite3

# Conectar a la base de datos SQLite o crearla si no existe
connection = sqlite3.connect("mi_base_de_datos.db")

# Crear un cursor
cursor = connection.cursor()

# Crear una tabla en la base de datos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tu_tabla (
        id INTEGER PRIMARY KEY,
        hash_contenido TEXT,
        otros_campos TEXT
    )
''')

# Confirmar los cambios y cerrar la conexión
connection.commit()
connection.close()

