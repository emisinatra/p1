class Cuenta:
    def __init__(self, titular=Persona(), cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    # Getters y Setters con validaciones
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        if isinstance(titular, Persona):
            self._titular = titular
        else:
            raise ValueError("El titular debe ser una instancia de la clase Persona.")

    @property
    def cantidad(self):
        return self._cantidad

