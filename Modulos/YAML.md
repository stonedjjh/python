# YAML

**YAML** (YAML Ain't Markup Language) es un formato de serialización de datos diseñado para ser legible por humanos y fácilmente estructurable. En Python, el módulo `yaml` permite codificar y decodificar información en este formato, facilitando la creación y lectura de archivos de configuración.

---

## Ejemplos de uso de YAML

A continuación se presentan ejemplos que describen cómo utilizar el módulo `yaml` de forma segura.

> [!WARNING]
> Se recomienda emplear siempre las funciones `safe_load` y `safe_dump`. Las funciones estándar `load` y `dump` pueden ejecutar código arbitrario si el contenido procesado no es seguro, por lo que el uso de las variantes `safe` elimina este riesgo de ejecución.

### 1. Serialización y guardado en archivos (`yaml.safe_dump`)

Para volcar estructuras de datos de Python (como listas y diccionarios) en un archivo YAML, se utiliza la función `safe_dump`.

```python
import yaml

# Se definen los datos a guardar
personas = {
    "empleados": [
        {"nombre": "Alicia", "rol": "Desarrolladora"},
        {"nombre": "Roberto", "rol": "Administrador"}
    ]
}

# Se abre el archivo en modo escritura
with open("people.yaml", "w", encoding="utf-8") as archivo_yaml:
    # Se vuelcan los datos en formato YAML en el archivo correspondiente
    yaml.safe_dump(personas, archivo_yaml, default_flow_style=False, sort_keys=False)
    print("Datos serializados y guardados en 'people.yaml'.")
```

### 2. Carga y lectura desde archivos (`yaml.safe_load`)

Para procesar un archivo en formato YAML y convertirlo en una estructura de datos nativa de Python (como un diccionario), se utiliza la función `safe_load`.

```python
import yaml

# Se abre el archivo en modo lectura
try:
    with open("people.yaml", "r", encoding="utf-8") as archivo_yaml:
        # Se cargan los datos estructurados
        datos = yaml.safe_load(archivo_yaml)
        print("Datos cargados desde el archivo:")
        print(datos)
except FileNotFoundError:
    print("El archivo 'people.yaml' no existe.")
```

### 3. Carga desde una cadena de texto

Es posible procesar texto en formato YAML directamente desde una variable o flujo de caracteres.

```python
import yaml

# Se define una cadena con estructura YAML
yaml_cadena = """
proyecto:
  nombre: Autenticación
  version: 1.0
  activo: true
"""

# Se analiza la cadena y se convierte en diccionario
configuracion = yaml.safe_load(yaml_cadena)
print("Versión del proyecto:", configuracion["proyecto"]["version"])
```

### 4. Carga de múltiples documentos (`yaml.safe_load_all`)

Si el archivo contiene varios documentos delimitados por tres guiones (`---`), se puede usar `safe_load_all` para cargarlos secuencialmente.

```python
import yaml

multiples_docs = """
---
id: 101
seccion: A
---
id: 102
seccion: B
"""

# Se genera un iterador con los documentos leídos
documentos = yaml.safe_load_all(multiples_docs)

for doc in documentos:
    print("Documento cargado:", doc)
```
