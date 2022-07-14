from movimientos_clientes import movimientos_clientes
from tipos_clientes import Black, Gold, Classic
# se importa la transaccion - mediante arg, pasar el json
cliente_detalle = movimientos_clientes()
cliente_detalle.load_from_json('eventos_classic.json')

# #si todo okay - implementar logica de validacion
match cliente_detalle.tipo.lower():
    case 'classic':
        cliente = Classic(cliente_detalle)
        for t in cliente_detalle.transacciones:
            print(cliente.cuenta_ahorro_pesos((t.monto)))
            pass
    case 'gold':
        cliente = Gold(cliente_detalle)
        for t in cliente_detalle.transacciones:
            print(cliente.cuenta_ahorro_pesos((t.monto)))
            print(cliente.cuenta_ahorro_dolares(t.monto))
            print(cliente.cuenta_corriente(t.monto))
            pass
    case 'black':
        cliente = Black(cliente_detalle)
        for t in cliente.transacciones:
            print(cliente.cuenta_ahorro_pesos(t.monto))
            print(cliente.cuenta_ahorro_dolares(t.monto))
            print(cliente.cuenta_corriente(t.monto))
            pass
        #max extraccion 100 000 por dia
        pass

try:
    if cliente_detalle.estado.lower() == "aceptada":
        pass #hay que poner que directamente lo imprima
    else:   #es rechazada --> hay que poner porque
        assert ()
except:
    pass
    # assert nombre:
    #     lo que tiene que 
    
