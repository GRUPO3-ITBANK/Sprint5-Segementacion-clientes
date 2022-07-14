import string


class Cliente:
    def __init__(self, cliente,direccion):
        self.nombre=cliente.nombre
        self.apellido=cliente.apellido
        self.numero=cliente.numero
        self.DNI=cliente.DNI 
        self.direccion=direccion
    
    def puede_crear_chequera(self): 
        pass
    def puede_crear_tarjeta_credito(self):
        pass
    def puede_comprar_dolar(self):
        pass

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.direccion}"

