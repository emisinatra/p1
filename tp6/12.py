# Preguntar al usuario
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu teléfono: ")

# Guardar en un diccionario
usuario = {'nombre': nombre, 'edad': edad, 'dirección': direccion, 'teléfono': telefono}

# Mostrar la información
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['dirección']} y su número de teléfono es {usuario['teléfono']}")
