#13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
# Ejemplo, si se introduce 23 que muestre 32.
numero = int(input("Ingrese un número de dos cifras: "))
inverso = (numero % 10) * 10 + (numero // 10)
print("El número invertido es", inverso)
