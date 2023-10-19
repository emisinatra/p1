# Definir una función que implementa el ordenamiento de burbuja
def bubble_sort(lista):
  # Obtener la longitud de la lista
  n = len(lista)
  # Recorrer la lista n - 1 veces
  for i in range(n - 1):
    # Recorrer la lista desde el inicio hasta el final - i - 1
    for j in range(n - i - 1):
      # Comparar el elemento actual con el siguiente
      if lista[j] > lista[j + 1]:
        # Intercambiar los elementos si el actual es mayor que el siguiente
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
  # Devolver la lista ordenada
  return lista

# Definir una lista de números como entrada
lista = [5, 3, 8, 2, 9, 4, 7, 6, 1]
# Llamar a la función de ordenamiento de burbuja con la lista como argumento
lista_ordenada = bubble_sort(lista)
# Imprimir la lista ordenada
print(lista_ordenada)
