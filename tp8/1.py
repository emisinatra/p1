# Definir una función que cuenta los dígitos de un número positivo
def contar_digitos(n):
  # Inicializar un contador en cero
  contador = 0
  # Mientras el número sea mayor que cero
  while n > 0:
    # Incrementar el contador en uno
    contador += 1
    # Dividir el número entre 10 y descartar el resto
    n //= 10
  # Devolver el contador como resultado
  return contador

# Probar la función con algunos ejemplos
print(contar_digitos(123)) 
print(contar_digitos(4567))
print(contar_digitos(0))
