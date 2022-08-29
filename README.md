Sprint 5
-----
Segmentación de clientes
--------------------
El archivo se debe ejecutar desde el Command Prompt/PowerShell/consola ingresando: python main.py. 
Luego se le va  a pedir que debe ingresar el nombre del archivo JSON, los que están disponibles son:
"eventos_black.json", "eventos_gold.json" o "eventos_classic.json".

Ejemplo de resultado:
![image](https://user-images.githubusercontent.com/29070543/187230289-7a6984b2-1933-4679-a33b-a23137e22a81.png)
-------
Consigna
--------
ITBANK tiene distintos tipos de clientes y distintos tipos de cuentas que le puede dara cada uno. A continuación se detallan las características de cada uno de ellos.
----
Tipos de clientes:
- Classic. 
- Gold. 
- Black.
----
Tipos de cuentas:
- Caja de ahorro en pesos.
- Caja de ahorro en dólares.
- Cuenta Corriente.
-----
Adicionalmente los clientes pueden tener distintos tipos de tarjetas de crédito y operaciones permitidas según su perfil asociado:
---
 Clientes Classic:

- Tiene solamente una tarjeta de débito que se crea junto con el cliente.
- Solo tiene una caja ahorro en pesos creada cuando se dio de alta el cliente. Como no tiene cuenta en dólares, no puede comprar y vender dólares.
- Solo se le permite retirar hasta un máximo de $10.000 diarios por cajero.
- No tienen acceso a tarjetas de crédito ni chequeras
- La comisión por transferencias hechas es de 1%.
- No puede recibir transferencias mayores a $150.000 sin previo aviso.
---
Clientes Gold:

- Tiene una tarjeta de débito que se crea con el cliente.
- Tiene una cuenta corriente con un descubierto de $10.000. Hay que tener presente que como tiene cuenta corriente el saldo en la cuenta podría sernegativo y hasta -$10.000 si tiene cupo diario para la operación que sequiera realizar.
- Tiene una caja de ahorro en dólares, por lo que puede comprar dólares.
- Puede tener solo una tarjeta de crédito. Las extracciones de efectivo tienen un máximo de $20.000 por día. Pueden tener una chequera.
- La comisión por transferencias hechas es de 0,5%.
- No puede recibir transferencias mayores a $500.000 sin previo aviso.
---
Clientes Black:
- Los clientes Black tienen una caja de ahorro en pesos, cuenta corriente enpesos, y una caja de ahorro en dólares. Pueden tener un descubierto en su cuenta corriente de hasta $10.000.
- Pueden tener hasta 5 tarjetas de crédito.
- Pueden extraer hasta $100.000 por día
- Pueden tener hasta dos chequeras.
- No se aplican comisiones a las transferencias.
- Pueden recibir transferencias por cualquier monto sin previa autorización.
----

Problemática
---
El banco cuenta con un sistema TPS (Sistema de Procesamiento de Transacciones) que tiene como principal función enviar las transacciones ocurridas, diferenciando si fueron aceptadas o no (sin indicar la razón). Dicho sistema tiene años de funcionamiento en el banco y fue depurado varias veces, llevando la tasa deerrores al mínimo, por lo que se sabe que funciona correctamente. El equipo de TI, identifica este sistema como un "Legacy" o "Legado". La única salida que provee el sistema, son los datos "crudos" del evento ocurrido con los montos asociados sin ningún procesamiento o información adicional. El área de operaciones del banco está integrada por gente de mucha experiencia en el banco que utiliza planillas propias para poder procesar la salida de datos del TPS. Dado que actualmente ITBANK se encuentra en un proceso de renovación, se están incorporando nuevos empleados al área de referencia. Es por ese motivo que el gerente requiere una automatización del procesamiento de los datos emitidos por el TPS. La mejor forma de abordar este problema es generar una aplicación que reciba como input la información del TPS, la procese y emita un reporte que
sea capaz de mostrar la razón de porque estas transacciones fueron rechazadas para ponerla a disposición del equipo de atención al cliente. Si son aceptadas simplemente se agrega al reporte la transacción que se hizo sin detalle particular, de esta forma quedara completo el informe. En el reporte se debe incluir el nombre de cliente, número, DNI, dirección y para cada transacción la fecha, el tipo de operación, el estado, el monto y razón por la cual se rechazó (vacío en caso de ser aceptada). Se pide que el reporte sea una página en HTML válida de forma que el browser estándar del banco lo pueda interpretar y visualizar. La salida del sistema TPS es un archivo JSON con las transacciones que debemos procesar.
