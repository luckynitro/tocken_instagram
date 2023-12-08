import schedule
import time
import hashlib

def generar_hash_contenido(contenido):
    # Calcula el hash SHA-256 del contenido y lo convierte a formato hexadecimal
    hash_contenido = hashlib.sha256(contenido.encode()).hexdigest()
    return hash_contenido

def almacenar_hash_en_archivo(hash_contenido):
    # Abre el archivo 'hash_archivo.txt' en modo de escritura y agrega el hash
    with open('hash_archivo.txt', 'a') as archivo:
        archivo.write(hash_contenido + '\n')

def publicar_contenido():
    # Ejemplo de contenido que se publicará en Instagram
    contenido_a_publicar = "Contenido para Instagram"

    # Lógica de publicación en Instagram (reemplaza esto con tu propia lógica)
    print(f"Publicando en Instagram: {contenido_a_publicar}")

    # Genera el hash y lo almacena
    hash_del_contenido = generar_hash_contenido(contenido_a_publicar)
    almacenar_hash_en_archivo(hash_del_contenido)

# Programar la publicación de contenido cada minuto (para pruebas)
schedule.every(1).minutes.do(publicar_contenido)

while True:
    # Ejecutar tareas programadas
    schedule.run_pending()
    time.sleep(1)

