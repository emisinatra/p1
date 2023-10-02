#17.Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo.
#Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia).
# Al finalizar el programa, mostrar el factorial del mayor número ingresado.
def suma_digitos(numero):
    # Convertir el número a string
    numero = str(numero)
    # Inicializar la suma en cero
    suma = 0
    # Recorrer cada caracter del número
    for caracter in numero:
        # Convertir el caracter a entero y sumarlo a la suma
        suma += int(caracter)
    # Devolver la suma
    return suma

# Inicializar el mayor número ingresado en cero
mayor = 0
# Crear un bucle para pedir números primos por teclado hasta que se ingrese uno que no lo sea
while True:
    # Pedir un número por teclado y convertirlo a entero
    numero = int(input("Ingrese un número primo (o uno que no lo sea para terminar): "))
    # Verificar si el número es primo o no usando la función definida anteriormente
    if es_primo(numero):
        # Si es primo, mostrar la suma de sus dígitos usando la función definida
        print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")
        # Pedir un dígito por teclado y mostrar la frecuencia del dígito en el número usando la función definida anteriormente
        digito = int(input("Ingrese un dígito: "))
        print(f"La frecuencia del dígito {digito} en el número {numero} es: {frecuencia(numero, digito)}")
        # Comparar el número con el mayor actual y actualizarlo si es necesario
        if numero > mayor:
            mayor = numero
    else:
        # Si no es primo, salir del bucle
        break
# Mostrar el factorial del mayor número ingresado usando la función definida anteriormente
print(f"El factorial del mayor número ingresado es: {factorial(mayor)}")