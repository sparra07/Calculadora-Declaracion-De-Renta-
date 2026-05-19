import sys
sys.path.append(".")
sys.path.append('src')

import psycopg2
from model.calculo_renta import CalculoRenta
import secret_config

class CalculoRentaController:
    
    def crear_tabla():
        cursor = CalculoRentaController.obtener_cursor()
        with open('sql/crear_calculos.sql', 'r') as file:
            sql = file.read()
        cursor.execute(sql)
        cursor.connection.commit()

    def borrar_tabla(): 
        cursor = CalculoRentaController.obtener_cursor()
        with open('sql/borrar_tablas.sql', 'r') as file:
            sql = file.read()
        cursor.execute(sql)
        cursor.connection.commit()

    def obtener_cursor():
        connection = psycopg2.connect(
            database=secret_config.PGDATABASE, 
            user=secret_config.PGUSER, 
            password=secret_config.PGPASSWORD, 
            host=secret_config.PGHOST
        )
        cursor = connection.cursor()
        return cursor

    def insertar_calculo(calculo: CalculoRenta):
        cursor = CalculoRentaController.obtener_cursor()
        
        sql = f"""INSERT INTO calculos_renta (cedula_usuario, ingreso_bruto, aportes_ley, deducciones, renta_liquida, fecha_creacion)
        VALUES ('{calculo.cedula_usuario}', {calculo.ingreso_bruto}, {calculo.aportes_ley}, {calculo.deducciones}, {calculo.renta_liquida}, '{calculo.fecha_creacion}') RETURNING id_calculo;"""
        
        cursor.execute(sql)
        # Capturamos el id autogenerado por el SERIAL
        calculo.id_calculo = cursor.fetchone()[0]
        cursor.connection.commit()

    def buscar_calculo(id_calculo):
        cursor = CalculoRentaController.obtener_cursor()
        
        sql = f"""SELECT id_calculo, cedula_usuario, ingreso_bruto, aportes_ley, deducciones, renta_liquida, fecha_creacion 
        FROM calculos_renta WHERE id_calculo = {id_calculo};"""
        
        cursor.execute(sql)
        fila = cursor.fetchone()
        
        if fila:
            resultado = CalculoRenta(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
            return resultado   
        return None