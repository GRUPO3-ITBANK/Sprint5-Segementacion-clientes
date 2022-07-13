from archivo_principal import Cliente, Cuenta


class Classic(Cliente):
    def puede_crear_chequera():
        return False
    def puede_crear_tarjeta_credito():
        return False
    def puede_comprar_dolar():
        return False

    Caja_ahorro_pesos = Cuenta(10000,150000,monto_CajaAhorro,0.01,0)

class Gold(Cliente):
    def puede_crear_chequera():
        return True
    #1 chequera
    def puede_crear_tarjeta_credito():
        return True

    # solo 1 tarjeta de credito
    def puede_comprar_dolar():
        return True
    Caja_ahorro_pesos = Cuenta(20000,500000,monto_CajaAhorro,0.005,0)
    Caja_ahorro_dolar = Cuenta(2000,300,20,10,5) #como seria en dolares?
    Cuenta_corriente = Cuenta(20000,500000,monto_CtaCte,0.005,10000)
    #saldo hasta de menos -10000

class Black(Cliente):
    def puede_crear_chequera():
        return True
    #dos chequeras
    def puede_crear_tarjeta_credito():
        return True

        #5 tarjetas de credito
    def puede_comprar_dolar():
        return True 
    
    Caja_ahorro_pesos = Cuenta(100000,500000,monto,0.005,10000)
    Caja_ahorro_dolar = Cuenta(2000,300,20,10,5) 
    Cuenta_corriente = Cuenta(21312,4325,34.21,10000)