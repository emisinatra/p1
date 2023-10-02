#16.Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número,
# utilizando para ello una función que calcule la frecuencia.
def frecuencia(numero, digito):
    # Convertir el número y el dígito a strings
    numero = str(numero)
    digito = str(digito)
    # Inicializar la frecuencia en cero
    frecuencia = 0
    # Recorrer cada caracter del número
    for caracter in numero:
        # Comparar el caracter con el dígito y si son iguales incrementar la frecuencia en uno
        if caracter == digito:
            frecuencia += 1
    # Devolver la frecuencia
    return frecuencia

# Pedir un número entero y un dígito por pantalla y mostrar la frecuencia del dígito en el número usando la función definida
numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese un dígito: "))
frecuencia = frecuencia(numero, digito)
print(f"La frecuencia del dígito {digito} en el número {numero} es: {frecuencia}")