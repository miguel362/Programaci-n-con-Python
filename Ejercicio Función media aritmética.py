num1 = (int)(input("Dime un número "))
num2 = (int)(input("Dime un segundo número "))
num3 = (int)(input("Dime un tercer número "))

def mediaAritmetica(num1,num2,num3):
	resultado = (num1 + num2 + num3)/3
	#Imprimo el resultado en función de si tiene decimales o no.
	if resultado.is_integer():
		resultadoNuevo = (int)(resultado) 
		print("La media aritmética de ",num1,num2,"y",num3,"es",resultadoNuevo)
	else:
		print("La media aritmética de ",num1,num2,"y",num3,"es",resultado)

mediaAritmetica(num1,num2,num3)
