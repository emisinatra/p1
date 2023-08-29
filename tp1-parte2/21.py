#21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto,
# para saber cuántos tanques de combustible consumirá el viaje entero.
# Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible,
# qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
km_por_litro = float(input("Ingrese cuántos kilómetros puede recorrer su moto con 1 litro de combustible: "))
capacidad_tanque = float(input("Ingrese qué capacidad (en litros) tiene el tanque: "))
km_totales = float(input("Ingrese cuántos kilómetros en total recorrerán: "))
tanques = km_totales / (km_por_litro * capacidad_tanque)
print("La cantidad de tanques de combustible necesarios es", tanques)
