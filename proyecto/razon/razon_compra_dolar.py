from razon import Razon

class RazonCompraDolar(Razon):
    def resolver(self):
        if not self.cliente.puede_comprar_dolar():
            return 'No puede comprar dolares'
        
        if self.transaccion.monto > self.transaccion.saldoEnCuenta:
            return 'Saldo insuficiente para compra de dolares'
