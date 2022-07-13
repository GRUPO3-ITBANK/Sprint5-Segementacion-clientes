from archivo_principal import Cliente, Cuenta

class Classic(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion, puede_crear_chequera, puede_crear_tarjeta_credito, puede_comprar_dolar):
        Cliente.__init__(nombre, apellido, numero, dni, direccion)  #llamo al constructor de cliente
        #agrego los atributos nuevos
        self.puede_crear_chequera = False
        self.puede_crear_tarjeta_credito = False
        self.puede_comprar_dolar = False

    Caja_ahorro_pesos = Cuenta(10000,150000,monto_CajaAhorro,0.01,0)

class Gold(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion, puede_crear_chequera, puede_crear_tarjeta_credito, puede_comprar_dolar):
        Cliente.__init__(nombre, apellido, numero, dni, direccion)  #llamo al constructor de cliente
        #agrego los atributos nuevos
        self.puede_crear_chequera = True    #solo puede tener 1 chequera
        self.puede_crear_tarjeta_credito = True   #solo puede tener 1 tarjeta de credito
        self.puede_comprar_dolar = True

    Caja_ahorro_pesos = Cuenta(20000,500000,monto_CajaAhorro,0.005,0)
    Caja_ahorro_dolar = Cuenta(2000,300,20,10,5) #como seria en dolares?
    Cuenta_corriente = Cuenta(20000,500000,monto_CtaCte,0.005,10000)
    #saldo hasta de menos -10000

class Black(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion, puede_crear_chequera, puede_crear_tarjeta_credito, puede_comprar_dolar):
        Cliente.__init__(nombre, apellido, numero, dni, direccion)  #llamo al constructor de cliente
        #agrego los atributos nuevos
        self.puede_crear_chequera = True    #puede tener 2 chequeras
        self.puede_crear_tarjeta_credito = True   #puede tener 5 tarjetas de credito
        self.puede_comprar_dolar = True

    Caja_ahorro_pesos = Cuenta(100000,500000,monto,0.005,10000)
    Caja_ahorro_dolar = Cuenta(2000,300,20,10,5) 
    Cuenta_corriente = Cuenta(21312,4325,34.21,10000)