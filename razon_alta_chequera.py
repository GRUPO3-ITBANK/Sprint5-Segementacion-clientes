from razon import Razon

class RazonAltaChequera(Razon):
    def resolver(self):
        if not self.cliente.puede_crear_chequera():
            return 'El cliente no puede crear chequera'
        else:
            cantidad_disponible = self.cliente.cuantas_chequeras_puede()
            if ( cantidad_disponible < self.transaccion.totalChequerasActualmente + 1):
                return 'Se supera la cantidad de chequeras disponibles'