#9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo,
# y muestre por pantalla el grupo que le corresponde.
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M o F): ")
if sexo == "F" and nombre[0].upper() < "M":
    grupo = "A"
elif sexo == "M" and nombre[0].upper() > "N":
    grupo = "A"
else:
    grupo = "B"
print("Usted pertenece al grupo", grupo)
