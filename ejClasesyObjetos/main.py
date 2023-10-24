from motocicleta import motocicleta

moto1 = motocicleta("rojo", "ABC-123", 10, 2, "Honda", "CBR 1000 RR", "2023-01-01", 299, 200)
moto2 = motocicleta("azul", "XYZ-789", 10, 2, "Yamaha", "YZF-R1", "2023-02-01", 298, 201)

moto1.arrancar()
moto1.arrancar()
moto1.detener()
moto1.detener()

moto2.arrancar()
moto2.detener()

moto1.precio = 15000

print(f"El precio de la motocicleta {moto1.marca} {moto1.modelo} es de {moto1.precio} $.")

moto1.consultar_precio()
moto2.consultar_precio()
