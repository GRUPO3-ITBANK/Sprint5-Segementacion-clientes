import sys
sys.path.append(r'.\proyecto')
from evento.transacciones import TransaccionesDetalle
from cliente.direccion import direccion
import json

class Evento:
    def __init__(self):
        pass

    def load_from_json(self, fileName):
        with open(fileName, 'r') as f:
            data = json.loads(f.read())

        self.numero = data['numero']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.dni=data['dni']
        self.tipo=data['tipo']
        self.direccion = direccion(data["direccion"])
        self.transacciones = []
        for x in data["transacciones"]:
            transaccion= TransaccionesDetalle(x)
            self.transacciones.append(transaccion)
        
        
        
        
        
