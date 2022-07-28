'''Crear una aplicación gráfica de tipo CRUD
en la cual conectamos con una base de datos
y podamos introducir un usuario, leer, actualizar y borrar...'''

#Para la interfaz
from tkinter import *
#Para la base de datos
import sqlite3
#Para las ventanas emergentes
from tkinter import messagebox

#Creo el marco
marco = Tk()
marco.title("Base de datos de usuarios")

#Creo la lámina
frame = Frame(marco)
frame.pack()

'''Creo las variables stringvar en los entry para poder trabajaro con lo que se 
escribe en los campos de la bbdd'''

mi_id = StringVar()
mi_nombre = StringVar()
mi_password = StringVar()
mi_apellido = StringVar()
mi_direccion = StringVar()

#Función para preguntar si quiere salir de la aplicación
def salir_aplicacion():
	valor=messagebox.askquestion("Salir","Deseas salir de la aplicación?")
	if valor == "yes":
		marco.destroy()

#Cuando seleccionamos BBDD/Conectar se conecta y crea una bbdd con estas características.
def nueva_base():
	conexion = sqlite3.connect("Base de datos")
	puntero = conexion.cursor()
	#Utilizo un bloque try-except por si al darle a conectar
	#ya está la base de datos creada.
	try:
		puntero.execute("""CREATE TABLE DATOS_USUARIOS(
						ID INTEGER PRIMARY KEY AUTOINCREMENT,
						NOMBRE_USUARIO VARCHAR(25),
						PASSWORD VARCHAR(10),
						APELLIDO VARCHAR(25),
						DIRECCION VARCHAR (100),
						COMENTARIOS VARCHAR(250))""")
		mensaje = messagebox.showinfo("BBDD","BBDD creada con éxito")
	except sqlite3.OperationalError:
		warning = messagebox.showwarning("Atención","La BBDD ya está creada")

#Para borrar todos los campos y que se quede limpia la interfaz
def borra_campos():
	mi_id.set("")
	mi_nombre.set("")
	mi_password.set("")
	mi_apellido.set("")
	mi_direccion.set("")
	cuadro_comentarios.delete("1.0","end")
	cuadro_comentarios.insert(INSERT,"Para leer necesitas poner un valor numérico en el id")
	#Otra opción
	#cuadro_direccion.delete(0,"end")
	#cuadro_id.insert(0,"Campo innecesario")

#Para añadir un usuario a la tabla
def aniadir_usuario():
	#Conecto con la base en la que voy a introducir los datos
	conexion = sqlite3.connect("Base de datos")
	puntero = conexion.cursor()
	'''Una opción para introducir a un usuario
	puntero.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,'" + mi_nombre.get() + 
		"','" + mi_password.get() + "','" + mi_apellido.get() + "','" + 
		mi_direccion.get() + "','" + cuadro_comentarios.get("1.0","end") + "')")'''

	#La opción que yo elijo,lista de tuplas con una sóla tupla y el método
	#executemany para que ejecute lo que hay en la lista	
	datos = mi_nombre.get(),mi_password.get(),mi_apellido.get(),mi_direccion.get(),cuadro_comentarios.get("1.0","end")
	
	puntero.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
	conexion.commit()
	aviso = messagebox.showinfo("Datos usuarios","Usuario introducido")

#Para leer a un usuario
def leer_usuario():
	#Conecto con la base en la que voy a LEER los datos
	conexion = sqlite3.connect("Base de datos")
	puntero = conexion.cursor()

	#Guardo en la variable valor lo que hay en el entry 
	#del id como entero para saber si realmente es un número 
	#lo que han puesto 
	try:
		valor = int(mi_id.get())
		cuadro_comentarios.delete("1.0","end")#Limpio el campo texto por si había algo anteriormente.
		puntero.execute("SELECT * FROM DATOS_USUARIOS WHERE ID LIKE " + mi_id.get())
		
		leido = puntero.fetchall()#Te devuelve un array con los valores de la consulta

		for val in leido:
			mi_nombre.set(val[1])
			mi_password.set(val[2])
			mi_apellido.set(val[3])
			mi_direccion.set(val[4])
			cuadro_comentarios.insert(INSERT,val[5])

		conexion.commit()
	except:
		mi_id.set("")
		mi_nombre.set("")
		mi_password.set("")
		mi_apellido.set("")
		mi_direccion.set("")
		cuadro_comentarios.delete("1.0","end")
		cuadro_comentarios.insert(INSERT,"Para leer necesitas poner un valor numérico en el id")

#Para modificar a un usuario
def modificar_usuario():
	#Conecto con la base en la que voy a MODIFICAR los datos
	conexion = sqlite3.connect("Base de datos")
	puntero = conexion.cursor()
	
	datos = mi_nombre.get(),mi_password.get(),mi_apellido.get(),mi_direccion.get(),cuadro_comentarios.get("1.0","end")
	#Ejecuto la sentencia sql si hay un id puesto
	try:
		'''puntero.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO = '" + mi_nombre.get() + 
					"', PASSWORD ='" + mi_password.get() + 
					"',APELLIDO ='" + mi_apellido.get() + 
					"',DIRECCION ='" + mi_direccion.get() + 
					"',COMENTARIOS ='" + cuadro_comentarios.get("1.0","end") + 
					"'WHERE ID =" + mi_id.get())'''
	
		puntero.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO = ?, PASSWORD=?, APELLIDO=?, DIRECCION=?,COMENTARIOS=? " +
						"WHERE ID="+mi_id.get(),(datos))

		conexion.commit()
		messagebox.showinfo("Datos usuarios","Usuario Modificado con éxito")
	except:
		cuadro_comentarios.delete("1.0","end")
		cuadro_comentarios.insert("1.0","Indica el id del usuario a modificar.")

