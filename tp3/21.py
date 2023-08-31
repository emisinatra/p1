# 21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
mayor = 0
while True:
    numero = int(input("Ingrese un número entero positivo (0 para terminar): "))
    if numero == 0:
        break
    elif numero < 0:
        print("Error: el número debe ser positivo")
    else:
        if numero > mayor:
            mayor = numero
print(f"El mayor número ingresado fue {mayor}")
