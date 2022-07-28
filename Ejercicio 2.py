contraseña = input("Dime la contraseña(Mínimo 8 caracteres sin espacios en blanco): ")
espacios = False #En principio vamos a suponer que no hay espacios en blanco.
if len(contraseña) < 8:#Si la longitud es menor de 8
	print("La contraseña no cumple con el mínimo de longitud.")
else:
	#i es cada uno de los elementos que hay en la variable contraseña
	for i in contraseña:
		#Si hay un espacio
		if i == ' ':
			espacios = True
	if espacios:
		print("La contraseña no puede tener espacios")
	else:
		print("Contraseña correcta.")