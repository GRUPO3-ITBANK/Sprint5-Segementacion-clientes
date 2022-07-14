from transacciones import transacciones_detalle, transacciones_clientes
from cliente import Cliente
from direccion import Direccion
from tipos_clientes import Black, Gold, Classic
# se importa la transaccion - mediante arg, pasar el json
transaccion = transacciones_clientes()
transaccion.load_from_json('datos.json')
direccion = Direccion("calle","231","ciu","pro","pais")

# #si todo okay - implementar logica de validacion
match transaccion.tipo.lower():
    case 'classic':
        cliente = Classic(transaccion,direccion)
        for t in transaccion.transacciones:
            cliente.cuenta_ahorro_pesos(t.monto)
        pass
    case 'gold':
        cliente = Gold(transaccion,direccion)
        
        pass
    case 'black':
        cliente = Black(transaccion,direccion)
        pass
