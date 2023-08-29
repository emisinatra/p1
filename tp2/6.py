#6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100,
# excepto que también sea divisible por 400.
año = int(input("Ingrese un año: "))
if (año % 4 == 0) and (not (año % 100 == 0) or (año % 400 == 0)):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
