
# Definir una función que verifica si un número natural es par usando la recursión mutua
def par(n):
  # Si el número es cero, devolver True
  if n == 0:
    return True
  # Si no, restar uno al número y llamar a la función impar con el resultado
  return impar(n - 1)

# Definir una función que verifica si un número natural es impar usando la recursión mutua
def impar(n):
  # Si el número es uno, devolver True
  if n == 1:
    return True
  # Si no, restar uno al número y llamar a la función par con el resultado
  return par(n - 1)

# Probar las funciones con algunos ejemplos
print(par(2)) 
print(par(3))
print(impar(1))
print(impar(4))
