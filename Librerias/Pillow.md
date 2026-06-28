# Pillow

**Pillow** es la biblioteca estándar de facto para el procesamiento de imágenes en Python. Es una bifurcación (fork) activa y compatible de la biblioteca original PIL (Python Imaging Library). Pillow ofrece soporte para abrir, manipular y guardar una amplia variedad de formatos de archivo de imagen (como PNG, JPEG, GIF, BMP, TIFF, entre otros), además de proveer herramientas para redimensionar, recortar, aplicar filtros y dibujar elementos gráficos.

## Principales características de Pillow

1. **Amplia compatibilidad de formatos:** Facilita la lectura y escritura de múltiples formatos de imagen sin necesidad de convertidores externos.
2. **Manipulación geométrica:** Permite realizar operaciones de transformación como redimensionar, rotar, recortar y transponer imágenes de forma eficiente.
3. **Mejora y filtrado de imágenes:** Incluye filtros predefinidos para ajustar el contraste, brillo, nitidez y aplicar efectos visuales como desenfoque o detección de bordes.
4. **Capacidad de dibujo:** Proporciona un módulo dedicado (`ImageDraw`) para trazar líneas, formas geométricas y superponer texto sobre imágenes existentes o lienzos nuevos.

## Instalación de Pillow

Para instalar la biblioteca Pillow en el sistema, se debe ejecutar el siguiente comando en la terminal:

```bash
pip install pillow
```

## Ejemplos de uso de Pillow

A continuación se presentan ejemplos que describen los flujos de trabajo más comunes al procesar imágenes con Pillow.

### 1. Abrir, mostrar y obtener información de una imagen

El módulo `Image` es el núcleo de la biblioteca y se utiliza para cargar y visualizar archivos de imagen.

```python
from PIL import Image

try:
    # Se abre un archivo de imagen desde el disco
    imagen = Image.open("ejemplo.jpg")
    
    # Se muestran los metadatos de la imagen
    print(f"Formato de la imagen: {imagen.format}")
    print(f"Dimensiones (ancho x alto): {imagen.size}")
    print(f"Modo de color (RGB, RGBA, L, etc.): {imagen.mode}")
    
    # Se despliega la imagen en el visor predeterminado del sistema operativo
    imagen.show()
except FileNotFoundError:
    print("El archivo de imagen especificado no fue encontrado.")
```

### 2. Conversión de formato y guardado

Se puede guardar una imagen en un formato diferente simplemente especificando la extensión correcta en el método `save`.

```python
from PIL import Image

# Se abre una imagen en formato JPEG
imagen = Image.open("ejemplo.jpg")

# Se guarda la imagen en formato PNG
imagen.save("ejemplo_convertido.png", "PNG")
print("Imagen convertida y guardada exitosamente.")
```

### 3. Redimensionar y recortar imágenes

Las dimensiones de una imagen se pueden cambiar utilizando el método `resize`, mientras que secciones específicas se extraen mediante el método `crop`.

```python
from PIL import Image

imagen = Image.open("ejemplo.jpg")

# Redimensionar la imagen a un tamaño específico (300 x 300 píxeles)
# Se pasa una tupla con las nuevas dimensiones
imagen_pequena = imagen.resize((300, 300))
imagen_pequena.save("ejemplo_pequeno.jpg")

# Recortar una sección de la imagen
# Se define una caja delimitadora: (izquierda, superior, derecha, inferior)
caja = (100, 100, 400, 400)
imagen_recortada = imagen.crop(caja)
imagen_recortada.save("ejemplo_recortado.jpg")
print("Operaciones de redimensión y recorte completadas.")
```

### 4. Rotar y voltear (Transponer)

Pillow proporciona métodos para cambiar la orientación física de una imagen.

```python
from PIL import Image

imagen = Image.open("ejemplo.jpg")

# Rotar la imagen 90 grados en sentido antihorario
imagen_rotada = imagen.rotate(90)
imagen_rotada.save("ejemplo_rotado.jpg")

# Voltear la imagen horizontalmente (efecto espejo)
imagen_espejo = imagen.transpose(Image.FLIP_LEFT_RIGHT)
imagen_espejo.save("ejemplo_espejo.jpg")
print("Operaciones de rotación y transposición completadas.")
```

### 5. Aplicación de filtros de imagen

El módulo `ImageFilter` contiene una colección de filtros listos para aplicar a cualquier objeto de imagen.

```python
from PIL import Image, ImageFilter

imagen = Image.open("ejemplo.jpg")

# Se aplica un filtro de desenfoque gaussiano
imagen_difuminada = imagen.filter(ImageFilter.GaussianBlur(radius=2))
imagen_difuminada.save("ejemplo_difuminado.jpg")

# Se aplica un filtro para resaltar los contornos (bordes)
imagen_contornos = imagen.filter(ImageFilter.CONTOUR)
imagen_contornos.save("ejemplo_contornos.jpg")
print("Filtros aplicados y guardados.")
```

### 6. Creación de imágenes y dibujo de gráficos

El módulo `ImageDraw` permite generar nuevas imágenes desde cero y dibujar figuras geométricas o escribir texto sobre ellas.

```python
from PIL import Image, ImageDraw, ImageFont

# Se crea una nueva imagen en modo RGB de 400x200 píxeles con fondo blanco
lienzo = Image.new("RGB", (400, 200), color="white")

# Se crea un objeto de dibujo asociado al lienzo
dibujo = ImageDraw.Draw(lienzo)

# Se dibuja un rectángulo azul
# Caja delimitadora y color de relleno
dibujo.rectangle([(50, 50), (150, 150)], fill="blue", outline="black")

# Se dibuja una elipse roja
dibujo.ellipse([(200, 50), (350, 150)], fill="red", outline="black")

# Se dibuja una línea verde
dibujo.line([(0, 0), (400, 200)], fill="green", width=3)

# Se guarda el lienzo resultante
lienzo.save("lienzo_dibujado.png")
print("Imagen con dibujos geométricos generada exitosamente.")
```
