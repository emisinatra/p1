# Modificar el ejercicio 1 para ordenar la lista de números en orden descendente utilizando el método de ordenamiento de burbuja

# Definir una función que implementa el ordenamiento de burbuja inverso
def bubble_sort_reverse(lista):
  # Obtener la longitud de la lista
  n = len(lista)
  # Recorrer la lista n - 1 veces
  for i in range(n - 1):
    # Recorrer la lista desde el inicio hasta el final - i - 1
    for j in range(n - i - 1):
      # Comparar el elemento actual con el siguiente
      if lista[j] < lista[j + 1]:
        # Intercambiar los elementos si el actual es menor que el siguiente
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
  # Devolver la lista ordenada en orden descendente
  return lista

# Definir una lista de números como entrada
lista = [5, 3, 8, 2, 9, 4, 7, 6, 1]
# Llamar a la función de ordenamiento de burbuja inverso con la lista como argumento
lista_ordenada = bubble_sort_reverse(lista)
# Imprimir la lista ordenada en orden descendente
print(lista_ordenada)
