import unittest
import sys
sys.path.append('src')

from model.calculo_renta import CalculoRenta
from controller.calculo_renta_controller import CalculoRentaController

class TestCalculoRenta(unittest.TestCase):

    # Text fixture
    @classmethod
    def setUpClass(cls):   
        CalculoRentaController.borrar_tabla()
        CalculoRentaController.crear_tabla()

    def test_1_calculo_renta_creacion_normal(self):
        calculo_prueba = CalculoRenta(
            id_calculo=1,
            cedula_usuario='135827326483',
            ingreso_bruto=85000000,
            aportes_ley=3400000,
            deducciones=12000000,
            renta_liquida=69600000,
            fecha_creacion='2026-05-18'
        )
        
        CalculoRentaController.insertar_calculo(calculo_prueba)

        calculo_encontrado = CalculoRentaController.buscar_calculo(calculo_prueba.id_calculo)      
        self.assertTrue(calculo_encontrado.is_equal(calculo_prueba))
    
    def test_2_calculo_renta_campos_vacios_opcionales(self):
        calculo_prueba = CalculoRenta(
            id_calculo=2,
            cedula_usuario='456123789',
            ingreso_bruto=0,
            aportes_ley=0,
            deducciones=0,
            renta_liquida=0,
            fecha_creacion='2026-05-18'
        )
        CalculoRentaController.insertar_calculo(calculo_prueba)
        calculo_encontrado = CalculoRentaController.buscar_calculo(calculo_prueba.id_calculo)      
        
        self.assertIsNotNone(calculo_encontrado)
        self.assertTrue(calculo_encontrado.is_equal(calculo_prueba))
    
    def test_3_calculo_renta_precision_valores_decimales(self):
        """Garantiza que el negocio procese centavos con total exactitud y deje la demanda satisfecha sin redondeos destructivos."""
        calculo_prueba = CalculoRenta(
            id_calculo=None,
            cedula_usuario='987654321',
            ingreso_bruto=45000050.75,   # Con centavos
            aportes_ley=1800000.25,      # Con centavos
            deducciones=3500000.00,
            renta_liquida=39700050.50,   # Con centavos
            fecha_creacion='2026-05-18'
        )
        CalculoRentaController.insertar_calculo(calculo_prueba)
        calculo_encontrado = CalculoRentaController.buscar_calculo(calculo_prueba.id_calculo)      
        
        self.assertIsNotNone(calculo_encontrado)
        self.assertTrue(calculo_encontrado.is_equal(calculo_prueba))

    def test_4_calculo_renta_valores_extremos_o_negativos(self):
        calculo_prueba = CalculoRenta(
            id_calculo=None,
            cedula_usuario='999888777',
            ingreso_bruto=10000000,
            aportes_ley=400000,
            deducciones=15000000,   
            renta_liquida=-5400000,  
            fecha_creacion='2026-05-18'
        )
        CalculoRentaController.insertar_calculo(calculo_prueba)
        calculo_encontrado = CalculoRentaController.buscar_calculo(calculo_prueba.id_calculo)
        
        self.assertIsNotNone(calculo_encontrado)
        self.assertTrue(calculo_encontrado.is_equal(calculo_prueba))

    def test_5_calculo_renta_altos_volumenes_financieros(self):
        calculo_prueba = CalculoRenta(
            id_calculo=None,
            cedula_usuario='2342356789',
            ingreso_bruto=12500000000,  
            aportes_ley=500000000,
            deducciones=2000000000,
            renta_liquida=10000000000, 
            fecha_creacion='2026-05-18'
        )
        CalculoRentaController.insertar_calculo(calculo_prueba)
        calculo_encontrado = CalculoRentaController.buscar_calculo(calculo_prueba.id_calculo)
        
        self.assertIsNotNone(calculo_encontrado)
        self.assertTrue(calculo_encontrado.is_equal(calculo_prueba))

if __name__ == '__main__':
    unittest.main()