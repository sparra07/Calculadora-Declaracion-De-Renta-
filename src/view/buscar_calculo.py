import sys
sys.path.append("src")

from datetime import date

from model.calculo_renta import CalculoRenta
from controller.calculo_renta_controller import CalculoRentaController

try:
    id_calculo = input("Ingrese el ID del calculo que desea buscar: ")
    calculo_buscado = CalculoRentaController.buscar_calculo(int(id_calculo))
    
    if calculo_buscado:
        print(f"Usuario encontrado, con cedula : {calculo_buscado.cedula_usuario}")
    else:
        print("No se encontro ningun calculo con ese ID.")
except Exception as err:
    print("Error : ")
    print(str(err))