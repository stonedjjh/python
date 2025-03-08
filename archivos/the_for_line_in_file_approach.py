#En este archivo se muestra cómo leer un archivo línea por línea con un bucle for.
flanders_filename = 'In-Flanders-Fields.txt'
flanders_file = open(flanders_filename, 'r')
for line in flanders_file:
    print(line, end='')#se coloca end='' para que no se imprima un salto de línea adicional
flanders_file.close()