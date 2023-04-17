# Convertir datos de diccionario en python a JSON

producto = {"nombre":"silla","color":"blanco","precio":80}

import json
# python(diccionario) -> JSON #
estructura_JSON = json.dumps(producto)

'''
Para acceder a los datos json es por posiciones de lista
en python:
estructura_json[0]
'''
print(estructura_JSON[20])

# JSON -> python(diccionario) #
json_pytthon = json.loads(estructura_JSON)
print(json_pytthon)