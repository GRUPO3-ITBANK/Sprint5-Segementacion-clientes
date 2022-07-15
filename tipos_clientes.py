from cliente import Cliente
from cuenta import Cuenta

class Classic(Cliente):
    def puede_crear_chequera(self):
        return False
    def puede_crear_tarjeta_credito(self):
        return False
    def puede_comprar_dolar(self):
        return False

    def cuenta_ahorro_pesos(self,monto):
        caja_ahorro_pesos = Cuenta(10000,150000,monto,monto*0.01,0)
        return caja_ahorro_pesos

class Gold(Cliente):
    def puede_crear_chequera(self):
        return True
        #1 chequera
    def puede_crear_tarjeta_credito(self):
        return True
        # solo 1 tarjeta de credito
    def puede_comprar_dolar(self):
        return True

    def cuenta_ahorro_pesos(self,monto):
        caja_ahorro_pesos = Cuenta(20000,500000,monto,monto*0.005,0)
        return caja_ahorro_pesos
    def cuenta_ahorro_dolares(self,monto):
        caja_ahorro_dolar = Cuenta(2000,300,monto,monto*0.005,0) 
        return caja_ahorro_dolar
    def cuenta_corriente(self,monto):
        cuenta_corriente = Cuenta(20000,500000,monto,monto*0.005,10000)
        return cuenta_corriente
    
    #saldo hasta de menos -10000

class Black(Cliente):
    def puede_crear_chequera(self):
        return True
    #dos chequeras
    def puede_crear_tarjeta_credito(self):
        return True
    #5 tarjetas de credito
    def puede_comprar_dolar(self):
        return True 
    
    
    def cuenta_ahorro_pesos(self,monto):
        caja_ahorro_pesos = Cuenta(100000,None,500000,monto,0,0)
        return caja_ahorro_pesos
    def cuenta_ahorro_dolares(self,monto):
        caja_ahorro_dolar = Cuenta(2000,None,monto,0,0)  
        return caja_ahorro_dolar
    def cuenta_corriente(self,monto):
        cuenta_corriente = Cuenta(100000,None,monto,0,10000)
        return cuenta_corriente
    
    
    
    
