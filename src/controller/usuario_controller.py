import sys
sys.path.append('src')

import psycopg2

from model.usuario import Usuario

class UsuarioController:
    """Crea un objeto cursor para poder ejecutar"""
    def obtener_cursor():
        conenetion = psycopg2.connect( database="calculadora_renta", user="calculadora_renta_user", password="NFBuYD2NTHvXVOnZv2hpdSUtu9BkRSM4", host="dpg-d7sk47mgkk3c73dapt6g-a.oregon-postgres.render.com")
        cursor = conenetion.cursor()
        return cursor

    def insertar_usuario(usuario: Usuario):
        # Conectar a la base de datos
        cursor = UsuarioController.obtener_cursor()
        # Armar la consulta SQL para insertar un nuevo usuario
        sql = f"""INSERT INTO public.usuarios (cedula, nombre, apellido, telefono, correo, direccion)
        VALUES ('{usuario.cedula}', '{usuario.nombre}', '{usuario.apellido}', '{usuario.telefono}', '{usuario.correo}', '{usuario.direccion}');"""
        
        # Ejecutar la consulta SQL para insertar el usuario
        cursor.cursor.execute(sql)
        
        # Guardar los cambios en la base de datos
        cursor.connection.commit()

    def buscar_usuario(cedula):
        # Conectar a la base de datos
        cursor = UsuarioController.obtener_cursor()

        
        
        # Armar la consulta SQL para buscar un usuario por su cédula
        sql = f"""SELECT cedula, nombre, apellido, telefono, correo, direccion FROM public.usuarios WHERE cedula = '{cedula}';"""
        
        # Ejecutar la consulta SQL para buscar el usuario
        cursor.execute(sql)
        
        # Obtener el resultado de la consulta
        result = cursor.fetchone()
        
        if result:
            return Usuario(*result)
        else:
            return None