# ReportLab

**ReportLab** es una biblioteca de Python de alto rendimiento diseñada para la creación y manipulación dinámica de documentos en formato PDF. Permite definir la maquetación y tipografía de los informes mediante código. Para la maquetación avanzada, se utiliza principalmente el componente **PLATYPUS** (Page Layout and Typography Using Scripts), el cual automatiza el diseño de páginas al manejar de forma fluida el flujo de textos, tablas y gráficos.

## Instalación de ReportLab

Al ser una biblioteca de terceros, requiere instalación previa en el entorno mediante el gestor de paquetes de Python:

```bash
pip install reportlab
```

---

## Elementos Fundamentales de PLATYPUS

La biblioteca se estructura en base a elementos de flujo denominados **Flowables** (objetos fluidos). Estos elementos representan las partes individuales del documento (como títulos, párrafos o tablas) que ReportLab organiza automáticamente a lo largo de las páginas.

*   **`SimpleDocTemplate`:** Clase contenedora encargada de definir el archivo PDF de salida y coordinar la construcción general del documento.
*   **`Paragraph`:** Permite insertar bloques de texto enriquecido que se ajustan automáticamente a los márgenes del documento.
*   **`Spacer`:** Genera un espacio en blanco vertical para separar elementos.
*   **`Table`:** Permite maquetar celdas organizadas en filas y columnas.
*   **`Image`:** Inserta imágenes en el documento.

---

## Ejemplos de uso de ReportLab

A continuación se presentan ejemplos que describen los flujos comunes para construir un reporte estructurado.

### 1. Creación de un PDF base con título

Para construir el reporte se debe crear una plantilla con `SimpleDocTemplate` y pasar una lista de elementos fluidos (Flowables) al método `build`.

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Se define el archivo de destino del PDF
reporte = SimpleDocTemplate("inventario_frutas.pdf")

# Se carga la hoja de estilos de ejemplo incorporada en el módulo
estilos = getSampleStyleSheet()

# Se crea un elemento de párrafo utilizando el estilo de encabezado h1
titulo = Paragraph("Inventario Completo de Frutas", estilos["h1"])

# Se construye el archivo PDF pasando una lista con los elementos creados
reporte.build([titulo])
print("PDF inicial generado correctamente.")
```

### 2. Adición de Tablas con Estilo (`Table` y `TableStyle`)

Los datos para una tabla deben organizarse como una lista de listas (matriz bidimensional). A continuación se muestra cómo transformar un diccionario en esta estructura, añadir bordes (GRID) y alinear la tabla.

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Datos de origen en un diccionario
frutas = {
    "Arándanos": 1,
    "Higos": 1,
    "Manzanas": 2,
    "Durianes": 3,
    "Plátanos": 5,
    "Cerezas": 8,
    "Uvas": 13
}

# Se convierte el diccionario en una lista de listas
datos_tabla = []
for fruta, cantidad in frutas.items():
    datos_tabla.append([fruta, cantidad])

# Se crea el objeto de tabla con los datos estructurados
# Se define un borde negro continuo alrededor de todas las celdas (GRID)
# El rango (0,0) a (-1,-1) indica que se aplica desde la primera a la última celda
estilo_tabla = [('GRID', (0,0), (-1,-1), 1, colors.black)]
tabla_reporte = Table(data=datos_tabla, style=estilo_tabla, hAlign="LEFT")

# Reconstrucción del PDF con el título y la tabla
reporte = SimpleDocTemplate("inventario_frutas.pdf")
estilos = getSampleStyleSheet()
titulo = Paragraph("Inventario Completo de Frutas", estilos["h1"])

# Se compila el PDF incluyendo la tabla
reporte.build([titulo, tabla_reporte])
print("PDF con tabla generado correctamente.")
```

### 3. Incorporación de Gráficos (Gráfico Circular)

Los gráficos estadísticos se generan mediante formas geométricas (`Drawing`) a las que se les asocian componentes específicos como `Pie` (gráfico circular). Para definir las dimensiones de forma precisa, se importa la unidad `inch` (pulgada).

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

# Se inicializa el componente del gráfico circular definiendo su tamaño en pulgadas
grafico_pie = Pie(width=3*inch, height=3*inch)

# Se inicializan listas para estructurar los datos y etiquetas ordenados alfabéticamente
grafico_pie.data = []
grafico_pie.labels = []

frutas_ordenadas = {
    "Arándanos": 1,
    "Higos": 1,
    "Manzanas": 2,
    "Durianes": 3,
    "Plátanos": 5,
    "Cerezas": 8,
    "Uvas": 13
}

for nombre in sorted(frutas_ordenadas):
    grafico_pie.data.append(frutas_ordenadas[nombre])
    grafico_pie.labels.append(nombre)

# Los gráficos no son elementos fluidos directos (Flowables); se deben encapsular en un Drawing
contenedor_grafico = Drawing()
contenedor_grafico.add(grafico_pie)

# Se definen los elementos previos
reporte = SimpleDocTemplate("inventario_frutas.pdf")
estilos = getSampleStyleSheet()
titulo = Paragraph("Inventario Completo de Frutas", estilos["h1"])

# Datos de la tabla estructurados previamente
datos_tabla = [[nombre, cantidad] for nombre, cantidad in frutas_ordenadas.items()]
tabla_reporte = Table(data=datos_tabla, style=[('GRID', (0,0), (-1,-1), 1, colors.black)], hAlign="LEFT")

# Se construye el PDF definitivo incluyendo el título, la tabla y el gráfico circular
reporte.build([titulo, tabla_reporte, contenedor_grafico])
print("PDF definitivo con gráfico circular generado correctamente.")
```
