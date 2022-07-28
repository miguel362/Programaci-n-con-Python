suma = 0
dar_numero = True
while dar_numero:
	valor = int(input("Dame un número positivo para ir sumando, en caso de negativo se termina el programa: "))
	if valor >= 0:
		print("Me has dado el", valor)
		print("Seguimos jugando...")
		suma = suma + valor
	else:
		print("Me has dado un número negativo. Fin del programa.")
		dar_numero = False
print("El resultado de la suma de todos los números positivos es",suma)