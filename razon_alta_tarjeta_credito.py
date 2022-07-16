from razon import Razon

class RazonAltaTarjetaCredito(Razon):
    def resolver(self,transaccion,evento):
        if not self.cliente.puede_crear_tarjeta_credito():
            return 'El cliente no puede crear tarjeta'
        else:
            if ( self.cliente.cant_tarjetas_credito_disp < transaccion.totalTarjetasDeCreditoActualmente + 1):
                return 'Se supera la cantidad de tarjetas de credito disponibles'