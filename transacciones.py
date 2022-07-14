import json

class transacciones_clientes:
    def __init__(self):
        pass

    def load_from_json(self, fileName):
        with open(fileName, 'r') as f:
            data = json.loads(f.read())

        self.numero = data['numero']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.DNI=data['DNI']
        self.tipo=data['tipo']
        self.transacciones = []
        for x in data["transacciones"]:
            transaccion= transacciones_detalle(x)
            self.transacciones.append(transaccion)
       

class transacciones_detalle:
    def __init__(self, data):
        self.estado=data['estado']
        self.tipo=data['tipo']
        self.cuentaNumero=data['cuentaNumero']
        self.cupoDiarioRestante=data['cupoDiarioRestante']
        self.monto=data['monto']
        self.fecha=data['fecha']
        self.numero=data['numero']
        self.saldoEnCuenta=data['saldoEnCuenta']
        self.totalTarjetasDeCreditoActualmente=data['totalTarjetasDeCreditoActualmente']
        self.totalChequerasActualmente=data['totalChequerasActualmente']

    # def __str__(self):
    #     return f"estado: {self.estado}, tipo: {self.tipo}"
