import unittest 
import sys
# Configuración del entorno: Acceso a los módulos del proyecto en la carpeta 'src'
sys.path.append('src')
from model.Logica_calculadora import CalculadoraImpuestos, Impuestos, IngresoInvalido, AportesInvalidos, IngresoCero, DeduccionFueraRango, AportesObligatorios

class TestCalculadora(unittest.TestCase):
    """Conjunto de pruebas unitarias para la lógica de cálculo de renta."""

    def test_normal_uno(self): 

        datos = Impuestos(5000000, 400000, 0)
        renta_liquida, beneficio_real, limite_legal, total = CalculadoraImpuestos.calcular_entradas(datos)

        self.assertEqual(renta_liquida, 4600000)
        self.assertEqual(beneficio_real, 1150000)
        self.assertEqual(limite_legal, 1840000)
        self.assertEqual(total, 3450000)

    def test_normal_dos(self): 
        datos = Impuestos(8000000, 640000, 600000)
        
        renta_liquida, beneficio_real, limite_legal, total = CalculadoraImpuestos.calcular_entradas(datos)

        self.assertEqual(renta_liquida, 7360000)
        self.assertEqual(beneficio_real, 2290000)
        self.assertEqual(limite_legal, 2944000)
        self.assertEqual(total, 5070000)

    def test_normal_tres(self): 
        datos = Impuestos(12000000, 960000, 500000)
        
        renta_liquida, beneficio_real, limite_legal, total = CalculadoraImpuestos.calcular_entradas(datos)
        
        self.assertEqual(renta_liquida, 11040000)
        self.assertEqual(beneficio_real, 3135000)
        self.assertEqual(limite_legal, 4416000)
        self.assertEqual(total, 7905000)

    def test_extra_uno(self): 
        datos = Impuestos(1300000, 104000, 0)
        
        renta_liquida, beneficio_real, limite_legal, total = CalculadoraImpuestos.calcular_entradas(datos)
        self.assertEqual(renta_liquida, 1196000)
        self.assertEqual(beneficio_real, 299000)
        self.assertEqual(limite_legal, 478400)
        self.assertEqual(total, 897000)

    def test_extra_dos(self): 
        datos = Impuestos(20000000, 1600000, 12000000)
        
        renta_liquida, beneficio_real, limite_legal, total = CalculadoraImpuestos.calcular_entradas(datos)
        self.assertEqual(renta_liquida, 18400000)
        self.assertEqual(beneficio_real, 13600000)
        self.assertEqual(limite_legal, 7360000)
        self.assertEqual(total, 11040000)
    
    def test_extra_tres(self): 
        datos = Impuestos(3500000, 280000, 0)
        
        renta_liquida, beneficio_real, limite_legal, total = CalculadoraImpuestos.calcular_entradas(datos)
        self.assertEqual(renta_liquida, 3220000)
        self.assertEqual(beneficio_real, 805000)
        self.assertEqual(limite_legal, 1288000)
        self.assertEqual(total, 2415000)

    def test_ingreso_negativo(self):
        """Asegura que se lance IngresoInvalido si el sueldo es menor a cero."""
        datos = Impuestos(-50000000, 400000, 0)
        with self.assertRaises(IngresoInvalido):
            CalculadoraImpuestos.calcular_entradas(datos)

    def test_aporte_ilogico(self):
        """Asegura que los aportes de ley no puedan ser superiores al ingreso bruto."""
        datos = Impuestos(1000000, 1500000, 0)
        with self.assertRaises(AportesInvalidos):
            CalculadoraImpuestos.calcular_entradas(datos)

    def test_ingreso_cero(self):
        """Valida que no se procesen declaraciones con ingreso bruto de cero."""
        datos = Impuestos(0, 0, 0)
        with self.assertRaises(IngresoCero):
            CalculadoraImpuestos.calcular_entradas(datos)

    def test_deducciones_mayores(self):
        """Valida que las deducciones no superen el dinero disponible tras aportes."""
        datos = Impuestos(2000000, 160000, 50000000)
        with self.assertRaises(DeduccionFueraRango):
            CalculadoraImpuestos.calcular_entradas(datos)

    def test_aportes_oblogatorios(self):
        """Verifica la obligatoriedad de aportes de ley para asalariados con ingresos."""
        datos = Impuestos(4000000, 0, 0)
        with self.assertRaises(AportesObligatorios):
            CalculadoraImpuestos.calcular_entradas(datos) 

if __name__ == "__main__":
    unittest.main()