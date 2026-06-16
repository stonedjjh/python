# Guía Rápida de Python: Herramientas del Día a Día

Esta guía cubre los comandos esenciales y flujos de trabajo que todo desarrollador de Python necesita para configurar entornos, gestionar paquetes y asegurar la portabilidad de sus proyectos.

---

## 1. Instalación y Verificación

### Instalación de Python

- **Windows**: Descarga el instalador oficial desde python.org. **CRUCIAL**: Asegúrate de marcar la casilla **"Add python.exe to PATH"** antes de hacer clic en _Install Now_.
- **Linux (Ubuntu/Debian)**: Normalmente ya viene instalado. Puedes actualizarlo o instalarlo usando la terminal:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Verificar la Versión de Python

Para comprobar que Python se instaló correctamente y ver qué versión tienes, ejecuta en tu terminal (PowerShell/CMD en Windows o Terminal en Linux):

```bash
python --version
```

Nota: En algunos sistemas Linux/macOS, el comando puede requerir especificar el 3:

```bash
python3 --version
```

## 2. Gestión de Entornos Virtuales

Un entorno virtual aísla las librerías de tu proyecto para evitar conflictos globales en tu sistema.

### En Windows (PowerShell o CMD)

Crear el entorno virtual (llamado env o .venv por convención):

```powershell
python -m venv env
```

Activar el entorno:
En PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

(Si da error de permisos, ejecuta antes: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`)

En CMD:

```cmd
.\env\Scripts\activate.bat
```

Desactivar el entorno:

```bash
deactivate
```

### En Linux / macOS

Crear el entorno virtual:

```bash
python3 -m venv env
```

(Si Linux te arroja un error solicitando una dependencia, instálala con: `sudo apt install python3-venv` y vuelve a intentar).

Activar el entorno:

```bash
source env/bin/activate
```

Desactivar el entorno:

```bash
deactivate
```

> [!Tip]
> Sabrás que el entorno está activo porque verás su nombre entre paréntesis al inicio de la línea de tu terminal, por ejemplo: `(env) user@machine:~$`.

### Verificar si el entorno está activo (Diagnóstico)

Un error muy común es instalar paquetes creyendo que el entorno está activo, cuando en realidad se están instalando de forma global. Para confirmar de dónde se está ejecutando Python realmente:

- **Windows**: `where python`
- **Linux**: `which python`

El primer resultado que te devuelva este comando debería ser una ruta que apunte a la carpeta `env` o `.venv` de tu proyecto.

## 3. ¿Qué es PIP y cómo gestionarlo?

PIP (Pip Installs Packages) es el gestor de paquetes oficial de Python. Te permite descargar, instalar y administrar librerías adicionales que no vienen incluidas en la biblioteca estándar de Python (como requests, pandas, django, etc.).

### Cómo actualizar PIP

Es buena práctica mantener PIP actualizado para evitar problemas de compatibilidad o seguridad al descargar paquetes:

En Windows:

```bash
python -m pip install --upgrade pip
```

En Linux / macOS:

```bash
python3 -m pip install --upgrade pip
```

## 4. Control de Librerías y Archivo requirements.txt

### Ver las librerías instaladas

Para ver un listado de todos los paquetes instalados en tu entorno actual (con sus versiones específicas):

```bash
pip list
```

Alternativamente, para verlo en el formato limpio que requiere un archivo de dependencias:

```bash
pip freeze
```

### Cómo crear un requirements.txt

El archivo `requirements.txt` es el estándar en la industria para compartir las dependencias de tu proyecto con otros desarrolladores o servidores de producción.
Para guardar automáticamente todo lo instalado en tu entorno actual dentro de este archivo, ejecuta:

```bash
pip freeze > requirements.txt
```

### Cómo instalar dependencias desde un requirements.txt

Cuando descargas el proyecto de otra persona (o clonas un repositorio), puedes instalar todas las librerías necesarias de golpe con un solo comando:

```bash
pip install -r requirements.txt
```

### Desinstalar y Actualizar Paquetes

Si necesitas eliminar una librería que ya no usas para limpiar tu entorno:

```bash
pip uninstall <nombre_paquete>
```

Para actualizar un paquete específico a su última versión disponible:

```bash
pip install --upgrade <nombre_paquete>
```

## 5. El "Cheat Sheet" del Día a Día (Resumen)

| Acción                        | Comando                                               |
| ----------------------------- | ----------------------------------------------------- |
| Verificar versión             | `python --version`                                    |
| Crear entorno                 | `python -m venv env`                                  |
| Activar (Windows)             | `.\env\Scripts\Activate.ps1`                          |
| Activar (Linux)               | `source env/bin/activate`                             |
| Diagnóstico del entorno       | `where python (Win) / which python (Lin)`             |
| Listar paquetes instalados    | `pip list`                                            |
| Instalar paquete              | `pip install <nombre_paquete>`                        |
| Desinst/Actualizar paquete    | `pip uninstall <paq>` / `pip install --upgrade <paq>` |
| Actualizar PIP                | `python -m pip install --upgrade pip`                 |
| Generar archivo de requisitos | `pip freeze > requirements.txt`                       |
| Instalar desde archivo        | `pip install -r requirements.txt`                     |
| Desactivar entorno            | `deactivate`                                          |

## 6. Recomendaciones para el archivo `.gitignore`

Cuando trabajas con Git (por ejemplo, publicando tu código en GitHub), es crucial evitar subir archivos innecesarios, pesados o que contengan información sensible (como claves API).

Crea un archivo llamado `.gitignore` en la raíz de tu proyecto e incluye las siguientes reglas básicas para Python:

```text
# Entornos virtuales (¡NUNCA los subas al repositorio!)
env/
venv/
.venv/

# Archivos compilados y caché de Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Variables de entorno y secretos locales
.env

# Archivos de configuración de editores/IDEs
.vscode/
.idea/

# Archivos del sistema operativo
.DS_Store
Thumbs.db
```

## 7. Variables de Entorno (Uso del `.env`)

Para proteger información sensible como contraseñas de bases de datos, tokens o claves de API (que evitamos subir al repositorio gracias al `.gitignore`), usamos variables de entorno. El estándar de la industria en Python es la librería `python-dotenv`.

### Instalación

```bash
pip install python-dotenv
```

### Uso básico

1. Crea un archivo `.env` en la raíz de tu proyecto y coloca tus secretos:

   ```text
   API_KEY=tu_clave_secreta_super_segura
   PORT=8080
   ```

2. Carga y usa estas variables en tu código de Python:

```python
import os
from dotenv import load_dotenv

# Carga las variables desde el archivo .env al entorno de Python
load_dotenv()

# Obtiene el valor de la variable
api_key = os.getenv("API_KEY")
puerto = os.getenv("PORT")

print(f"Iniciando en el puerto {puerto}...")
```
