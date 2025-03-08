import tkinter.filedialog

# La función askopenfilename solicita al usuario que seleccione un archivo para abrir.
# tkinter.filedialog.askopenfilename()
# Esta función devuelve la ruta completa al archivo, por lo que podemos usarla cuando llamemos a la función open para abrir ese archivo.

from_filename = tkinter.filedialog.askopenfilename(title="Selecciona el archivo de origen")  # Agregado título en español
# La función asksaveasfilename solicita al usuario que seleccione un archivo para guardar y proporciona una advertencia si el archivo ya existe.

to_filename = tkinter.filedialog.asksaveasfilename(title="Selecciona el archivo de destino")  # Agregado título en español

# Ejemplo
# A continuación, se muestra un programa que copia un archivo, pero coloca "Copia" como la primera línea del archivo copiado.

# Para solicitar un archivo al usuario.

# Ahora podemos abrir el archivo del que queremos leer y obtener el contenido:

from_file = open(from_filename, 'r')
contents = from_file.read()
from_file.close()
# Y podemos abrir el archivo en el que queremos escribir y escribir el contenido:

to_file = open(to_filename, 'w')
to_file.write('Copia\n')  # Tenemos que agregar el salto de línea nosotros mismos.
to_file.write(contents)  # Ahora escribimos el contenido del archivo.
to_file.close()
