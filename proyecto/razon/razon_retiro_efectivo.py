from .razon import Razon

class RazonRetiroEfectivo(Razon):
    def resolver(self):
        if self.cuenta_corriente==None:
            if  self.transaccion.monto < self.transaccion.cupoDiarioRestante:
                if self.transaccion.monto < self.transaccion.saldoEnCuenta:
                    pass
                else:
                    return 'Saldo insuficiente'
            else:
                return f'Superaste el cupo diario de retiro de efectivo, el cual es de: ${self.transaccion.cupoDiarioRestante}' 
     
        else:
            if  self.transaccion.monto < self.transaccion.cupoDiarioRestante:
                if self.transaccion.monto < self.transaccion.saldoEnCuenta:
                    pass
                else:
                    if (self.transaccion.saldoEnCuenta - self.transaccion.monto) < -1*(self.cuenta_corriente.saldo_descubierto_disponible):
                        return f'Saldo insuficiente y el descubierto no puede cubrir la transferencia, recorda que tu descubierto es hasta: ${self.cuenta_corriente.saldo_descubierto_disponible}'               
            else:
                return f'Superaste el cupo diario de retiro de efectivo, el cual es de: ${self.transaccion.cupoDiarioRestante}' 
