num1 = (int)(input("Dame un número "))
num2 = (int)(input("Dame otro número "))

def devuelveMax(valor1,valor2):
	if valor1 > valor2:
		mayor = "El mayor es el",valor1
	elif valor2 > valor1:
		mayor = "El mayor es el ",valor2
	else:
		mayor = "Son iguales"
	return mayor

resultado = devuelveMax(num1,num2)
print(resultado)
