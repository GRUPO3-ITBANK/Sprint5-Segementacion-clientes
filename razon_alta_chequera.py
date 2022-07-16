from razon import Razon

class RazonAltaChequera(Razon):
    def resolver(self,transaccion,evento):
        if not self.cliente.puede_crear_chequera():
            return 'El cliente no puede crear chequera'
        else:
            if ( self.cliente.cant_chequeras_disp < transaccion.totalChequerasActualmente + 1):
                return 'Se supera la cantidad de chequeras disponibles'