"""
Script principal para la interfaz de consola del sistema de declaración de renta.
Este módulo gestiona la captura de datos financieros del usuario y presenta 
el desglose de impuestos calculado por la lógica de negocio.
"""
import sys
sys.path.append("src")
from model.Logica_calculadora import CalculadoraImpuestos, Impuestos
"""Script principal para la interacción con el usuario y el cálculo de declaración de renta."""

try:
    """Ejecuta la interfaz de consola para capturar datos y mostrar los resultados del cálculo tributario."""
    print("Este programa permite calcular la declaracion de renta")

    # Captura de datos de entrada desde la consola
    ingreso_bruto= float(input("Ingrese sus ingresos: "))
    aportes_ley= float(input("Ingrese sus aportes: "))
    deducciones= float(input("Ingrese sus deducciones: "))

# Inicialización del objeto con los datos proporcionados por el usuario
    datos_usuario = Impuestos(ingreso_bruto, aportes_ley, deducciones)

    # Procesamiento: Se obtiene una tupla con los 4 valores resultantes del cálculo
    # Índice 0: Renta Líquida, 1: Beneficio Real, 2: Límite Legal, 3: Impuesto Total
    resultado = CalculadoraImpuestos.calcular_entradas(datos_usuario)
    
    # Desglose de resultados para el usuario
    print(f"la renta liquida tiene un valor de: {resultado[0]}")
    print(f"El beneficio real tiene un valor de: {resultado[1]}")
    print(f"El limite legal tiene un valor de: {resultado[2]}")
    print(f"El volor total de impuestos a pagar es: {resultado[3]}")         

except Exception as err:
    """Captura y muestra cualquier error de validación o ejecución ocurrido durante el proceso."""
    print(f"Error: {err}")                                                                                                                 


