import sys
sys.path.append("src")

from datetime import date
from model.usuario import Usuario
from controller.usuario_controller import UsuarioController

try:
    cedula = input("Ingrese la cedula del usuario que desea buscar: ")
    
    usuario_buscado = UsuarioController.buscar_usuario(cedula)
    
    if usuario_buscado:
        print(f"Usuario encontrado: Nombre : {usuario_buscado.nombre} {usuario_buscado.apellido}, con correo : {usuario_buscado.correo}")
    else:
        print("No se encontro ningun usuario con esa cedula en la tabla.")
        
except Exception as err:
    print("Error : ")
    print(str(err))