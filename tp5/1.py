#1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es.
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
def validar_dni(dni):
  # Convertir el dni a un string
  dni = str(dni)
  # Verificar que tenga entre 7 y 8 dígitos
  if len(dni) < 7 or len(dni) > 8:
    return False
  # Verificar que todos los caracteres sean dígitos
  for c in dni:
    if not c.isdigit():
      return False
  # Si se cumplen las condiciones, el dni es válido
  return True


# Pedir un número de DNI por pantalla y validar si es correcto
dni = input("Ingrese un número de DNI: ")
if validar_dni(dni):
  print("El número de DNI es válido.")
else:
  print("El número de DNI es inválido.")
