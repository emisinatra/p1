#9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contraseña = "1234"
intentos = 3
while intentos > 0:
    entrada = input("Ingrese la contraseña: ")
    if entrada == contraseña:
        print("Contraseña correcta")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Le quedan {intentos} intentos.")
if intentos == 0:
    print("Se acabaron los intentos. Acceso denegado.")