#Borrar usuario
def borra_usuario():
	#Conecto con la base en la que voy a ELIMINAR los datos
	conexion = sqlite3.connect("Base de datos")
	puntero = conexion.cursor()

	#Mensaje para asegurarnos de que se quiere eliminar al usuario
	valor = messagebox.askquestion("Atención","Seguro que quieres eliminar a este usuario?")

	if valor == "yes":
		puntero.execute("DELETE FROM DATOS_USUARIOS WHERE ID = " + mi_id.get())
		conexion.commit()
		messagebox.showinfo("Datos usuarios","Usuario eliminado con éxito")

#Para la información de la licencia
def licencia():
	messagebox.showinfo("Licencia","Licencia exclusiva de Miguel Navarro")

#Para a cerca de...
def a_cerca_de():
	messagebox.showinfo("A cerca de...","Base de datos de los usuarios de la empresa Mi_Casa S.A. Derechos reservados a los responsables del mantenimiento de la misma.") 

#Creo el menú
menu_marco = Menu(marco)
marco.config(menu=menu_marco)  

#Opciones del menu
bbdd_menu = Menu(menu_marco,tearoff=0)
bbdd_menu.add_command(label="Conectar",command=nueva_base)
bbdd_menu.add_command(label="Salir",command=salir_aplicacion)
borrar_menu = Menu(menu_marco,tearoff=0)
borrar_menu.add_command(label="Borrar campos",command=borra_campos)
crud_menu = Menu(menu_marco,tearoff=0)
crud_menu.add_command(label="Insertar",command=aniadir_usuario)
crud_menu.add_command(label="Leer",command=leer_usuario)
crud_menu.add_command(label="Actualizar",command=modificar_usuario)
crud_menu.add_command(label="Borrar",command=borra_usuario)
ayuda_menu = Menu(menu_marco,tearoff=0)
ayuda_menu.add_command(label="Licencia",command=licencia)
ayuda_menu.add_command(label="A cerca de..",command=a_cerca_de)

#Para que se vea
menu_marco.add_cascade(label="BBDD",menu=bbdd_menu)
menu_marco.add_cascade(label="Borrar",menu=borrar_menu)
menu_marco.add_cascade(label="CRUD",menu=crud_menu)
menu_marco.add_cascade(label="Ayuda",menu=ayuda_menu)

#Labels
identificador = Label(frame,text="id:",width=15)
identificador.grid(row=0,column=0,sticky="e",padx=10,pady=10)
nombre = Label(frame,text="Nombre:",width=15)
nombre.grid(row=1,column=0,sticky="e",padx=10,pady=10)
password = Label(frame,text="Password:",width=15)
password.grid(row=2,column=0,sticky="e",padx=10,pady=10)
apellido = Label(frame,text="Apellido:",width=15)
apellido.grid(row=3,column=0,sticky="e",padx=10,pady=10)
direccion = Label(frame,text="Dirección:",width=15)
direccion.grid(row=4,column=0,sticky="e",padx=10,pady=10)
comentarios = Label(frame,text="Comentarios:",width=15)
comentarios.grid(row=5,column=0,sticky="e",padx=10,pady=10)
#no funciona el parámetro sticky

#Entrys
cuadro_id = Entry(frame,textvariable = mi_id)
cuadro_id.grid(row=0,column=1,padx=10,pady=10)
cuadro_nombre = Entry(frame,textvariable = mi_nombre)
cuadro_nombre.grid(row=1,column=1,padx=10,pady=10)
cuadro_password = Entry(frame,textvariable = mi_password)
cuadro_password.grid(row=2,column=1,padx=10,pady=10)
cuadro_password.config(justify="center",fg="red",show="*")
cuadro_apellido = Entry(frame,textvariable = mi_apellido)
cuadro_apellido.grid(row=3,column=1,padx=10,pady=10)
cuadro_direccion = Entry(frame,textvariable = mi_direccion)
cuadro_direccion.grid(row=4,column=1,padx=10,pady=10)
cuadro_comentarios = Text(frame,width=17,height=5)
cuadro_comentarios.grid(row=5,column=1,padx=10,pady=10)

#Scrollbar para el cuadro de comentarios
scrolbar = Scrollbar(frame,command=cuadro_comentarios.yview)
scrolbar.grid(row=5,column=2,sticky="nsew")
cuadro_comentarios.config(yscrollcommand=scrolbar.set)

#Segundo frame para los botones
frame2 = Frame(marco)
frame2.pack()

#Botones
boton_insertar = Button(frame2,width=5,text="Add",command=aniadir_usuario)
boton_insertar.grid(row=1,column=0,padx=10,pady=10,sticky="e")
boton_read = Button(frame2,width=5,text="Read",command=leer_usuario)
boton_read.grid(row=1,column=1,padx=10,pady=10,sticky="e")
boton_update = Button(frame2,width=5,text="Update",command=modificar_usuario)
boton_update.grid(row=1,column=2,padx=10,pady=10,sticky="e")
boton_delete = Button(frame2,width=5,text="Delete",command=borra_usuario)
boton_delete.grid(row=1,column=3,padx=10,pady=10,sticky="e")

marco.mainloop()