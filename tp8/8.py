# Definir una función que calcula el valor del triángulo de Pascal en la fila n y la columna k usando la recursión
def pascal(n,k):
    # Si k es cero o igual a n, devolver uno (caso base)
    if k ==0 or k ==n:
        return 1
    # Si no, devolver la suma de los valores del triángulo en las posiciones (n-1,k-1) y (n-1,k) (caso recursivo)
    return pascal(n-1,k-1) + pascal(n-1,k)

# Probar la función con algunos ejemplos
print(pascal(0,0)) 
print(pascal(4,2))
print(pascal(5,3))
