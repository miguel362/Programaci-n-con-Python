pideNumeros = True
valor = 0
while pideNumeros:
	print("El número que tengo es el",valor)
	numero = int(input("Dame un número mayor, si me das uno menor terminamos el programa..."))
	if numero > valor:
		print("Me has dado el ",numero)
		print("Seguimos jugando...")
		valor = numero
	elif numero < valor:
		print("Me has dado un número menor. Programa finalizado")
		break