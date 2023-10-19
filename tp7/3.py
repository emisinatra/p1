# Definir una función que implementa el ordenamiento por clave
def key_sort(lista, clave):
  # Obtener la longitud de la lista
  n = len(lista)
  # Recorrer la lista desde el inicio hasta el final - 1
  for i in range(n - 1):
    # Asignar el índice del elemento más pequeño al primer elemento del subarreglo no ordenado
    min_index = i
    # Recorrer el subarreglo no ordenado desde el segundo elemento hasta el final
    for j in range(i + 1, n):
      # Comparar el valor del campo clave del elemento actual con el del más pequeño
      if lista[j][clave] < lista[min_index][clave]:
        # Actualizar el índice del elemento más pequeño si el valor del campo clave del actual es menor que el del más pequeño
        min_index = j
    # Intercambiar el primer elemento del subarreglo no ordenado con el más pequeño
    lista[i], lista[min_index] = lista[min_index], lista[i]
  # Devolver la lista ordenada por clave
  return lista

# Definir una lista de diccionarios que contienen información sobre libros
lista = [
         {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "año": 1943},
         {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
         {"titulo": "El código Da Vinci", "autor": "Dan Brown", "año": 2003},
         {"titulo": "El alquimista", "autor": "Paulo Coelho", "año": 1988},
         {"titulo": "Harry Potter y la piedra filosofal", "autor": "J. K. Rowling", "año": 1997}
        ]
# Llamar a la función de ordenamiento por clave con la lista y el campo año como argumentos
lista_ordenada_por_año = key_sort(lista, "año")
# Imprimir la lista ordenada por año
print(lista_ordenada_por_año)
# Llamar a la función de ordenamiento por clave con la lista y el campo autor como argumentos
lista_ordenada_por_autor = key_sort(lista, "autor")
# Imprimir la lista ordenada por autor
print(lista_ordenada_por_autor)
