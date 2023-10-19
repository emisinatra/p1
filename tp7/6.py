# Definir una función que implementa el ordenamiento por conteo
def counting_sort(lista):
  # Obtener el valor máximo y mínimo de la lista
  maximo = max(lista)
  minimo = min(lista)
  # Calcular el rango
  rango = maximo - minimo + 1
  # Crear una lista de conteo inicializada con ceros
  conteo = [0] * rango
  # Crear una lista de salida del mismo tamaño que la lista de entrada
  salida = [0] * len(lista)
  # Recorrer la lista de entrada y contar la frecuencia de cada elemento
  for x in lista:
    conteo[x - minimo] += 1
  # Acumular los valores de la lista de conteo para obtener las posiciones de los elementos en la lista de salida
  for i in range(1, rango):
    conteo[i] += conteo[i - 1]
  # Recorrer la lista de entrada en orden inverso y colocar los elementos en la lista de salida según sus posiciones calculadas
  for i in range(len(lista) - 1, -1, -1):
    salida[conteo[lista[i] - minimo] - 1] = lista[i]
    conteo[lista[i] - minimo] -= 1
  # Devolver la lista ordenada por conteo
  return salida

# Definir una lista de números enteros como entrada
lista = [5, 3, 8, 2, 9, 4, 7, 6, 1]
# Llamar a la función de ordenamiento por conteo con la lista como argumento
lista_ordenada = counting_sort(lista)
# Imprimir la lista ordenada por conteo
print(lista_ordenada)
