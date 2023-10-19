# Definir una función que calcula las medidas de la hoja A(N) usando la recursión
def medidas_hoja_A(N):
  # Si N es cero, devolver las medidas de la hoja A0 como caso base
  if N == 0:
    return (841, 1189)
  # Si no, obtener las medidas de la hoja A(N-1) llamando a la función recursivamente
  ancho, largo = medidas_hoja_A(N - 1)
  # Si el ancho es mayor que el largo, dividir el ancho por dos y devolver el nuevo ancho y el largo como resultado
  if ancho > largo:
    return (ancho // 2, largo)
  # Si no, dividir el largo por dos y devolver el ancho y el nuevo largo como resultado
  else:
    return (ancho, largo // 2)

# Probar la función con algunos ejemplos
print(medidas_hoja_A(1))
print(medidas_hoja_A(2))
print(medidas_hoja_A(3))
print(medidas_hoja_A(4))
