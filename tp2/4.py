#4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.
#Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el partido [color del candidato elegido].
#Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar ‘Opción errónea.’
print("Las opciones son:")
print("A) Candidato A por el partido rojo")
print("B) Candidato B por el partido verdad")
print("C) Candidato C por el partido azul")
opcion = input("Ingrese la opción elegida (A, B o C): ")
if opcion == "A":
    color = "rojo"
elif opcion == "B":
    color = "verdad"
elif opcion == "C":
    color = "azul"
else:
    color = None
if color == None:
    print("Opción errónea")
else:
    print("Usted ha votado por el partido", color)
