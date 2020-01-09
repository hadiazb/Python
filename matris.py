matrizA = []
matrizB = []
matrizC = []

filasA = int(input("Ingresa las filas de A: "))
columnasA = int(input("Ingresa las columnas de A: "))

filasB = int(input("Ingresa las filas de B: "))
columnasB = int(input("Ingresa las columnas de B: "))

if columnasA != filasB:
	print("No existe solucion")

else:
	print ("---------Matris A--------")
	for i in range(filasA):
		for c in range(columnasA):
			  matrizA[i][c] = 0

	for f in range(filasA):
		for c in range(columnasA):
			matrizA[f][c] = int(input("Elemento %d, %d "%(f,c)))

	print ("---------Matris B--------")
	for i in range(filasB):
		matrizB.append([0]*columnasB)
		
	for f in range(filasB):
		for c in range(columnasB):
			matrizB[f][c] = int(input("Elemento %d, %d "%(f,c)))
	print ("------Matrices-------")
	print ('MAtris A\n')
	print (matrisA)
	print ('Matris B\n')
	print (matrisB)