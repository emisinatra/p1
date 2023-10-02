#15.	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total.
# Utilizar una o más funciones, según sea necesario.
def factorial(numero):
    # Inicializar el factorial en uno
    factorial = 1
    # Recorrer los números desde uno hasta el número dado
    for i in range(1, numero + 1):
        # Multiplicar el factorial por el número actual
        factorial *= i
    # Devolver el factorial
    return factorial

# Inicializar la cantidad de números leídos en cero
cantidad = 0
# Crear un bucle para pedir números por teclado hasta que se ingrese un valor no numérico
while True:
    try:
        # Pedir un número por teclado y convertirlo a entero
        numero = int(input("Ingrese un número (o cualquier otro valor para terminar): "))
        # Mostrar el factorial del número usando la función definida
        print(f"El factorial de {numero} es: {factorial(numero)}")
        # Incrementar la cantidad de números leídos en uno
        cantidad += 1
    except:
        # Si se produce una excepción al convertir el valor, salir del bucle
        break
# Mostrar la cantidad de números leídos en total
print(f"Se leyeron {cantidad} números en total.")
