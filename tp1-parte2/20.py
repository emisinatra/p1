#20.	Hacer otra versión del programa, pero esta vez almacenado
# todo en una única variable con formato DDMMAAA.
fecha = int(input("Ingrese su fecha de nacimiento en formato DDMMAAA: "))

dia = fecha // 1000000
mes = (fecha % 1000000) // 10000
año = fecha % 10000
aprint(dia, "/", mes, "/", año) # Usando una coma
print(str(dia) + "/" + str(mes) + "/" + str(año)) # Usando el operador +
