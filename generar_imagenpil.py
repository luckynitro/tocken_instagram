import schedule
import time
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont

# Función para generar una imagen con texto
def generar_imagen(contenido):
    imagen = Image.new('RGB', (800, 600), color='white')
    dibujo = ImageDraw.Draw(imagen)
    fuente = ImageFont.load_default()
    dibujo.text((10, 10), contenido, fill='black', font=fuente)
    imagen.save('imagen_generada.jpg')

# Función para publicar contenido en Instagram
def publicar_contenido():
    # Generar la imagen con el contenido
    contenido_a_subir = "Contenido que vas a subir a Instagram"
    generar_imagen(contenido_a_subir)

    # Subir la imagen a Instagram
    media_path = 'imagen_generada.jpg'
    caption = 'Descripción de la publicación'

    # Aquí deberías agregar la lógica real para subir la imagen a Instagram
    # Reemplaza esta línea con tu código real de publicación en Instagram
    print(f"Subiendo {media_path} a Instagram con la descripción: {caption}")

# Obtener la hora actual
hora_actual = datetime.now().time()

# Calcular la hora para la primera publicación (por ejemplo, 14:30)
hora_programada = datetime.strptime('14:30', '%H:%M').time()

# Calcular el tiempo hasta la próxima publicación
tiempo_hasta_proxima_publicacion = datetime.combine(datetime.today(), hora_programada) - datetime.combine(datetime.today(), hora_actual)

# Programar la primera publicación para la hora programada
schedule.every().day.at(str(hora_programada)).do(publicar_contenido)

while True:
    # Ejecutar tareas programadas
    schedule.run_pending()
    time.sleep(1)

