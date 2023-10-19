# Definir una función que calcula la sumatoria K(n,p) usando la recursión
def K(n,p):
    # Si n es cero o menor que cero, devolver cero
    if n <=0:
        return 0
    # Si no, devolver el producto de n y p más el resultado de K(n-1,p)
    return n*p + K(n-1,p)

# Pedir al usuario que ingrese un número n y un número p
n = int(input("Ingrese un número n: "))
p = int(input("Ingrese un número p: "))
# Calcular el valor de K(n,p) usando la función recursiva
resultado = K(n,p)
# Imprimir el resultado de K(n,p)
print("El resultado de K(",n,",",p,") es:",resultado)
