# Definir una función que implementa el ordenamiento mixto
def mixed_sort(lista):
  # Crear dos listas vacías para separar los números y las cadenas
  numeros = []
  cadenas = []
  # Recorrer la lista y clasificar los elementos según su tipo
  for x in lista:
    if isinstance(x, int) or isinstance(x, float):
      numeros.append(x)
    elif isinstance(x, str):
      cadenas.append(x)
    else:
      print("Tipo no válido:", x)
      return None
  # Ordenar las listas de números y cadenas utilizando el método sorted()
  numeros.sort()
  cadenas.sort()
  # Concatenar las listas ordenadas y devolver el resultado
  return numeros + cadenas

# Definir una lista que contenga tanto números como cadenas como entrada
lista = [5, "hola", "mundo", "python", "bing", "ordenamiento", "3.14", "2.71", "42"]
# Llamar a la función de ordenamiento mixto con la lista como argumento
lista_ordenada = mixed_sort(lista)
# Imprimir la lista ordenada mixta
print(lista_ordenada)
