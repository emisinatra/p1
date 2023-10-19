# Definir una función que encuentra el mayor elemento de una lista usando la recursión
def maximo(lista):
  # Si la lista está vacía, devolver None
  if not lista:
    return None
  # Si la lista tiene un solo elemento, devolver ese elemento
  if len(lista) == 1:
    return lista[0]
  # Si no, comparar el primer elemento de la lista con el máximo del resto de la lista y devolver el mayor de los dos
  return max(lista[0], maximo(lista[1:]))

# Probar la función con algunos ejemplos
print(maximo([5, 3, 8, 2, 9, 4, 7, 6, 1])) 
print(maximo([1, 2, 3, 4, 5]))
print(maximo([]))