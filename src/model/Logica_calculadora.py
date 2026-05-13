class IngresoInvalido( Exception ): 
    """ Se dispara cuando el ingreso es negativo """
    def __init__( self):
    # Llama al constructor de la excepción con el mensaje de error específico
        super().__init__( f"El valor del ingreso bruto debe ser mayor que cero" )

class AportesInvalidos( Exception ): 
    """ Se dispara cuando los aportes de ley superan los ingresos """
    def __init__( self ):
    # Llama al constructor para indicar inconsistencia entre aportes e ingresos
        super().__init__( f"Los aportes de ley no pueden ser mayores al ingreso bruto" )

class IngresoCero( Exception ): 
    """ Se dispara cuando el ingreso es cero """
    def __init__( self ):
    # Llama al constructor para informar que se requieren ingresos para el cálculo
        super().__init__( f"El usuario debe de tener ingresos" )

class DeduccionFueraRango( Exception ): 
    """ Se dispara si las deducciones superan la renta liquida """
    def __init__( self ):
    # Llama al constructor para indicar que las deducciones exceden el límite permitido    
        super().__init__( f"Las deducciones estan fuera de rango" )

class AportesObligatorios( Exception ): 
    """ Se dispara si no hay aportes siendo asalariado """
    def __init__( self ):
    # Llama al constructor para exigir los aportes obligatorios de salud y pensión
        super().__init__( f"Aportes de ley obligatorios faltantes, todo asalariado debe aportar a salud y pension" )

class Impuestos():
    """ Representa los datos de entrada para el cálculo (Como la clase Purchase) """
    ingreso_bruto : float
    aportes_ley : float
    deducciones : float

    def __init__(self, ingreso_bruto, aportes_ley, deducciones):
        self.ingreso_bruto = ingreso_bruto
        self.aportes_ley = aportes_ley
        self.deducciones = deducciones

class CalculadoraImpuestos:
    """ Clase para realizar operaciones financieras de impuestos """

    def calcular_entradas( impuestos : Impuestos ):
        """ Calcula la renta liquida, beneficio real, limite legal y total """

        CalculadoraImpuestos.comprobar_ingreso(impuestos.ingreso_bruto)
        CalculadoraImpuestos.comprobar_aportes(impuestos.aportes_ley, impuestos.ingreso_bruto)
        CalculadoraImpuestos.comprobar_obligaciones(impuestos.ingreso_bruto, impuestos.aportes_ley)

        # Lógica de cálculo
        renta_liquida = impuestos.ingreso_bruto - impuestos.aportes_ley

        # Validación de deducciones después de calcular renta_liquida
        CalculadoraImpuestos.comprobar_deducciones(impuestos.deducciones, renta_liquida)

        beneficio_real = impuestos.deducciones + ((renta_liquida - impuestos.deducciones) * 0.25)
        limite_legal = renta_liquida * 0.40

        if beneficio_real > limite_legal:
            total = renta_liquida - limite_legal
        else:
            total = renta_liquida - beneficio_real

        return renta_liquida, beneficio_real, limite_legal, total
    
    def comprobar_ingreso(ingreso):
        if ingreso < 0 :
            raise IngresoInvalido()
        if ingreso == 0 :
            raise IngresoCero()

    def comprobar_aportes(aportes, ingreso):
        if aportes > ingreso :
            raise AportesInvalidos()

    def comprobar_obligaciones(ingreso, aportes):
        if ingreso > 0 and aportes == 0 :
            raise AportesObligatorios()

    def comprobar_deducciones(deducciones, renta_liquida):
        if deducciones > renta_liquida :
            raise DeduccionFueraRango()