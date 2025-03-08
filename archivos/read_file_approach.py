#En este ejemplo se muestra cómo leer un archivo completo con el método read().
#no usar en archivos muy grandes
flanders_filename = 'In-Flanders-Fields.txt'
flanders_file = open(flanders_filename, 'r')
print(flanders_file.read())
flanders_file.close()    