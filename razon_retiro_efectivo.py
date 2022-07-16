from razon import Razon

class RazonRetiroEfectivo(Razon):
    def resolver(self,transaccion,evento):

        if  transaccion.monto < transaccion.cupoDiarioRestante:
            if transaccion.monto < transaccion.saldoEnCuenta:
                pass
            else:
                return 'Saldo insuficiente'
        else:
            return f'Superaste el cupo diario de retiro de efectivo, el cual es de: ${transaccion.cupoDiarioRestante}' 
