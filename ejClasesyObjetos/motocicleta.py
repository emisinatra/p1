class motocicleta:

    isNew = True
    motor = False

    def __init__(self, color, motoId, fuel_liter, number_wheels, brand, model, fabrication_date, top_speed, weight):
        self.color = color
        self.matricula = motoId
        self.combustible_litros = fuel_liter
        self.numero_ruedas = number_wheels
        self.marca = brand
        self.modelo = model
        self.fecha_fabricacion = fabrication_date
        self.velocidad_punta = top_speed
        self.peso = weight

    def arrancar(self):
        if self.motor == False:
            self.motor = True
            print(f"El motor de la motocicleta {self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"El motor de la motocicleta {self.marca} {self.modelo} ya estaba en marcha.")

    def detener(self):
        if self.motor == True:
            self.motor = False
            print(f"El motor de la motocicleta {self.marca} {self.modelo} se ha detenido.")
        else:
            print(f"El motor de la motocicleta {self.marca} {self.modelo} ya estaba detenido.")

    def consultar_precio(self):
        if hasattr(self, "precio"):
            print(f"El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio} $.")
        else:
            print(f"La motocicleta {self.marca} {self.modelo} no tiene precio asignado.")
