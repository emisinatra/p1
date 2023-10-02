#7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
def maximo_minimo(lista):
    # Inicializar el máximo y el mínimo con el primer elemento de la lista
    maximo = lista[0]
    minimo = lista[0]
    # Recorrer el resto de la lista
    for i in range(1, len(lista)):
        # Comparar cada elemento con el máximo y el mínimo actual y actualizarlos si es necesario
        if lista[i] > maximo:
            maximo = lista[i]
        if lista[i] < minimo:
            minimo = lista[i]
    # Devolver el máximo y el mínimo como una tupla
    return (maximo, minimo)

# Crear una lista vacía para guardar los números ingresados por teclado
numeros = []
# Crear un bucle para pedir números por teclado hasta que se ingrese un valor no numérico
while True:
    try:
        # Pedir un número por teclado y convertirlo a float
        numero = float(input("Ingrese un número (o cualquier otro valor para terminar): "))
        # Agregar el número a la lista
        numeros.append(numero)
    except:
        # Si se produce una excepción al convertir el valor, salir del bucle
        break
# Si la lista no está vacía, mostrar el máximo y el mínimo usando la función definida
if len(numeros) > 0:
    maximo, minimo = maximo_minimo(numeros)
    print(f"El valor máximo es: {maximo}")
    print(f"El valor mínimo es: {minimo}")
else:
    print("No se ingresaron números.")
