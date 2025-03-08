#En este enfoque se utiliza el método readline() para leer el archivo línea por línea.
flanders_filename = 'In-Flanders-Fields.txt'
flanders_file = open(flanders_filename, 'r')
line = flanders_file.readline()
while line != '':
	print(line, end='')
	line = flanders_file.readline()
flanders_file.close()


#en este ejemplo imprimimos solo el primer parrafo
flanders_file = open(flanders_filename, 'r')
line = flanders_file.readline()
line = flanders_file.readline()
while not line.startswith('We are the Dead'):
    line = flanders_file.readline()
    print(line, end='')
flanders_file.close()    