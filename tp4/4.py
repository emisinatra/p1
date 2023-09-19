inicio = int(input("Ingrese el año inicial: "))
final = int(input("Ingrese el año final: "))

for año in range(inicio, final + 1):
  if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0) and (año % 10 == 0):
    print(año)
