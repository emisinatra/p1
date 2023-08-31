#4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
numero = int(input("Ingrese un número entero positivo: "))
cuenta_atras = []
for i in range(numero, -1, -1):
    cuenta_atras.append(str(i))
print(", ".join(cuenta_atras))