# Crear el diccionario
divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

# Preguntar al usuario
divisa = input("Introduce una divisa: ")

# Mostrar el símbolo o un mensaje de aviso
print(divisas.get(divisa, "La divisa no está en el diccionario"))
