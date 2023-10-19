# Definir una función que implementa el ordenamiento de selección
def selection_sort(lista):
  # Obtener la longitud de la lista
  n = len(lista)
  # Recorrer la lista desde el inicio hasta el final - 1
  for i in range(n - 1):
    # Asignar el índice del elemento más pequeño al primer elemento del subarreglo no ordenado
    min_index = i
    # Recorrer el subarreglo no ordenado desde el segundo elemento hasta el final
    for j in range(i + 1, n):
      # Comparar el elemento actual con el más pequeño
      if lista[j] < lista[min_index]:
        # Actualizar el índice del elemento más pequeño si el actual es menor que el más pequeño
        min_index = j
    # Intercambiar el primer elemento del subarreglo no ordenado con el más pequeño
    lista[i], lista[min_index] = lista[min_index], lista[i]
  # Devolver la lista ordenada
  return lista

# Definir una lista de palabras como entrada
lista = ["hola", "mundo", "python", "bing", "ordenamiento"]
# Llamar a la función de ordenamiento de selección con la lista como argumento
lista_ordenada = selection_sort(lista)
# Imprimir la lista ordenada
print(lista_ordenada)
