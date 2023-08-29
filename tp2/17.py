#17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes,
#otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo.
#Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
dia = input("Ingrese un día de la semana: ")
if dia.lower() == "lunes":
    print("Hoy es lunes, comienza una nueva semana")
elif dia.lower() == "viernes":
    print("Hoy es viernes, se acerca el fin de semana")
elif dia.lower() == "sábado" or dia.lower() == "domingo":
    print("Hoy es fin de semana, a disfrutar")
else:
    print("No reconozco ese día")
