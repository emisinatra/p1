#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
n = int(input("Ingrese un número entero: "))
primo = True
if n < 2:
    primo = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break
if primo:
    print(f"El número {n} es primo")
else:
    print(f"El número {n} no es primo")