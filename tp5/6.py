#6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra.
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.
def espacio_adicional(texto):
    # Crear una cadena vacía para guardar el resultado
    resultado = ""
    # Recorrer cada letra del texto
    for letra in texto:
        # Agregar la letra y un espacio al resultado
        resultado += letra + " "
    # Devolver el resultado
    return resultado

# Pedir un texto por pantalla y mostrar el resultado de aplicar la función espacio_adicional
texto = input("Ingrese un texto: ")
resultado = espacio_adicional(texto)
print(f"El resultado es: {resultado}")