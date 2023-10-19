# Definir una función que busca las ocurrencias de una cadena dentro de otra
def buscar_ocurrencias(a, b):
  # Crear una lista vacía para guardar las posiciones
  posiciones = []
  # Definir una función auxiliar que realiza la búsqueda recursiva
  def buscar_recursivo(a, b, i):
    # Si el índice i es mayor o igual que la longitud de a, terminar la búsqueda
    if i >= len(a):
      return
    # Si la subcadena de a desde i hasta i + la longitud de b es igual a b, agregar i a la lista de posiciones
    if a[i:i + len(b)] == b:
      posiciones.append(i)
    # Llamar a la función auxiliar con el índice i incrementado en uno
    buscar_recursivo(a, b, i + 1)
  # Llamar a la función auxiliar con el índice inicial en cero
  buscar_recursivo(a, b, 0)
  # Devolver la lista de posiciones como resultado
  return posiciones

# Probar la función con algunos ejemplos
print(buscar_ocurrencias("abracadabra", "a")) 
print(buscar_ocurrencias("anita lava la tina", "a"))
print(buscar_ocurrencias("hola mundo", "o"))
print(buscar_ocurrencias("hola mundo", "z"))
