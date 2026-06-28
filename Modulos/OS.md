# OS

**OS** es un módulo incorporado en la biblioteca estándar de Python que proporciona funciones para interactuar con el sistema operativo. Permite realizar operaciones relacionadas con la gestión de archivos, carpetas, rutas del sistema y variables de entorno de forma portable, lo que significa que el mismo código puede ejecutarse en diferentes sistemas operativos (como Windows, Linux o macOS) con mínimas modificaciones.

## Principales características de OS

1. **Gestión de archivos y directorios:** Permite listar, crear, renombrar, mover y eliminar archivos y carpetas del disco.
2. **Manipulación de rutas:** Mediante el submódulo `os.path`, facilita el trabajo con rutas del sistema de archivos de manera segura, gestionando automáticamente las barras separadoras correspondientes a cada sistema operativo.
3. **Variables de entorno:** Proporciona mecanismos para leer y escribir variables de entorno del sistema operativo.
4. **Información del entorno:** Ofrece detalles sobre el sistema operativo en ejecución, procesos y configuraciones del sistema.

---

## Ejemplos de uso de OS

A continuación se presentan ejemplos que describen el uso del módulo en las tareas cotidianas de administración del sistema de archivos.

### 1. Directorio de trabajo y listado de contenidos

Es posible obtener la ubicación actual del script y explorar los elementos contenidos en una carpeta específica.

```python
import os

# Se obtiene el directorio de trabajo actual (Current Working Directory)
directorio_actual = os.getcwd()
print("Directorio de trabajo actual:", directorio_actual)

# Se listan los archivos y carpetas del directorio actual
elementos = os.listdir(directorio_actual)
print("\nElementos en el directorio:")
for elemento in elementos:
    print("-", elemento)
```

### 2. Creación, renombrado y eliminación de carpetas

El módulo permite estructurar directorios y modificarlos dinámicamente durante la ejecución del programa.

```python
import os

nombre_carpeta = "nueva_carpeta_prueba"

# Se verifica si la carpeta no existe antes de crearla
if not os.path.exists(nombre_carpeta):
    # Se crea una carpeta simple
    os.mkdir(nombre_carpeta)
    print(f"Carpeta '{nombre_carpeta}' creada con éxito.")
else:
    print(f"La carpeta '{nombre_carpeta}' ya existe.")

# Se renombra la carpeta creada
nombre_nuevo = "carpeta_prueba_renombrada"
if os.path.exists(nombre_carpeta):
    os.rename(nombre_carpeta, nombre_nuevo)
    print(f"Carpeta renombrada a '{nombre_nuevo}'.")

# Se elimina la carpeta (debe estar vacía)
if os.path.exists(nombre_nuevo):
    os.rmdir(nombre_nuevo)
    print(f"Carpeta '{nombre_nuevo}' eliminada.")
```

### 3. Manipulación segura de rutas (`os.path`)

El submódulo `os.path` evita errores comunes al concatenar rutas manualmente, adaptándose al sistema operativo en uso (por ejemplo, usando barras `/` en Unix o contrabarras `\` en Windows).

```python
import os

directorio_base = "c:/programacion/proyectos" if os.name == "nt" else "/usr/proyectos"
subcarpeta = "python"
nombre_archivo = "datos.txt"

# Se construye la ruta completa de forma segura
ruta_completa = os.path.join(directorio_base, subcarpeta, nombre_archivo)
print("Ruta construida de forma portable:", ruta_completa)

# Se extrae el nombre del archivo y el directorio contenedor
print("Nombre del archivo:", os.path.basename(ruta_completa))
print("Directorio contenedor:", os.path.dirname(ruta_completa))

# Se verifica si una ruta es un archivo o una carpeta
if os.path.exists(ruta_completa):
    if os.path.isfile(ruta_completa):
        print("La ruta corresponde a un archivo.")
    elif os.path.isdir(ruta_completa):
        print("La ruta corresponde a un directorio.")
else:
    print("La ruta especificada no existe en el sistema de archivos actual.")
```

### 4. Gestión de variables de entorno

Es posible acceder a las configuraciones globales del sistema operativo y definir nuevas variables temporales para la ejecución del script.

```python
import os

# Se obtiene el valor de una variable de entorno común
# Se utiliza el método 'get' para evitar excepciones si la variable no existe
ruta_sistema = os.environ.get("PATH")
print("Contenido de la variable PATH (primeros 100 caracteres):")
print(ruta_sistema[:100] if ruta_sistema else "No disponible")

# Se establece una nueva variable de entorno temporal
os.environ["VERSION_APP"] = "2.5.0"

# Se verifica la variable de entorno recién creada
print("\nVersión de la aplicación registrada en el entorno:", os.environ.get("VERSION_APP"))
```
