from razon import Razon
from evento import Evento
from cliente.tipos_clientes import Classic, Gold, Black


class RazonCompraDolar(Razon):
    def resolver(self):
        if not self.cliente.puede_comprar_dolar():
            return 'No puede comprar dolares'
        
        if self.transaccion.monto > self.transaccion.saldoEnCuenta:
            return 'Saldo insuficiente para compra de dolares'
