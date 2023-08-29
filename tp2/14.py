#14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
#Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es
#x = -b / a
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
if a == 0 and b == 0:
    print("Todos los números son solución")
elif a == 0 and b != 0:
    print("No hay solución")
else:
    x = -b / a
    print("La solución es", x)

