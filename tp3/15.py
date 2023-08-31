#Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
n = int(input("Ingrese un número entero mayor que cero: "))
if n <= 0:
    print("Error: el número debe ser mayor que cero")
else:
    print(f"Los divisores de {n} son:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)