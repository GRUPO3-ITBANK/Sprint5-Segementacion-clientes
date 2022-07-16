from abc import abstractmethod
from evento import Evento
from transacciones import TransaccionesDetalle
from cliente import Cliente
from tipos_clientes import  Gold, Classic, Black
from transacciones import TransaccionesDetalle

class Razon:
    @abstractmethod
    def resolver(self,transaccion: TransaccionesDetalle, evento: Evento):
        pass


    def cuentas_cliente(self,evento,transaccion):
        lista_de_cuentas=[]

        if (evento.tipo.lower()=="classic"):
            cliente = Classic(evento)
            lista_de_cuentas.append(cliente.cuenta_ahorro_pesos(transaccion.monto))
            lista_de_cuentas.append(None)
            lista_de_cuentas.append(None)
        if (evento.tipo.lower()=="gold"):
            cliente = Gold(evento)
            lista_de_cuentas.append(cliente.cuenta_ahorro_pesos(transaccion.monto))
            lista_de_cuentas.append(cliente.cuenta_ahorro_dolares(transaccion.monto))
            lista_de_cuentas.append(cliente.cuenta_corriente(transaccion.monto))
        if(evento.tipo.lower()=="black"):
            cliente = Black(evento)
            lista_de_cuentas.append(cliente.cuenta_ahorro_pesos(transaccion.monto))
            lista_de_cuentas.append(cliente.cuenta_ahorro_dolares(transaccion.monto))
            lista_de_cuentas.append(cliente.cuenta_corriente(transaccion.monto))
        
        return lista_de_cuentas
    
    def __init__(self,transaccion,evento):
        
        lista_de_cuentas = self.cuentas_cliente(evento,transaccion)
        self.caja_ahorro_pesos= lista_de_cuentas[0]
        self.caja_ahorro_dolares= lista_de_cuentas[1]
        self.cuenta_corriente= lista_de_cuentas[2]
        if (evento.tipo.lower()=="classic"):
            self.cliente= Classic(evento)
        if (evento.tipo.lower()=="gold"):
            self.cliente= Gold(evento)
        if(evento.tipo.lower()=="black"):
            self.cliente= Black(evento)
  