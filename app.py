import sys
sys.path.append("src")

from flask import Flask, render_template, request

# Importaciones de tu proyecto
from controller.usuario_controller import UsuarioController
from model.usuario import Usuario
from controller.calculo_renta_controller import CalculoRentaController
from model.calculo_renta import CalculoRenta

server = Flask(__name__)

# =========================================================================
# RUTA INICIAL PRINCIPAL
# =========================================================================
@server.route("/")
def pagina_inicio():
    return render_template("pagina_inicio.html")


# =========================================================================
# MÓDULO USUARIOS
# =========================================================================

@server.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

@server.route("/insertar_usuario")
def insertar_usuario():
    try:
        usuario = Usuario(
            cedula=request.args["cedula"],
            nombre=request.args["nombre"],
            apellido=request.args["apellido"],
            telefono=request.args["telefono"],
            correo=request.args["correo"],
            direccion=request.args["direccion"]
        )
        UsuarioController.insertar_usuario(usuario)
        return f"Se guardó exitosamente el usuario con cédula: {request.args['cedula']}.<br /><a href='/'>Volver al inicio</a>"
    except Exception as e:
        return f"Error al insertar el usuario: {str(e)}.<br /><a href='/'>Volver al inicio</a>"

@server.route("/buscar_usuario")
def buscar_usuario():
    try:
        cedula = request.args["cedula"]
        usuario = UsuarioController.buscar_usuario(cedula)
        if not usuario:
            return "No se encontró ningún usuario con esa cédula.<br /><a href='/'>Volver al inicio</a>"
        return render_template("ver_usuario.html", usuario=usuario)
    except Exception as e:
        return "No se encontró ningún usuario con esa cédula.<br /><a href='/'>Volver al inicio</a>"

@server.route("/modificar_usuario")
def modificar_usuario():
    try:
        cedula = request.args["cedula"]
        usuario = UsuarioController.buscar_usuario(cedula)
        if not usuario:
            return "No se encontró ningún usuario con esa cédula.<br /><a href='/'>Volver al inicio</a>"
        return render_template("modificar_usuario.html", usuario=usuario)
    except Exception as e:
        return "No se encontró ningún usuario con esa cédula.<br /><a href='/'>Volver al inicio</a>"

@server.route("/actualizar_usuario")
def actualizar_usuario():
    try:
        usuario = Usuario(
            cedula=request.args["cedula"],
            nombre=request.args["nombre"],
            apellido=request.args["apellido"],
            telefono=request.args["telefono"],
            correo=request.args["correo"],
            direccion=request.args["direccion"]
        )
        UsuarioController.actualizar_usuario(usuario)
        return "Usuario modificado exitosamente.<br /><a href='/'>Volver al inicio</a>"
    except Exception as e:
        return f"Error al modificar el usuario: {str(e)}.<br /><a href='/'>Volver al inicio</a>"

@server.route("/eliminar_usuario")
def eliminar_usuario():
    try:
        cedula = request.args["cedula"]
        UsuarioController.eliminar_usuario_por_cedula(cedula)
        return "Usuario eliminado exitosamente. <a href='/'>Volver al inicio</a>"
    except Exception as e:
        return f"Error al eliminar usuario: {str(e)}.<br /><a href='/'>Volver al inicio</a>"


# =========================================================================
# MÓDULO CÁLCULOS DE RENTA
# =========================================================================

@server.route("/calculos")
def calculos():
    return render_template("calculos.html")

@server.route("/insertar_calculo")
def insertar_calculo():
    try:
        calculo = CalculoRenta(
            id_calculo=None,
            cedula_usuario=request.args["cedula_usuario"],
            ingreso_bruto=float(request.args["ingreso_bruto"].replace(".", "")),
            aportes_ley=float(request.args["aportes_ley"].replace(".", "")),
            deducciones=float(request.args["deducciones"].replace(".", "")),
            renta_liquida=float(request.args["renta_liquida"].replace(".", "")),
            fecha_creacion=request.args["fecha_creacion"]
        )
        id_calculo = CalculoRentaController.insertar_calculo(calculo)
        return f"Se guardó exitosamente el cálculo para la cédula: {request.args['cedula_usuario']} con el ID: {id_calculo}.<br /><a href='/'>Volver al inicio</a>"
    except Exception as e:
        return f"Error al insertar el cálculo: {str(e)}.<br /><a href='/'>Volver al inicio</a>"

@server.route("/buscar_calculo")
def buscar_calculo():
    try:
        cedula_usuario = request.args["cedula_usuario"]
        lista_calculos = CalculoRentaController.buscar_calculos_por_usuario(cedula_usuario)
        if len(lista_calculos) == 0:
            return "No se encontró ningún cálculo para esa cédula.<br /><a href='/'>Volver al inicio</a>"
        return render_template("ver_calculos.html", calculos=lista_calculos)
    except Exception as e:
        return "No se encontró ningún cálculo para esa cédula.<br /><a href='/'>Volver al inicio</a>"

@server.route("/modificar_calculo")
def modificar_calculo():
    try:
        id_calculo = int(request.args["id_calculo"])
        calculo = CalculoRentaController.buscar_calculo_por_id(id_calculo)
        if not calculo:
            return "No se encontró ningún cálculo con ese ID.<br /><a href='/'>Volver al inicio</a>"
        return render_template("modificar_calculo.html", calculo=calculo)
    except Exception as e:
        return "No se encontró ningún cálculo con ese ID.<br /><a href='/'>Volver al inicio</a>"

@server.route("/actualizar_calculo")
def actualizar_calculo():
    try:
        calculo = CalculoRenta(
            id_calculo=int(request.args["id_calculo"]),
            cedula_usuario=request.args["cedula_usuario"],
            ingreso_bruto=float(request.args["ingreso_bruto"].replace(".", "")),
            aportes_ley=float(request.args["aportes_ley"].replace(".", "")),
            deducciones=float(request.args["deducciones"].replace(".", "")),
            renta_liquida=float(request.args["renta_liquida"].replace(".", "")),
            fecha_creacion=request.args["fecha_creacion"]
        )
        CalculoRentaController.actualizar_calculo(calculo)
        return f"Cálculo modificado exitosamente. <a href='/'>Volver al inicio</a>"
    except Exception as e:
        return f"Error al actualizar el cálculo: {str(e)}.<br /><a href='/'>Volver al inicio</a>"

@server.route("/eliminar_calculo")
def eliminar_calculo():
    try:
        id_calculo = int(request.args["id_calculo"])
        CalculoRentaController.eliminar_calculo_por_id(id_calculo)
        return "Cálculo eliminado exitosamente. <a href='/'>Volver al inicio</a>"
    except Exception as e:
        return f"Error al eliminar el cálculo: {str(e)}.<br /><a href='/'>Volver al inicio</a>"


@server.route("/crear_tablas")
def crear_tablas():
    try:
        UsuarioController.crear_tabla()
        CalculoRentaController.crear_tabla()
        return "Tablas creadas exitosamente. Ya puede usar la aplicación.<br /><a href='/'>Volver al inicio</a>"
    except Exception as e:
        return "Las tablas ya existen o se presentó un error de conexión. Ya puede usar la aplicación.<br /><a href='/'>Volver al inicio</a>"


if __name__ == '__main__':
    server.run(debug=True, port=8080)