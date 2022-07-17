import sys
sys.path.append(r'./proyecto')
from evento.evento import Evento
from evento.transacciones import TransaccionesDetalle
from cliente.cliente import Cliente
from evento.conversor_html import CreadorHTML
from .razon_compra_dolar import RazonCompraDolar
from .razon_transferencia_enviada import RazonTransferenciaEnviada
from .razon_transferencia_recibida import RazonTransferenciaRecibida
from .razon_retiro_efectivo import RazonRetiroEfectivo
from .razon_alta_tarjeta_credito import RazonAltaTarjetaCredito
from .razon_alta_chequera import RazonAltaChequera

def obtenerRazon(t,evento):
    if t.estado == "RECHAZADA":
        match t.tipo.lower():
            case 'transferencia_enviada':
                return RazonTransferenciaEnviada(t,evento).resolver() 
            case 'transferencia_recibida':
                return RazonTransferenciaRecibida(t,evento).resolver()
            case 'alta_tarjeta_credito':
                return RazonAltaTarjetaCredito(t,evento).resolver()
            case 'alta_chequera':
                return RazonAltaChequera(t,evento).resolver()
            case 'compra_dolar':
                return RazonCompraDolar(t,evento).resolver()
            case'retiro_efectivo_cajero_automatico':
                return RazonRetiroEfectivo(t,evento).resolver()
    else:
        return ""

def Procesar(archivoJSON):
    evento = Evento()
    evento.load_from_json(f"archivos_json/{archivoJSON}")
    cliente = Cliente(evento)
    resultados=[]
    for t in evento.transacciones:
        resultado = t
        resultado.razon = ((obtenerRazon(t,evento)))
        resultados.append(resultado)
    
    CreadorHTML(cliente, resultados)

