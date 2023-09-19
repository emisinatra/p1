saldo = 0

bitacora = []

operacion = input("Ingrese una operación: ")

while operacion != "":
  bitacora.append(operacion)
  tipo, monto = operacion.split()
  monto = float(monto)
  if tipo == "D":
    saldo += monto
  elif tipo == "R":
    saldo -= monto
  operacion = input("Ingrese otra operación: ")

print("El saldo final de la cuenta es:", saldo)

print("La bitácora de operaciones es:")
for operacion in bitacora:
  print(operacion)
