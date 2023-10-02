#11.Escribir una función que reciba otra función y una lista,
# y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
def aplicar_funcion(funcion, lista):
    # Crear una lista vacía para guardar el resultado
    resultado = []
    # Recorrer cada elemento de la lista
    for elemento in lista:
        # Aplicar la función al elemento y agregarlo al resultado
        resultado.append(funcion(elemento))
    # Devolver el resultado
    return resultado

# Definir una función de ejemplo que eleva al cuadrado un número
def cuadrado(numero):
    return numero ** 2

# Crear una lista de ejemplo con números enteros
lista = [1, 2, 3, 4, 5]
# Mostrar el resultado de aplicar la función cuadrado a cada elemento de la lista usando la función aplicar_funcion
print(aplicar_funcion(cuadrado, lista))