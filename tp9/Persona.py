class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Getters y Setters con validaciones
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto.")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un número entero positivo.")

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        if isinstance(dni, str):
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de texto.")

    # Método para mostrar los datos de la persona
    def mostrar(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}'

    # Método para verificar si la persona es mayor de edad
    def esMayorDeEdad(self):
        return self.edad >= 18
