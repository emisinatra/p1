#8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña.
#Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”.
#Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
if usuario == "Gwenevere" and contraseña == "excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")
