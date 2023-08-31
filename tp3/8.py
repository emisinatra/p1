#8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
n = int(input("Ingrese un número entero: "))
contador = 1
for i in range(1, n + 1):
    for j in range(i):
        print(contador, end=" ")
        contador += 1
    print()