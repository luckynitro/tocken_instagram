import requests

def generar_contenido_dinamico():
    response = requests.get('https://picsum.photos/800/600')
    with open('imagen.jpg', 'wb') as f:
        f.write(response.content)

if __name__ == "__main__":
    generar_contenido_dinamico()
