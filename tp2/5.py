#5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
#Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.
letra = input("Ingrese una letra: ")
if len(letra) != 1:
    print("No se puede procesar el dato")
else:
    if letra.lower() in "aeiou":
        print("Es vocal")
    else:
        print("No es vocal")
