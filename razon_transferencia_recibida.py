from razon import Razon

class RazonTransferenciaRecibida(Razon):
    def resolver(self):
        
        if (self.evento.tipo.lower() == 'classic' or self.evento.tipo.lower() == 'gold'):
            if self.transaccion.monto > self.caja_ahorro_pesos.limite_transferencia_recibida:
                if self.evento.tipo.lower() == 'classic':
                    return f'La transferencia a recibir supera los ${self.caja_ahorro_pesos.limite_transferencia_recibida} que es tu limite de extracción a recibir'
                else:
                    return f'Las transferencias a recibir que supera los ${self.caja_ahorro_pesos.limite_transferencia_recibida} deben ser autorizadas previamente'
 