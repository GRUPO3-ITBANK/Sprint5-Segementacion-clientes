import sys
sys.path.append(r'.\proyecto')
from abc import abstractmethod
from evento.evento import Evento
from evento.transacciones import TransaccionesDetalle
from cliente.tipos_clientes import Gold, Classic, Black


class Razon:
    @abstractmethod
    def resolver(self,transaccion: TransaccionesDetalle, evento: Evento):
        pass


    def cuentas_cliente(self,transaccion):
        lista_de_cuentas=[]
        if (self.cliente.tiene_cta_corriente() == True) and (self.cliente.tiene_cta_dolar() == True):
            lista_de_cuentas.append(self.cliente.cuenta_ahorro_pesos(transaccion.monto)) #0 
            lista_de_cuentas.append(self.cliente.cuenta_ahorro_dolares(transaccion.monto)) #1
            lista_de_cuentas.append(self.cliente.cuenta_corriente(transaccion.monto)) #2
        else:
            lista_de_cuentas.append(self.cliente.cuenta_ahorro_pesos(transaccion.monto))
            lista_de_cuentas.append(None)
            lista_de_cuentas.append(None)
        
        return lista_de_cuentas
    
    def __init__(self,transaccion,evento):
        self.transaccion = transaccion
        self.evento = evento
        
        if (evento.tipo.lower()=="classic"):
            self.cliente= Classic(evento)
        if (evento.tipo.lower()=="gold"):
            self.cliente= Gold(evento)
        if(evento.tipo.lower()=="black"):
            self.cliente= Black(evento)

        lista_de_cuentas = self.cuentas_cliente(transaccion)
        self.caja_ahorro_pesos= lista_de_cuentas[0]
        self.caja_ahorro_dolares= lista_de_cuentas[1]
        self.cuenta_corriente= lista_de_cuentas[2]