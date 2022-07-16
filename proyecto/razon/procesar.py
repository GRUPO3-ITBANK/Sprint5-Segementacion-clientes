from razon_compra_dolar import RazonCompraDolar
from razon_transferencia_enviada import RazonTransferenciaEnviada
from razon_transferencia_recibida import RazonTransferenciaRecibida
from razon_retiro_efectivo import RazonRetiroEfectivo
from razon_alta_tarjeta_credito import RazonAltaTarjetaCredito
from razon_alta_chequera import RazonAltaChequera
from cliente.tipos_clientes import Black
from cliente.cliente import Cliente
from evento.evento import Evento

evento = Evento()
evento.load_from_json('eventos_black.json')
cliente= Cliente(evento)

def Procesar():

    # se importa los clientes con sus transacciones - mediante arg, pasar el json
    evento = Evento()
    evento.load_from_json('eventos_gold.json')
    #si todo okay - implementar logica de validacion

    for t in evento.transacciones:
        if t.estado == "RECHAZADA":
            match t.tipo.lower():
                case 'transferencia_enviada':
                    return RazonTransferenciaEnviada(t,evento).resolver() #en vez de print va return para mandar los datos a una variable
                case 'transferencia_recibida':
                    return RazonTransferenciaRecibida(t,evento).resolver()
                case 'alta_tarjeta_credito':
                    print(RazonAltaTarjetaCredito(t,evento).resolver())
                case 'alta_chequera':
                    print(RazonAltaChequera(t,evento).resolver())
                case 'comprar_dolar':
                    print(RazonCompraDolar(t,evento).resolver())
                case'retiro_efectivo_cajero_automatico':
                    print(RazonRetiroEfectivo(t,evento).resolver())


print(Procesar())