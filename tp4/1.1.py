lineas = []

linea = input("Ingrese una línea: ")

while linea != "":
  lineas.append(linea)
  linea = input("Ingrese otra línea: ")

for linea in lineas:
  print(linea.upper())
