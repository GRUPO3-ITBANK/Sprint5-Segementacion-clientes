import sys
sys.path.append(r'.\proyecto')
from evento.evento import Evento
from razon_compra_dolar import RazonCompraDolar
from razon_transferencia_enviada import RazonTransferenciaEnviada
from razon_transferencia_recibida import RazonTransferenciaRecibida
from razon_retiro_efectivo import RazonRetiroEfectivo
from razon_alta_tarjeta_credito import RazonAltaTarjetaCredito
from razon_alta_chequera import RazonAltaChequera

def Procesar():

    # se importa los clientes con sus transacciones - mediante arg, pasar el json
    evento = Evento()
    evento.load_from_json("proyecto/archivos_json/eventos_classic.json")
    #si todo okay - implementar logica de validacion
    for t in evento.transacciones:
        if t.estado == "RECHAZADA":
            match t.tipo.lower():
                case 'transferencia_enviada':
                    return RazonTransferenciaEnviada(t,evento).resolver() 
                case 'transferencia_recibida':
                    return RazonTransferenciaRecibida(t,evento).resolver()
                case 'alta_tarjeta_credito':
                    print(RazonAltaTarjetaCredito(t,evento).resolver())
                case 'alta_chequera':
                    print(RazonAltaChequera(t,evento).resolver())
                case 'compra_dolar':
                    print(RazonCompraDolar(t,evento).resolver())
                case'retiro_efectivo_cajero_automatico':
                    print(RazonRetiroEfectivo(t,evento).resolver())

print(Procesar())