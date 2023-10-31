class Agenda:
    def __init__(self):
        self.contactos = []

    # Método para añadir un contacto
    def añadir_contacto(self, nombre, telefono, email):
        contacto = {'nombre': nombre, 'telefono': telefono, 'email': email}
        self.contactos.append(contacto)

    # Método para listar los contactos
    def lista_contactos(self):
        for contacto in self.contactos:
            print(contacto)

    # Método para buscar un contacto por nombre
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                return contacto

    # Método para editar un contacto
    def editar_contacto(self, nombre, telefono=None, email=None):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                if telefono is not None:
                    contacto['telefono'] = telefono
                if email is not None:
                    contacto['email'] = email

    # Método para cerrar la agenda (no hace nada en este caso)
    def cerrar_agenda(self):
        pass

