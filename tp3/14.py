#14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.
n1 = int(input("Ingrese el primer número entero: "))
n2 = int(input("Ingrese el segundo número entero: "))
for i in range(n1, n2 + 1):
    if i % 2 == 0:
        print(f"El número {i} es par")
    else:
        print(f"El número {i} es impar")