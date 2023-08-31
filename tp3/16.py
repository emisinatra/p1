#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
cantidad = int(input("¿Cuántos números va a introducir? "))
negativos = 0
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero < 0:
        negativos += 1
print(f"Ha introducido {negativos} números negativos")
