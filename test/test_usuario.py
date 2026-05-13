import unittest
import sys
sys.path.append('src')

from model.usuario import Usuario
from controller.usuario_controller import UsuarioController



class TestUsuario(unittest.TestCase):

    def test_usuario_creacion(self):
        usuario_prueba = Usuario(
            cedula='135827326483',
            nombre='Estela',
            apellido='Flores',
            telefono='525-1234',
            correo='Estela.flores@example.com',
            direccion='Calle Principal 123')
        
        UsuarioController.insertar_usuario(usuario_prueba)

        usuario_encontrado = UsuarioController.buscar_usuario('135827326483')
        

        self.assertEqual(usuario_prueba, usuario_encontrado)