# Definir una función que imprime las combinaciones de longitud k de una lista de caracteres
def combinaciones(lista,k):
    # Si k es cero, imprimir la cadena vacía (caso base)
    if k == 0:
        print("")
        return
    # Si no, recorrer la lista de caracteres
    for x in lista:
        # Para cada caracter, concatenarlo con las combinaciones de longitud k-1 de la lista (caso recursivo)
        for y in combinaciones(lista,k-1):
            print(x+y)

# Probar la función con algunos ejemplos
combinaciones(["a","b","c"],2) 
combinaciones(["x","y"],3)
