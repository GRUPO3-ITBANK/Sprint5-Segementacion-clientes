from movimientos_clientes import movimientos_clientes
from tipos_clientes import Black, Gold, Classic

# se importa los clientes con sus transacciones - mediante arg, pasar el json
evento = movimientos_clientes()
evento.load_from_json('eventos_classic.json')

clienteClassic = Classic(evento)
clienteGold = Gold(evento)
clienteBlack = Black(evento)

#si todo okay - implementar logica de validacion

match evento.tipo.lower():
    case 'classic':
        
        for t in evento.transacciones:
            cta_ahorro_pesos=clienteClassic.cuenta_ahorro_pesos(t.monto)
             #Costo de transferencia
            if t.estado.lower() == "rechazada":
                match t.tipo.lower():
                    case 'retiro_efectivo_cajero_automatico':
                        pass
                    case 'alta_tarjeta_credito':
                        print('Cliente classic no tiene acceso a tarjeta de credito')
                        pass
                    case 'alta_chequera':
                        print('Cliente classic no tiene acceso a chequeras')
                        pass
                    case 'comprar_dolar':
                        print('Cliente classic no tiene caja de ahorro en dolares, no tiene permitido comprar dolares')
                        pass
                    case 'transferencia_enviada':
                        if cta_ahorro_pesos.limite_extraccion_diario > (t.monto + cta_ahorro_pesos.costo_transferencias):
                           if (t.monto + cta_ahorro_pesos) < t.saldoEnCuenta:
                            print('No tenes fondo disponible')
                        else:
                            print('Tranferencia supera limite de extracción')
                    case 'transferencia_recibida':
                        pass
            pass

    case 'gold':
        for t in evento.transacciones:
            cta_ahorro_pesos=clienteGold.cuenta_ahorro_pesos(t.monto)
            cta_ahorro_pesos.limite_extraccion_diario #Costo de transferencia


            cta_ahorro_dolar=clienteGold.cuenta_ahorro_dolares(t.monto)
            cta_ahorro_dolar.limite_extraccion_diario #Costo de transferencia


            cta_corriente=clienteGold.cuenta_corriente(t.monto)
            cta_corriente.limite_extraccion_diario #Costo de transferencia
            pass
    case 'black':
        for t in evento.transacciones:
            cta_ahorro_pesos=clienteBlack.cuenta_ahorro_pesos(t.monto)
            cta_ahorro_pesos.limite_extraccion_diario #Costo de transferencia
            cta_ahorro_pesos.limite_transferencia_recibida #limite de transferencia recibida
            cta_ahorro_pesos.monto #monto
            cta_ahorro_pesos.costo_transferencias #costo
            cta_ahorro_pesos.saldo_descubierto_disponible #descubierto

            cta_ahorro_dolar=clienteBlack.cuenta_ahorro_dolares(t.monto)
            cta_ahorro_dolar.limite_extraccion_diario #Costo de transferencia
            cta_ahorro_dolar.limite_transferencia_recibida #limite de transferencia recibida
            cta_ahorro_dolar.monto #monto
            cta_ahorro_dolar.costo_transferencias #costo
            cta_ahorro_dolar.saldo_descubierto_disponible #descubierto

            cta_corriente=clienteBlack.cuenta_corriente(t.monto)
            cta_corriente.limite_extraccion_diario #Costo de transferencia
            cta_corriente.limite_transferencia_recibida #limite de transferencia recibida
            cta_corriente.monto #monto
            cta_corriente.costo_transferencias #costo
            cta_corriente.saldo_descubierto_disponible #descubierto
            pass
        #max extraccion 100 000 por dia
        pass

try:
    if evento.estado.lower() == "aceptada":
        pass #hay que poner que directamente lo imprima
    else:   #es rechazada --> hay que poner porque
        assert ()
except:
    pass
    # assert nombre:
    #     lo que tiene que 
    
