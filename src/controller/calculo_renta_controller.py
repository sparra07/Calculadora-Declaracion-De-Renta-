import sys
sys.path.append(".")
sys.path.append('src')

import psycopg2
from model.calculo_renta import CalculoRenta
import secret_config

class CalculoRentaController:

    @staticmethod
    def obtener_cursor():
        connection = psycopg2.connect(
            database=secret_config.PGDATABASE, 
            user=secret_config.PGUSER, 
            password=secret_config.PGPASSWORD, 
            host=secret_config.PGHOST
        )
        cursor = connection.cursor()
        return cursor

    @staticmethod
    def crear_tabla():
        cursor = CalculoRentaController.obtener_cursor()
        with open('sql/crear_calculos.sql', 'r') as file:
            sql = file.read()
        cursor.execute(sql)
        cursor.connection.commit()

    @staticmethod
    def borrar_tabla(): 
        cursor = CalculoRentaController.obtener_cursor()
        with open('sql/borrar_tablas.sql', 'r') as file:
            sql = file.read()
        cursor.execute(sql)
        cursor.connection.commit()

    @staticmethod
    def insertar_calculo(calculo: CalculoRenta):
        cursor = CalculoRentaController.obtener_cursor()
        sql = f"""INSERT INTO calculos_renta (cedula_usuario, ingreso_bruto, aportes_ley, deducciones, fecha_creacion)
        VALUES ('{calculo.cedula_usuario}', {calculo.ingreso_bruto}, {calculo.aportes_ley}, {calculo.deducciones}, '{calculo.fecha_creacion}') RETURNING id_calculo;"""
        cursor.execute(sql)
        id_generado = cursor.fetchone()[0]
        calculo.id_calculo = id_generado
        cursor.connection.commit()
        return id_generado

    @staticmethod
    def buscar_calculos_por_usuario(cedula_usuario):
        cursor = CalculoRentaController.obtener_cursor()
        sql = f"""SELECT id_calculo, cedula_usuario, ingreso_bruto, aportes_ley, deducciones, fecha_creacion 
                  FROM calculos_renta WHERE cedula_usuario = '{cedula_usuario}' ORDER BY id_calculo DESC;"""
        cursor.execute(sql)
        filas = cursor.fetchall()
        
        lista_resultados = []
        for fila in filas:
            # Reconstrucción adaptada a los 6 parámetros básicos
            objeto_calculo = CalculoRenta(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            objeto_calculo.income_bruto = fila[2]  
            objeto_calculo.renta_liquida = fila[2] - fila[3] - fila[4]
            lista_resultados.append(objeto_calculo)
            
        return lista_resultados

    # === MÉTODO NUEVO REQUERIDO POR test_calculo_renta.py ===
    @staticmethod
    def buscar_calculo(id_calculo):
        cursor = CalculoRentaController.obtener_cursor()
        sql = f"""SELECT id_calculo, cedula_usuario, ingreso_bruto, aportes_ley, deducciones, fecha_creacion 
                  FROM calculos_renta WHERE id_calculo = {id_calculo};"""
        cursor.execute(sql)
        fila = cursor.fetchone()
        if fila:
            objeto_calculo = CalculoRenta(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            objeto_calculo.income_bruto = fila[2]
            objeto_calculo.renta_liquida = fila[2] - fila[3] - fila[4]
            return objeto_calculo
        return None

    # === MÉTODO NUEVO REQUERIDO POR vista_calculadora.py (Línea 161) ===
    @staticmethod
    def buscar_calculo_por_id(id_calculo):
        return CalculoRentaController.buscar_calculo(id_calculo)

    # === MÉTODO NUEVO REQUERIDO POR vista_calculadora.py (Línea 184) ===
    @staticmethod
    def actualizar_calculo(calculo: CalculoRenta):
        cursor = CalculoRentaController.obtener_cursor()
        sql = f"""UPDATE calculos_renta 
                  SET ingreso_bruto={calculo.ingreso_bruto}, aportes_ley={calculo.aportes_ley}, 
                      deducciones={calculo.deducciones}, fecha_creacion='{calculo.fecha_creacion}' 
                  WHERE cedula_usuario='{calculo.cedula_usuario}';"""
        cursor.execute(sql)
        cursor.connection.commit()

    # === MÉTODO NUEVO REQUERIDO POR vista_calculadora.py (Línea 195) ===
    @staticmethod
    def eliminar_calculo_por_id(cedula_usuario):
        CalculoRentaController.eliminar_calculo_por_cedula(cedula_usuario)

    @staticmethod
    def eliminar_calculo_por_cedula(cedula_usuario):
        cursor = CalculoRentaController.obtener_cursor()
        sql = f"DELETE FROM calculos_renta WHERE cedula_usuario = '{cedula_usuario}';"
        cursor.execute(sql)
        cursor.connection.commit()