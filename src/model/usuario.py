class Usuario:
    def __init__(self, cedula, nombre, apellido, telefono="", correo="", direccion=""):
        self.cedula = str(cedula)
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.telefono = str(telefono)
        self.correo = str(correo)
        self.direccion = str(direccion)

    def is_equal(self, otro):
        if not isinstance(otro, Usuario):
            return False
        return (self.cedula == otro.cedula and
                self.nombre == otro.nombre and
                self.apellido == otro.apellido and
                self.telefono == otro.telefono and
                self.correo == otro.correo and
                self.direccion == otro.direccion)