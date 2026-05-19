import sys
sys.path.append("src")

from model.calculo_renta import CalculoRenta
from controller.calculo_renta_controller import CalculoRentaController

calculo = CalculoRenta(
    id_calculo=None, 
    cedula_usuario="", 
    ingreso_bruto=0.0, 
    aportes_ley=0.0, 
    deducciones=0.0, 
    renta_liquida=0.0, 
    fecha_creacion=""
)

print("Por favor ingrese los datos del calculo de renta que desea crear")

calculo.cedula_usuario = input("Cedula del Usuario : ")
calculo.ingreso_bruto = float(input("Ingreso Bruto : "))
calculo.aportes_ley = float(input("Aportes de Ley : "))
calculo.deducciones = input("Deducciones : ")  # Si deseas puedes envolverlo en float() según tu base de datos
calculo.renta_liquida = float(input("Renta Liquida : "))
calculo.fecha_creacion = input("Fecha de Creacion (AAAA-MM-DD) : ")
calculo.deducciones = float(calculo.deducciones)

CalculoRentaController.insertar_calculo(calculo)

print("Calculo insertado correctamente!")