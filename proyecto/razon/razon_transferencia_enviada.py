from razon import Razon

class RazonTransferenciaEnviada(Razon):
    def resolver(self):      
        transferencia_con_costo = self.caja_ahorro_pesos.monto + self.caja_ahorro_pesos.costo_transferencias


        if self.cuenta_corriente == None:
            if transferencia_con_costo < self.caja_ahorro_pesos.limite_extraccion_diario:
                if self.transaccion.saldoEnCuenta > transferencia_con_costo:
                    pass
                else:
                    return 'Estás intentando transferir más plata de la que tenes en cuenta'
            else:
                return f'La transferencia a realizar supera los ${self.caja_ahorro_pesos.limite_extraccion_diario} que es tu limite de extracción diario'
        else: #es decir, si cuenta con cuenta corriente...
            if transferencia_con_costo < self.caja_ahorro_pesos.limite_extraccion_diario:
                if self.transaccion.saldoEnCuenta > transferencia_con_costo:
                    pass
                else:
                    if (self.transaccion.saldoEnCuenta - transferencia_con_costo < -1*(self.cuenta_corriente.saldo_descubierto_disponible)):
                        return f'El descubierto no puede cubrir la transferencia, recorda que tu descubierto es hasta: ${self.cuenta_corriente.saldo_descubierto_disponible}'
            else:
                return f'La transferencia superan los ${self.caja_ahorro_pesos.limite_extraccion_diario} que es tu limite de extracción diario'
