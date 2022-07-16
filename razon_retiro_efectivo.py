from razon import Razon

class RazonRetiroEfectivo(Razon):
    def resolver(self):
        if  self.transaccion.monto < self.transaccion.cupoDiarioRestante:
            if self.transaccion.monto < self.transaccion.saldoEnCuenta:
                pass
            else:
                return 'Saldo insuficiente'
        else:
            return f'Superaste el cupo diario de retiro de efectivo, el cual es de: ${self.transaccion.cupoDiarioRestante}' 
