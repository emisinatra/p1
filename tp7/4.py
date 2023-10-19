# Definir una función que implementa el ordenamiento de inserción
def insertion_sort(lista):
  # Obtener la longitud de la lista
  n = len(lista)
  # Recorrer la lista desde el segundo elemento hasta el final
  for i in range(1, n):
    # Asignar el elemento actual a una variable temporal
    temp = lista[i]
    # Asignar el índice del elemento anterior al actual a una variable auxiliar
    j = i - 1
    # Recorrer el subarreglo ordenado desde el final hasta el inicio mientras el elemento temporal sea menor que el elemento actual
    while j >= 0 and len(temp) < len(lista[j]):
      # Desplazar el elemento actual una posición a la derecha
      lista[j + 1] = lista[j]
      # Decrementar el índice auxiliar en uno
      j -= 1
    # Insertar el elemento temporal en la posición correcta
    lista[j + 1] = temp
  # Devolver la lista ordenada por longitud
  return lista

# Definir una lista de cadenas como entrada
lista = ["hola", "mundo", "python", "bing", "ordenamiento"]
# Llamar a la función de ordenamiento de inserción con la lista como argumento
lista_ordenada = insertion_sort(lista)
# Imprimir la lista ordenada por longitud
print(lista_ordenada)
