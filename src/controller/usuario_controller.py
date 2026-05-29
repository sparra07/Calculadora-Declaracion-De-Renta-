import sys
sys.path.append( ".")
sys.path.append('src')

import psycopg2
from model.usuario import Usuario
import secret_config

class UsuarioController:
    
    def crear_tabla():
        cursor= UsuarioController.obtener_cursor()
        # Leer el contenido del archivo SQL
        with open('sql/crear_usuarios.sql', 'r') as file:
            sql= file.read()
        cursor.execute(sql)
        cursor.connection.commit()

    def borrar_tabla(): 
        cursor= UsuarioController.obtener_cursor()
        # Leer el contenido del archivo SQL
        with open('sql/borrar_tablas.sql', 'r') as file:
            sql= file.read()
        cursor.execute(sql)
        cursor.connection.commit()

    
    """Crea un objeto cursor para poder ejecutar"""
    def obtener_cursor():
        connection = psycopg2.connect( database=secret_config.PGDATABASE, user=secret_config.PGUSER, password=secret_config.PGPASSWORD, host=secret_config.PGHOST)
        cursor = connection.cursor()
        return cursor

    def insertar_usuario(usuario: Usuario):
        # Conectar a la base de datos
        cursor = UsuarioController.obtener_cursor()
        # Armar la consulta SQL para insertar un nuevo usuario
        sql = f"""INSERT INTO usuarios (cedula, nombre, apellido, telefono, correo, direccion)
        VALUES ('{usuario.cedula}', '{usuario.nombre}', '{usuario.apellido}', '{usuario.telefono}', '{usuario.correo}', '{usuario.direccion}');"""
        
        # Ejecutar la consulta SQL para insertar el usuario
        cursor.execute(sql)
        
        # Guardar los cambios en la base de datos
        cursor.connection.commit()

    def buscar_usuario(cedula):
        # Conectar a la base de datos
        cursor = UsuarioController.obtener_cursor()

    
        # Armar la consulta SQL para buscar un usuario por su cédula
        sql = f"""SELECT cedula, nombre, apellido, telefono, correo, direccion FROM usuarios WHERE cedula = '{cedula}';"""
        
        # Ejecutar la consulta SQL para buscar el usuario
        cursor.execute(sql)
        
        # Obtener el resultado de la consulta
        fila = cursor.fetchone()
        if fila:
            resultado = Usuario(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            return resultado   
        return None

    def eliminar_usuario(cedula):
        cursor = UsuarioController.obtener_cursor()
        sql = f"DELETE FROM usuarios WHERE cedula = '{cedula}';"
        cursor.execute(sql)
        cursor.connection.commit()

    def actualizar_usuario(usuario: Usuario):
        cursor = UsuarioController.obtener_cursor()
        sql = f"""UPDATE usuarios 
                SET nombre='{usuario.nombre}', apellido='{usuario.apellido}', 
                    telefono='{usuario.telefono}', correo='{usuario.correo}', direccion='{usuario.direccion}' 
                WHERE cedula='{usuario.cedula}';"""
        cursor.execute(sql)
        cursor.connection.commit()
       
        
        