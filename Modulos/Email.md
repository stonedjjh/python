# Email

El módulo **email** es una herramienta incorporada en la biblioteca estándar de Python que permite construir, analizar y manipular mensajes de correo electrónico. Aunque los correos electrónicos se visualizan de manera sencilla en los clientes de mensajería, internamente corresponden a estructuras de texto complejas reguladas por los estándares **SMTP** (Simple Mail Transfer Protocol) y **MIME** (Multipurpose Internet Mail Extensions). Al ser un componente nativo, no requiere instalación adicional.

---

## Estructura de un Correo Electrónico

Los mensajes de correo electrónico se dividen en dos secciones principales:

1. **Cabeceras (Headers):** Pares de clave-valor que contienen metadatos e instrucciones de enrutamiento utilizados por servidores y clientes de correo (como el remitente, destinatario y asunto).
2. **Cuerpo (Body):** El contenido principal del mensaje (texto plano, HTML, o datos adjuntos).

---

## Ejemplos de uso del módulo Email

A continuación se detalla el proceso para estructurar un correo electrónico utilizando la clase `EmailMessage`.

### 1. Inicialización del mensaje

Para crear un mensaje de correo electrónico vacío, se importa e instancia la clase `EmailMessage` perteneciente al submódulo `email.message`.

```python
from email.message import EmailMessage

# Se crea un objeto de mensaje vacío
mensaje = EmailMessage()

# La impresión del objeto vacío mostrará una estructura sin contenido
print(mensaje)
```

### 2. Configuración de Cabeceras (`From`, `To` y `Subject`)

Los campos de cabecera se configuran tratando al objeto `EmailMessage` como si fuera un diccionario de Python, asignando valores a claves específicas.

```python
from email.message import EmailMessage

mensaje = EmailMessage()

# Se definen las variables para el remitente y el destinatario
remitente = "me@example.com"
destinatario = "you@example.com"

# Se asignan los valores a las cabeceras estándar
mensaje["From"] = remitente
mensaje["To"] = destinatario
mensaje["Subject"] = f"Saludos de {remitente} para {destinatario}"

# Al imprimir el objeto, se visualizan las cabeceras estructuradas
print(mensaje)
```

**Salida en consola:**
```text
From: me@example.com
To: you@example.com
Subject: Saludos de me@example.com para you@example.com
```

### 3. Definición del cuerpo del mensaje (`set_content`)

Para agregar el contenido de texto principal al correo, se utiliza el método `set_content`. Este método también añade de forma automática cabeceras necesarias para la interpretación del formato.

```python
from email.message import EmailMessage

mensaje = EmailMessage()
mensaje["From"] = "me@example.com"
mensaje["To"] = "you@example.com"
mensaje["Subject"] = "Mensaje de prueba"

# Se define el texto del cuerpo
cuerpo = """Hola:

Se está aprendiendo a enviar correos electrónicos utilizando Python."""

# Se establece el contenido en el objeto de mensaje
mensaje.set_content(cuerpo)

# Se muestra el mensaje final estructurado
print(mensaje)
```

**Salida en consola:**
```text
From: me@example.com
To: you@example.com
Subject: Mensaje de prueba
MIME-Version: 1.0
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 8bit

Hola:

Se está aprendiendo a enviar correos electrónicos utilizando Python.
```

> [!NOTE]
> El método `set_content` añade automáticamente las cabeceras `Content-Type` (que define el formato del texto y la codificación `utf-8`) y `Content-Transfer-Encoding` (que indica cómo se interpretan los bytes del mensaje), garantizando que el cliente de correo del destinatario decodifique los caracteres especiales correctamente.

### 4. Adición de archivos adjuntos (MIME y `mimetypes`)

Los correos electrónicos se componen únicamente de caracteres de texto. Para adjuntar archivos binarios (como imágenes, PDFs o audios), se debe codificar su contenido en texto y etiquetarlos con el tipo MIME correcto.

Si se desconoce el tipo de archivo, se puede emplear el módulo estándar `mimetypes` para deducirlo a partir del nombre o la ruta del archivo.

```python
import os
import mimetypes
from email.message import EmailMessage

mensaje = EmailMessage()
mensaje["From"] = "me@example.com"
mensaje["To"] = "you@example.com"
mensaje["Subject"] = "Envío de reporte"
mensaje.set_content("Se adjunta la imagen correspondiente al reporte.")

# Se define la ruta del archivo a adjuntar
ruta_adjunto = "ejemplo.png"
nombre_archivo = os.path.basename(ruta_adjunto)

# Se adivina el tipo y subtipo MIME del archivo (ejemplo salida: 'image/png')
tipo_completo, _ = mimetypes.guess_type(ruta_adjunto)

# Se divide en tipo principal ('image') y subtipo ('png')
tipo_principal, subtipo = tipo_completo.split('/', 1)

# Se lee el archivo en modo binario ("rb")
with open(ruta_adjunto, 'rb') as archivo_binario:
    # Se añade el adjunto al objeto del mensaje
    mensaje.add_attachment(
        archivo_binario.read(),
        maintype=tipo_principal,
        subtype=subtipo,
        filename=nombre_archivo
    )

# La impresión del mensaje mostrará una estructura compuesta
print(mensaje)
```

> [!NOTE]
> Al añadir archivos adjuntos, el tipo de contenido general del correo cambia automáticamente a `Content-Type: multipart/mixed`, sirviendo como contenedor para las diferentes secciones individuales (el texto plano y la imagen codificada en base64).

### 5. Envío de correos electrónicos mediante SMTP (`smtplib`)

El envío físico del mensaje estructurado a través de la red se realiza empleando el protocolo **SMTP** (Simple Mail Transfer Protocol) a través del módulo incorporado `smtplib`.

Para interactuar con servidores remotos que exigen cifrado y autenticación de seguridad, se utiliza la clase `SMTP_SSL` junto con el módulo `getpass` para ocultar la escritura de credenciales en pantalla.

```python
import smtplib
import getpass

# Se crea la conexión segura SSL/TLS con el servidor SMTP externo
# (Se debe reemplazar por la dirección del servidor de correo del usuario)
servidor_correo = smtplib.SMTP_SSL("smtp.ejemplo.com")

# Opcional: Se habilita la depuración detallada para monitorizar la comunicación de red
servidor_correo.set_debuglevel(1)

# Se solicita la contraseña del remitente de forma segura en la consola
contrasena = getpass.getpass("Ingrese la contraseña del correo: ")

# Se inicia sesión en el servidor con el usuario y la contraseña
remitente = "me@example.com"
servidor_correo.login(remitente, contrasena)

# Se envía el mensaje estructurado de tipo EmailMessage
# El método devuelve un diccionario con los destinatarios rechazados
errores = servidor_correo.send_message(mensaje)
print("Errores en el envío:", errores)

# Se cierra la conexión de red de forma limpia
servidor_correo.quit()
```

