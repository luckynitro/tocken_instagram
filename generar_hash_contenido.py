import hashlib

def generar_hash_contenido(contenido):
    # Generar un hash único para el contenido
    hash_contenido = hashlib.sha256(contenido.encode()).hexdigest()
    return hash_contenido

# Ejemplo de uso:
contenido1 = "Contenido de la imagen 1"
hash_contenido1 = generar_hash_contenido(contenido1)

# Puedes repetir esto para cada pieza de contenido que desees publicar y monitorear

# Ejemplo de impresión al final del script
print("El script se ejecutó correctamente")
