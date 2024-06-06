import json

def enviar_mensaje(profesor, asunto, contenido, remitente, datos_mensajes):
    mensaje = {
        "asunto": asunto,
        "contenido": contenido,
        "remitente": remitente
    }
    if profesor in datos_mensajes:
        datos_mensajes[profesor].append(mensaje)
    else:
        datos_mensajes[profesor] = [mensaje]

def mostrar_mensajes(profesor, datos_mensajes):
    if profesor in datos_mensajes:
        print(f"Mensajes para {profesor}:")
        for mensaje in datos_mensajes[profesor]:
            print(f"Asunto: {mensaje['asunto']}")
            print(f"Contenido: {mensaje['contenido']}")
            print(f"Remitente: {mensaje['remitente']}")
            print()