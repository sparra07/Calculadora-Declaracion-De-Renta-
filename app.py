import sys
sys.path.append("src")

from flask import Flask, render_template, request


from controller.usuario_controller import UsuarioController
from model.usuario import Usuario
from controller.calculo_renta_controller import CalculoRentaController
from model.calculo_renta import CalculoRenta
from model.Logica_calculadora import (
    CalculadoraImpuestos, Impuestos, IngresoInvalido, 
    AportesInvalidos, IngresoCero, DeduccionFueraRango, AportesObligatorios
)

from view.web import vista_calculadora
server = Flask(__name__)

server.register_blueprint(vista_calculadora.blueprint)

if __name__ == '__main__':
    server.run(debug=True, port=8080)