fecha = input("Ingrese la fecha actual en formato día, DD/MM: ")

dia_semana, dia_mes = fecha.split(", ")
dia, mes = map(int, dia_mes.split("/"))

dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes"]

if dia_semana.lower() not in dias_validos:
    print("Error: día de la semana inexistente")
    exit()

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Error: fecha inválida")
    exit()

nivel = ""
if dia_semana.lower() == "lunes":
    nivel = "inicial"
elif dia_semana.lower() == "martes":
    nivel = "intermedio"
elif dia_semana.lower() == "miércoles":
    nivel = "avanzado"
elif dia_semana.lower() == "jueves":
    nivel = "práctica hablada"
elif dia_semana.lower() == "viernes":
    nivel = "inglés para viajeros"

if nivel in ["inicial", "intermedio", "avanzado"]:
    examenes = input("¿Se tomaron los exámenes? (S/N): ")
    if examenes.upper() == "S":
        aprobados = int(input("Ingrese el número de alumnos aprobados: "))
        desaprobados = int(input("Ingrese el número de alumnos desaprobados: "))
        porcentaje = aprobados / (aprobados + desaprobados) * 100
        print(f"El porcentaje de aprobados es {porcentaje:.2f}%")

if nivel == "práctica hablada":
    asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
    if asistencia > 50:
        print("Asistió la mayoría")
    else:
        print("No asistió la mayoría")

if nivel == "inglés para viajeros" and dia == 1 and mes in [1, 7]:
    print("Comienzo de nuevo ciclo")
    cantidad = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
    arancel = float(input("Ingrese el arancel en $ por cada alumno: "))
    ingreso = cantidad * arancel
    print(f"El ingreso total en $ es {ingreso:.2f}")
