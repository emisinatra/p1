# Definir una función que verifica si un número es potencia de otro
def es_potencia(n, b):
  # Si el número es igual a uno, devolver True
  if n == 1:
    return True
  # Si el número es menor que uno o no es divisible por la base, devolver False
  if n < 1 or n % b != 0:
    return False
  # Si no, dividir el número por la base y repetir el proceso recursivamente
  return es_potencia(n // b, b)

# Probar la función con algunos ejemplos
print(es_potencia(8, 2)) 
print(es_potencia(9, 3))
print(es_potencia(10, 2))
print(es_potencia(25, 5))
