class Usuario:
    def __init__(self, cedula, nombre, apellido, telefono, correo, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def __str__(self):
        return f"Usuario(cedula={self.cedula}, nombre={self.nombre}, apellido={self.apellido}, telefono={self.telefono}, correo={self.correo}, direccion={self.direccion})"