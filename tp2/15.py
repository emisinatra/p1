#15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo.
# Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t),
# el programa tiene que pedir entonces la base y la altura y escribir el área.
# Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c),
# el programa tiene que pedir entonces el radio y escribir el área.
# Preguntar primero si se quiere calcular el área de un triángulo o la de un círculo, mostrando las opciones disponibles
print("Las opciones son:")
print("T) Área de un triángulo")
print("C) Área de un círculo")
opcion = input("Ingrese la opción elegida (T o C): ")
if opcion == "T" or opcion == "t":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print("El área del triángulo es", area)
else:
    radio = float(input("Ingrese el radio del círculo: "))
    import math
    area = math.pi * radio**2
    print("El área del círculo es", area)
