class CalculoRenta:
    def __init__(self, id_calculo, cedula_usuario, ingreso_bruto, aportes_ley, deducciones, renta_liquida, fecha_creacion):
   
        self.id_calculo = id_calculo
        self.cedula_usuario = cedula_usuario
        self.ingreso_bruto = ingreso_bruto
        self.aportes_ley = aportes_ley
        self.deducciones = deducciones
        self.renta_liquida = renta_liquida
        self.fecha_creacion = fecha_creacion

    def is_equal(self, otro): 
        return (self.id_calculo == otro.id_calculo and
                self.cedula_usuario == otro.cedula_usuario and
                float(self.ingreso_bruto) == float(otro.ingreso_bruto) and
                float(self.aportes_ley) == float(otro.aportes_ley) and
                float(self.deducciones) == float(otro.deducciones) and
                float(self.renta_liquida) == float(otro.renta_liquida) and
                str(self.fecha_creacion) == str(otro.fecha_creacion))