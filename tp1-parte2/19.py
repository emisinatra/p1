#19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes).
# Finalmente, mostrar la fecha en formato dd/mm/aaaa.
dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))
ano = int(input("Ingrese el año de su nacimiento: "))
print(dia, "/", mes, "/", ano) # Usando una coma
print(str(dia) + "/" + str(mes) + "/" + str(ano)) # Usando el operador +

