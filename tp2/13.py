#13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
# Haciendo que el programa avise cuando se escriben valores negativos o nulos.
n1 = int(input("Ingrese el primer número entero: "))
n2 = int(input("Ingrese el segundo número entero: "))
if n1 <= 0 or n2 <= 0:
    print("Error: los números deben ser positivos y distintos de cero")
else:
    if n1 > n2:
        if n1 % n2 == 0:
            print(n1, "es múltiplo de", n2)
        else:
            print(n1, "no es múltiplo de", n2)
    else:
        if n2 % n1 == 0:
            print(n2, "es múltiplo de", n1)
        else:
            print(n2, "no es múltiplo de", n1)
