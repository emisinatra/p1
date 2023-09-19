def es_primo(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

cantidad = 0

numero = int(input("Ingrese un número mayor que 1: "))

while numero != 0:
  if es_primo(numero):
    cantidad += 1
  numero = int(input("Ingrese otro número mayor que 1: "))

print("La cantidad de números primos ingresados es:", cantidad)
