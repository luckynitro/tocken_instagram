import schedule
import time

def publicar_contenido():
    # Aquí deberías agregar la lógica real para publicar contenido
    print("Publicando contenido...")

# Programar la publicación de contenido cada minuto (para pruebas)
schedule.every(1).minutes.do(publicar_contenido)

while True:
    # Ejecutar tareas programadas
    schedule.run_pending()
    time.sleep(1)

