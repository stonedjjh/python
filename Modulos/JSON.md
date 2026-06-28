# JSON

**JSON** (JavaScript Object Notation) es un módulo incorporado en la biblioteca estándar de Python que permite la codificación y decodificación de datos en formato JSON. Al ser un formato estándar ligero y legible para el intercambio de datos, este módulo facilita la comunicación entre aplicaciones y el almacenamiento estructurado de información. No requiere instalación adicional.

## Conversión de Datos (Mapeo)

El módulo realiza una traducción automática de los tipos de datos al serializar y deserializar información:

| Tipo en Python | Tipo en JSON |
| :--- | :--- |
| `dict` | `object` |
| `list`, `tuple` | `array` |
| `str` | `string` |
| `int`, `float` | `number` |
| `True` | `true` |
| `False` | `false` |
| `None` | `null` |

---

## Ejemplos de uso de JSON

A continuación se presentan ejemplos que ilustran cómo codificar y decodificar datos en formato JSON.

### 1. Serialización a cadena de texto (`json.dumps`)

La conversión de un objeto de Python (como un diccionario) en una cadena de texto estructurada en formato JSON se realiza mediante la función `dumps`.

```python
import json

# Se define un diccionario con datos de prueba
datos_usuario = {
    "nombre": "Carlos Gómez",
    "edad": 34,
    "es_administrador": True,
    "habilidades": ["Python", "SQL", "Git"],
    "certificaciones": None
}

# Se convierte el diccionario en una cadena JSON
# indent: Añade sangría para mejorar la legibilidad (formateo estético)
# sort_keys: Ordena alfabéticamente las claves del diccionario
# ensure_ascii: Permite representar caracteres especiales (como acentos o la ñ) correctamente
cadena_json = json.dumps(datos_usuario, indent=4, sort_keys=True, ensure_ascii=False)

print("Cadena JSON resultante:")
print(cadena_json)
print("Tipo de dato resultante:", type(cadena_json))
```

### 2. Escritura directa en un archivo (`json.dump`)

Para almacenar la información directamente en un archivo físico del disco sin pasar por una cadena de texto intermedia, se utiliza la función `dump`.

```python
import json

datos_config = {
    "puerto": 8080,
    "depuracion": False,
    "servidor": "localhost"
}

# Se abre el archivo en modo escritura con codificación UTF-8
with open("configuracion.json", "w", encoding="utf-8") as archivo:
    # Se guarda el diccionario directamente en el archivo
    json.dump(datos_config, archivo, indent=4)
    print("Datos de configuración guardados con éxito.")
```

### 3. Deserialización desde una cadena de texto (`json.loads`)

El proceso inverso (convertir una cadena de texto JSON en una estructura nativa de Python, como un diccionario) se realiza mediante `loads`.

```python
import json

# Se define una cadena de texto que contiene una estructura JSON
json_texto = '{"id": 105, "producto": "Teclado Mecánico", "precio": 79.99, "disponible": true}'

# Se convierte la cadena de texto en un diccionario de Python
datos_producto = json.loads(json_texto)

print("Diccionario de Python obtenido:", datos_producto)
print("Acceso al nombre del producto:", datos_producto["producto"])
print("Tipo de dato obtenido:", type(datos_producto))
```

### 4. Lectura directa desde un archivo (`json.load`)

Para cargar la estructura de datos directamente desde un archivo JSON del disco, se utiliza la función `load`.

```python
import json

# Se abre el archivo JSON en modo lectura
try:
    with open("configuracion.json", "r", encoding="utf-8") as archivo:
        # Se cargan los datos y se convierten en un objeto Python
        config = json.load(archivo)
        print("Datos cargados desde el archivo:")
        print(config)
        print("Puerto:", config.get("puerto"))
except FileNotFoundError:
    print("El archivo 'configuracion.json' no existe.")
```
