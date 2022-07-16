from razon_transferencia_enviada import RazonTransferenciaEnviada
from razon_transferencia_recibida import RazonTransferenciaRecibida
from razon_retiro_efectivo import RazonRetiroEfectivo
from razon_alta_tarjeta_credito import RazonAltaTarjetaCredito
from razon_alta_chequera import RazonAltaChequera
from cliente import Cliente
from evento import Evento
# se importa los clientes con sus transacciones - mediante arg, pasar el json
evento = Evento()
evento.load_from_json('eventos_classic.json')
cliente= Cliente(evento)
#si todo okay - implementar logica de validacion


for t in evento.transacciones:
    if t.estado == "RECHAZADA":
        match t.tipo.lower():
            case 'transferencia_enviada':
                rz= RazonTransferenciaEnviada(t,evento)
                print(rz.resolver(t,evento))
            case 'transferencia_recibida':
                rz= RazonTransferenciaRecibida(t,evento)
                print(rz.resolver(t,evento))
            case 'alta_tarjeta_credito':
                rz= RazonAltaTarjetaCredito(t,evento)
                print(rz.resolver(t,evento))
            case 'alta_chequera':
                rz= RazonAltaChequera(t,evento)
                print(rz.resolver(t,evento))
            case 'comprar_dolar':
                pass #faltó hacer este
            case'retiro_efectivo_cajero_automatico':
                rz= RazonRetiroEfectivo(t,evento)
                print(rz.resolver(t,evento))

