class CalculoRenta:
    def __init__(self, id_calculo, cedula_usuario, ingreso_bruto, aportes_ley, deducciones, fecha_creacion, renta_liquida=None):
        self.id_calculo = id_calculo
        self.cedula_usuario = str(cedula_usuario)
        self.ingreso_bruto = float(ingreso_bruto)
        self.aportes_ley = float(aportes_ley)
        self.deducciones = float(deducciones)
        self.fecha_creacion = str(fecha_creacion)
        # Si no se pasa renta_liquida, se calcula automáticamente
        self.renta_liquida = float(renta_liquida) if renta_liquida is not None else (self.ingreso_bruto - self.aportes_ley - self.deducciones)
        self.income_bruto = self.ingreso_bruto

    def is_equal(self, otro):
        if not isinstance(otro, CalculoRenta):
            return False
        # Comparamos los valores clave (evitando comparar ID si uno es None debido a la generación en BD)
        return (self.cedula_usuario == otro.cedula_usuario and
                abs(self.ingreso_bruto - otro.ingreso_bruto) < 0.01 and
                abs(self.aportes_ley - otro.aportes_ley) < 0.01 and
                abs(self.deducciones - otro.deducciones) < 0.01)