#2.Dados los catetos de un triángulo rectángulo, calcular su hipotenusa
a = float(input("Ingrese el cateto a: "))
b = float(input("Ingrese el cateto b: "))
import math
c = math.sqrt(a**2 + b**2)
print("La hipotenusa del triángulo rectángulo es", c)