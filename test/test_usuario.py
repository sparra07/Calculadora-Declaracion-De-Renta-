import unittest
import sys
sys.path.append('src')

from model.usuario import Usuario
from controller.usuario_controller import UsuarioController



class TestUsuario(unittest.TestCase):

    # Text fixture
    @classmethod
    def setUpClass(cls):   
        UsuarioController.borrar_tabla()
        UsuarioController.crear_tabla()
        

    def test_1_usuario_creacion_normal(self):
        usuario_prueba = Usuario(
            cedula='135827326483',
            nombre='Carolina',
            apellido='Flores',
            telefono='525-1234',
            correo='Carolina.flores@example.com',
            direccion='Calle Principal 123')
        
        UsuarioController.insertar_usuario(usuario_prueba)

        usuario_encontrado = UsuarioController.buscar_usuario(usuario_prueba.cedula)      
        self.assertTrue(usuario_encontrado.is_equal(usuario_prueba))
    
    def test_2_usuario_campos_vacios_opcionales(self):
            usuario_prueba = Usuario(
                cedula='456123789',
                nombre='Carlos',
                apellido='Gomez',
                telefono='', # Vacio
                correo='',   # Vacio
                direccion='Zona Industrial Bodega 5'
            )
            UsuarioController.insertar_usuario(usuario_prueba)
            usuario_encontrado = UsuarioController.buscar_usuario(usuario_prueba.cedula)      
            
            self.assertIsNotNone(usuario_encontrado)
            self.assertTrue(usuario_encontrado.is_equal(usuario_prueba))
    
    def test_3_usuario_cedula_duplicada(self):
        usuario_original = Usuario(
            cedula='741852963',
            nombre='Andres',
            apellido='Mendoza',
            telefono='3159876543',
            correo='andres.mendoza@example.com',
            direccion='Diagonal 45 # 10-20'
        )
        UsuarioController.insertar_usuario(usuario_original)

        usuario_duplicado = Usuario(
            cedula='741852963', # Misma cedula para forzar el error de llave primaria
            nombre='Camila',
            apellido='Restrepo',
            telefono='3104561234',
            correo='camila.restrepo@example.com',
            direccion='Avenida El Poblado 50'
        )
        
        self.assertRaises(Exception, UsuarioController.insertar_usuario, usuario_duplicado)

    def test_4_usuario_cedula_corta(self):
        usuario_prueba = Usuario(
            cedula='1',
            nombre='Mateo',
            apellido='Zapata',
            telefono='3004445555',
            correo='mateo.zapata@example.com',
            direccion='Carrera 70 # 32B-15'
        )
        UsuarioController.insertar_usuario(usuario_prueba)
        usuario_encontrado = UsuarioController.buscar_usuario(usuario_prueba.cedula)      
        
        self.assertIsNotNone(usuario_encontrado)
        self.assertTrue(usuario_encontrado.is_equal(usuario_prueba))

    def test_5_usuario_cedula_con_ceros_iniciales(self):
        usuario_prueba = Usuario(
            cedula='000123456789', # Al ser un campo de texto, los ceros a la izquierda deben mantenerse intactos
            nombre='Sebastian',
            apellido='Mejia',
            telefono='3119876543',
            correo='sebastian.mejia@example.com',
            direccion='Circular 4 # 73-10'
        )
        UsuarioController.insertar_usuario(usuario_prueba)
        usuario_encontrado = UsuarioController.buscar_usuario(usuario_prueba.cedula)      
        
        self.assertIsNotNone(usuario_encontrado)
        self.assertTrue(usuario_encontrado.is_equal(usuario_prueba))

if __name__ == '__main__':
    unittest.main() 