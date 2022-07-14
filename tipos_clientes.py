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
       

class Gold(Cliente):
    def puede_crear_chequera(self):
        return True
    #1 chequera
    def puede_crear_tarjeta_credito(self):
        return True
    # solo 1 tarjeta de credito
    def puede_comprar_dolar(self):
        return True
    Caja_ahorro_pesos = Cuenta(20000,500000,21321,0.005,0)
    Caja_ahorro_dolar = Cuenta(2000,300,20,10,5) 
    Cuenta_corriente = Cuenta(20000,500000,123123,0.005,10000)
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
    
    Caja_ahorro_pesos = Cuenta(100000,500000,21312321,0.005,10000)
    Caja_ahorro_dolar = Cuenta(2000,300,20,10,5) 
    Cuenta_corriente = Cuenta(21312,4325,34.21,4,10000)