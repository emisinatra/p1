#12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
n = float(input("Ingrese un número: "))
import math
raiz_cuadrada = math.sqrt(n)
raiz_cubica = math.pow(n, 1/3)
print("La raíz cuadrada de", n, "es", raiz_cuadrada)
print("La raíz cúbica de", n, "es", raiz_cubica)
