from operator import truediv
import string

class Cliente:
    nombre=string
    apellido=string
    numero=string
    dni=string

    def __init__(self,nombre,apellido,numero,dni,direccion):
        self.nombre=nombre
        self.apellido=apellido
        self.numero=numero
        self.dni=dni 
        self.direccion=direccion
        print('soy cliente')
    def puede_crear_chequera(bool): 
        return bool
    def puede_crear_tarjeta_credito(bool):
        pass
    def puede_comprar_dolar(bool):
        pass
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.direccion}"

class Direccion:
    calle=string
    ciudad=string
    provincia=string
    pais=string
    def __init__(self,calle,numero,ciudad,provincia,pais):
        self.calle=calle
        self.numero=numero
        self.ciudad=ciudad
        self.provincia=provincia
        self.pais=pais
    def __str__(self):
        return f"{self.calle}, {self.numero}"

class Cuenta:
    limite_extraccion_diario:float


clienteNuchi=Cliente("nuchi","jauch","2901540843","42471466", Direccion("ciudad de la paz","70","ush","p","pais"))
print(clienteNuchi)

class Cuenta:
    limite_extraccion_diario:float
    limite_transferencia_recibida:float
    monto:float
    costo_transferencias:float
    saldo_descubierto_disponible:float

