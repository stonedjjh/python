#En este enfoque creamos una lista con las lineas del archivo
flanders_filename = 'In-Flanders-Fields.txt'
flanders_file = open(flanders_filename, 'r')
lines = flanders_file.readlines()

'''

for line in lines:
	print(line, end='')
print(lines)
print(lines[3])
print(line - '\n')
print(line, end='')
print(line.strip())
print(line.rstrip('\n'))
'''

for line in lines:
	print(line, end='')