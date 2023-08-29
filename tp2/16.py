#16-	Haz una calculadora básica pida al usuario dos valores, a y b.
#Según la opción que desean, realizar la operación:
#•	Si operación es 1 entonces debemos ver el resultado de a + b
#•	Si operación es 2 entonces debemos ver el resultado de a * b
#•	Si operación es 3 entonces debemos ver el resultado de a - b
#•	Si operación es 4 entonces debemos ver el resultado de a / b
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
print("Las opciones son:")
print("1) Suma")
print("2) Multiplicación")
print("3) Resta")
print("4) División")
opcion = int(input("Ingrese la opción elegida (1, 2, 3 o 4): "))
if opcion == 1:
    resultado = a + b
elif opcion == 2:
    resultado = a * b
elif opcion == 3:
    resultado = a - b
elif opcion == 4:
    resultado = a / b
else:
    print("Opción inválida")
    resultado = None
if resultado != None:
    print("El resultado es", resultado)
