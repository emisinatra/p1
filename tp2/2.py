#2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.
años = int(input("Ingrese el número de años que tiene su computadora: "))
if años < 0:
    print("Error: el número debe ser positivo")
else:
    if años <= 2:
        print("El computador es nuevo")
    else:
        print("El computador es viejo")
