import sys
sys.path.append("src")

from model.usuario import Usuario
from controller.usuario_controller import UsuarioController

# Insertar un Usuario en la tabla
usuario = Usuario(
    cedula="", 
    nombre="", 
    apellido="", 
    telefono="", 
    correo="", 
    direccion=""
)

print("Por favor ingrese los datos del usuario que desea crear")

usuario.cedula = input("Cedula : ")
usuario.nombre = input("Nombre : ")
usuario.apellido = input("Apellido : ")
usuario.telefono = input("Telefono : ")
usuario.correo = input("Correo : ")
usuario.direccion = input("Direccion : ")

# Se envía el objeto al método exacto de tu controlador
UsuarioController.insertar_usuario(usuario)

print("Usuario insertado correctamente!")