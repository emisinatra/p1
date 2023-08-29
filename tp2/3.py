#3-	Solicitar al usuario que ingrese los nombres de dos personas,
# los cuales se almacenarán en dos variables.
# A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra.
# Si no es así, imprimir ‘no hay coincidencia’.
nombre1 = input("Ingrese el nombre de la primera persona: ")
nombre2 = input("Ingrese el nombre de la segunda persona: ")
if nombre1[0].upper() == nombre2[0].upper():
    print("Coincidencia")
else:
    print("No hay coincidencia")
