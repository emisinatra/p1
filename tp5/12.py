#12.Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
def palabras_longitud(frase):
    # Crear un diccionario vacío para guardar el resultado
    resultado = {}
    # Separar la frase por los espacios y obtener las palabras
    palabras = frase.split()
    # Recorrer cada palabra de la frase
    for palabra in palabras:
        # Calcular la longitud de la palabra
        longitud = len(palabra)
        # Agregar la palabra y su longitud al diccionario como una clave y un valor
        resultado[palabra] = longitud
    # Devolver el diccionario
    return resultado

# Pedir una frase por pantalla y mostrar el diccionario con las palabras y su longitud usando la función definida
frase = input("Ingrese una frase: ")
diccionario = palabras_longitud(frase)
print(diccionario)