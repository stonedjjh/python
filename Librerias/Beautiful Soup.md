# Beautiful Soup

**Beautiful Soup** es una biblioteca de Python diseñada para extraer información de archivos HTML y XML. Proporciona herramientas sencillas para navegar, buscar y modificar el árbol de elementos de una página web, facilitando tareas de raspado web (web scraping) al convertir documentos HTML complejos en un árbol estructurado de objetos Python.

## Principales características de Beautiful Soup

1. **Facilidad de navegación:** Permite recorrer la estructura jerárquica de un documento HTML utilizando propiedades sencillas de Python (como `.parent`, `.children`, o nombres de etiquetas directas).
2. **Búsqueda flexible:** Facilita la localización de elementos específicos mediante filtros basados en nombres de etiquetas, atributos de clase, identificadores únicos (IDs) y expresiones regulares.
3. **Compatibilidad con analizadores (parsers):** Se integra con múltiples analizadores de Python, incluyendo el analizador integrado `html.parser`, así como bibliotecas externas rápidas y robustas como `lxml` y `html5lib`.
4. **Tolerancia a errores:** Es capaz de procesar HTML mal formateado o con etiquetas sin cerrar, reconstruyendo la estructura de forma lógica.

## Instalación de Beautiful Soup

Para instalar Beautiful Soup y su analizador recomendado (`lxml`), se debe ejecutar el siguiente comando en la consola del sistema:

```bash
pip install beautifulsoup4 lxml
```

## Ejemplos de uso de Beautiful Soup

A continuación se presentan ejemplos prácticos que ilustran cómo analizar y extraer datos de documentos estructurados en HTML.

### 1. Creación de un objeto BeautifulSoup

Para iniciar el análisis, se debe instanciar la clase `BeautifulSoup` pasando el contenido HTML y el analizador correspondiente.

```python
from bs4 import BeautifulSoup

# Se define un fragmento de código HTML de ejemplo
html_ejemplo = """
<html>
  <head>
    <title>Página de Prueba</title>
  </head>
  <body>
    <h1>Bienvenido a la Guía de Beautiful Soup</h1>
    <p class="descripcion">Esta biblioteca facilita la extracción de datos en Python.</p>
    <p class="contenido">El análisis de HTML se realiza de forma rápida y sencilla.</p>
  </body>
</html>
"""

# Se crea el objeto BeautifulSoup utilizando el analizador html.parser
sopa = BeautifulSoup(html_ejemplo, "html.parser")

# Se muestra el título de la página
print("Título de la página:", sopa.title.string)

# Se muestra el contenido formateado jerárquicamente
print("\nHTML Formateado:")
print(sopa.prettify())
```

### 2. Búsqueda de elementos únicos (`find`)

El método `find` busca y devuelve el primer elemento del árbol que coincida con los criterios especificados.

```python
from bs4 import BeautifulSoup

sopa = BeautifulSoup(html_ejemplo, "html.parser")

# Se busca la primera etiqueta <p> que contenga la clase "descripcion"
parrafo_desc = sopa.find("p", class_="descripcion")

if parrafo_desc:
    # Se extrae el texto del elemento
    print("Texto del párrafo de descripción:", parrafo_desc.text)
else:
    print("No se encontró el elemento especificado.")
```

### 3. Búsqueda de múltiples elementos (`find_all`)

El método `find_all` devuelve una lista con todos los elementos que coincidan con los criterios de búsqueda.

```python
from bs4 import BeautifulSoup

sopa = BeautifulSoup(html_ejemplo, "html.parser")

# Se buscan todas las etiquetas <p> en el documento
todos_los_parrafos = sopa.find_all("p")

# Se itera sobre la lista de elementos encontrados
for indice, parrafo in enumerate(todos_los_parrafos, start=1):
    print(f"Párrafo {indice}: {parrafo.text}")
```

### 4. Extracción de atributos (Enlaces y Fuentes)

Es posible acceder a los atributos de un elemento (como `href` en enlaces o `src` en imágenes) tratándolo como si fuera un diccionario de Python.

```python
from bs4 import BeautifulSoup

html_enlaces = """
<div>
  <a href="https://www.python.org" id="link-python">Sitio Oficial de Python</a>
  <a href="https://pypi.org" id="link-pypi">Repositorio PyPI</a>
</div>
"""

sopa = BeautifulSoup(html_enlaces, "html.parser")

# Se buscan todos los enlaces <a>
enlaces = sopa.find_all("a")

for enlace in enlaces:
    # Se extrae el atributo "href" y el texto visible del enlace
    url = enlace.get("href") # También es posible usar: enlace['href']
    texto = enlace.text
    print(f"Enlace: {texto} -> Dirección: {url}")
```

### 5. Navegación por la estructura del documento

Beautiful Soup permite moverse horizontal o verticalmente a través del árbol de elementos.

```python
from bs4 import BeautifulSoup

html_navegacion = """
<ul>
  <li>Elemento A</li>
  <li id="medio">Elemento B</li>
  <li>Elemento C</li>
</ul>
"""

sopa = BeautifulSoup(html_navegacion, "html.parser")

# Se localiza el elemento central
elemento_b = sopa.find("li", id="medio")

# Navegación hacia el elemento padre
padre = elemento_b.parent
print("Nombre de la etiqueta padre:", padre.name)

# Navegación hacia el elemento hermano anterior e inmediato siguiente
hermano_anterior = elemento_b.find_previous_sibling()
hermano_siguiente = elemento_b.find_next_sibling()

print("Hermano anterior:", hermano_anterior.text if hermano_anterior else "Ninguno")
print("Hermano siguiente:", hermano_siguiente.text if hermano_siguiente else "Ninguno")
```
