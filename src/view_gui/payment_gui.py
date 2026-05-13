import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

from src.model.Logica_calculadora import Impuestos, CalculadoraImpuestos

class RentaApp(App):
    def build(self):

        self.title = "Calculadora del valor de la renta"
        contenedor = GridLayout(cols=2, padding=20, spacing=20)

        contenedor.add_widget(Label(text="Ingreso Bruto"))
        self.ingreso = TextInput(font_size=30)
        contenedor.add_widget(self.ingreso)

        contenedor.add_widget(Label(text="Aportes de Ley"))
        self.aportes = TextInput(font_size=30)
        contenedor.add_widget(self.aportes)

        contenedor.add_widget(Label(text="Deducciones"))
        self.deducciones = TextInput(font_size=30)
        contenedor.add_widget(self.deducciones)

        # Etiquetas para el desglose
        contenedor.add_widget(Label(text="Renta Líquida"))
        self.label_renta = Label(text="-")
        contenedor.add_widget(self.label_renta)

        contenedor.add_widget(Label(text="Beneficio Real"))
        self.label_beneficio = Label(text="-")
        contenedor.add_widget(self.label_beneficio)

        contenedor.add_widget(Label(text="Límite Legal"))
        self.label_limite = Label(text="-")
        contenedor.add_widget(self.label_limite)

        contenedor.add_widget(Label(text="Total a Pagar"))
        self.resultado = Label(text="-")
        contenedor.add_widget(self.resultado)

        calcular = Button(text="Calcular", font_size=40)
        contenedor.add_widget(calcular)
        calcular.bind(on_press=self.calcular_renta)

        limpiar = Button(text="Limpiar", font_size=40)
        contenedor.add_widget(limpiar)
        limpiar.bind(on_press=self.limpiar_campos)

        # Historial
        contenedor.add_widget(Label(text="Historial de cálculos", font_size=20))
        contenedor.add_widget(Label(text=""))

        self.historial = []
        self.label_historial = Label(text="Sin cálculos aún", font_size=18)
        contenedor.add_widget(self.label_historial)

        return contenedor

    def calcular_renta(self, value):
        try:
            self.validar()

            datos = Impuestos(
                ingreso_bruto=float(self.ingreso.text),
                aportes_ley=float(self.aportes.text),
                deducciones=float(self.deducciones.text)
            )

            renta_liquida, beneficio_real, limite_legal, total = CalculadoraImpuestos.calcular_entradas(datos)

            # Mostrar desglose
            self.label_renta.text = str(round(renta_liquida, 2))
            self.label_beneficio.text = str(round(beneficio_real, 2))
            self.label_limite.text = str(round(limite_legal, 2))
            self.resultado.text = str(round(total, 2))

            # Guardar en historial (máximo 5)
            entrada = "Ingreso: " + self.ingreso.text + " | Total: " + str(round(total, 2))
            self.historial.append(entrada)
            if len(self.historial) > 5:
                self.historial.pop(0)

            self.label_historial.text = "\n".join(self.historial)

        except ValueError:
            self.resultado.text = "El valor ingresado no es válido"

        except Exception as err:
            self.mostrar_error(err)

    def limpiar_campos(self, value):
        self.ingreso.text = ""
        self.aportes.text = ""
        self.deducciones.text = ""
        self.label_renta.text = "-"
        self.label_beneficio.text = "-"
        self.label_limite.text = "-"
        self.resultado.text = "-"

    def mostrar_error(self, err):
        contenido = GridLayout(cols=1)

        contenido.add_widget(Label(text=str(err)))

        cerrar = Button(text="Cerrar")
        contenido.add_widget(cerrar)

        popup = Popup(title="Error", content=contenido)

        cerrar.bind(on_press=popup.dismiss)

        popup.open()

    def validar(self):

        if not (self.ingreso.text.replace('.', '', 1).isdigit()):
            raise Exception("El ingreso bruto debe ser un número válido")

        if not (self.aportes.text.replace('.', '', 1).isdigit()):
            raise Exception("Los aportes deben ser un número válido")

        if not (self.deducciones.text.replace('.', '', 1).isdigit()):
            raise Exception("Las deducciones deben ser un número válido")


if __name__ == "__main__":
    RentaApp().run()