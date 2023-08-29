#12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año
# o cuántos años faltan para llegar a ese año.
actual = int(input("Ingrese el año actual: "))
cualquiera = int(input("Ingrese un año cualquiera: "))
diferencia = abs(actual - cualquiera)
if actual > cualquiera:
    print("Han pasado", diferencia, "años desde el año", cualquiera)
else:
    print("Faltan", diferencia, "años para llegar al año", cualquiera)
