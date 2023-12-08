import requests

def enviar_invitacion(usuario_id, token_acceso):
    url = f'https://graph.instagram.com/v13.0/{usuario_id}/relationships'
    parametros = {
        'access_token': token_acceso,
        'action': 'follow',
    }

    try:
        respuesta = requests.post(url, params=parametros)
        respuesta.raise_for_status()
        print(f"Invitación enviada a {usuario_id}")
    except requests.exceptions.HTTPError as err:
        print(f"Error al enviar la invitación a {usuario_id}: {err}")

# Ejemplo de uso con la URL de perfil
url_perfil_destino = 'https://www.instagram.com/marisolvrs/'
token_acceso = 'EAAGEJSwSZCwIBOZCpR1LFMdolvZCDKMAkrS4YL03aKEeO3Q6V1ZBmvX4ZA3h49'

# Obtén el ID de usuario de la URL del perfil
usuario_id_destino = url_perfil_destino.split('/')[-2]

# Luego, puedes usar la función con el usuario de destino y el token de acceso
enviar_invitacion(usuario_id_destino, token_acceso)

