from .razon import Razon

class RazonAltaTarjetaCredito(Razon):
    def resolver(self):
        if self.cliente.puede_crear_tarjeta_credito() == False:
            return 'El cliente no puede crear tarjeta'
        else:
            cantidad_disponible = self.cliente.cuantas_tarjetas_cr_puede()
            if ( cantidad_disponible < self.transaccion.totalTarjetasDeCreditoActualmente + 1):
                return 'Se supera la cantidad de tarjetas de credito disponibles'