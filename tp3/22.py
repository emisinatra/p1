#22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
pares = 0
while True:
    numero = int(input("Ingrese un número entero positivo (-1 para terminar): "))
    if numero == -1:
        break
    elif numero < 0:
        print("Error: el número debe ser positivo")
    else:
        suma = 0
        for digito in str(numero):
            suma += int(digito)
        print(f"La suma de los dígitos de {numero} es {suma}")
        if numero % 2 == 0:
            pares += 1
print(f"Ha ingresado {pares} números pares")