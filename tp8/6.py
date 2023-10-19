# Definir una función que replica los elementos de una lista n veces
def replicar(lista, n):
  # Si la lista está vacía o n es cero, devolver la lista vacía
  if not lista or n == 0:
    return []
  # Si no, crear una lista con el primer elemento de la lista repetido n veces
  repetido = [lista[0]] * n
  # Concatenar la lista repetida con el resultado de replicar el resto de la lista n veces
  return repetido + replicar(lista[1:], n)

# Probar la función con algunos ejemplos
print(replicar([1, 3, 3, 7], 2))
print(replicar([5, 4], 3))
print(replicar([], 2))
print(replicar([1, 2], 0))
