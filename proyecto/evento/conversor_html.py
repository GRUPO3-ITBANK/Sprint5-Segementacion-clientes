def CreadorHTML(cliente,resultados):

    html=f"""
    <html>
     <head>
        <title class=>Listado de transacciones</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="./estilo/bootstrap.min.css" rel="stylesheet">
        <link href="./estilo/main.css" rel="stylesheet">
      </head>
        <body class="bg">
            <header class="col-auto bg-dark text-light">
            <h1 class="text-center"><b>Lista de transacciones</b></h1>
            <div><b>Nombre y apellido:</b> {cliente.nombre}, {cliente.apellido}</div>
            <div><b>ID de cliente:</b> {cliente.numero}</div>
            <div><b>DNI:</b> {cliente.dni}</div>
            <div><b>Dirección:</b> {cliente.direccion}</div>
        </header>
            <table class="mt-4 m-sm-auto">"""
    for r in resultados:
            html += f"""
              <tr class="card p-2 m-3 rounded shadow">
                <td><b>Tipo:</b> {r.tipo}</td>
                <td><b>Estado:</b> {r.estado}</td>
                <td><b>Monto:</b> ${r.monto}</td>"""
            if r.razon != "":
                html += f"<td><b>Razon:</b> {r.razon}</td>"
            else:
                html += "<td></td>"
            html += "</tr>"
    html += """</table>
        </body> 
    <html>"""

    archivoHTML=open("index.html","w", encoding="utf-8")
    archivoHTML.write(html)
    archivoHTML.close()

