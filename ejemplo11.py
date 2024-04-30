archivo = open("datos/atp_tennis.csv", "r", encoding="utf-8")  # Especificar la codificación UTF-8 al abrir el archivo CSV

lineas = archivo.readlines()

lineas = [l.strip().split("|") for l in lineas]

archivos_generados = 0  # Variable para contar los archivos HTML generados con éxito

for i, x in enumerate(lineas, 1):
    # Verificar si hay suficientes elementos en la lista x
    if len(x) >= 17:
        # Generar la cadena HTML
        cadena = """<html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Información del Torneo</title>
            <link rel="stylesheet" type="text/css" href="estilos/estilos.css">
        </head>
        <body>
            <h1>Información del Torneo</h1>
            <p><strong>Número:</strong> %d</p>
            <p><strong>Torneo:</strong> %s</p>
            <p><strong>Fecha:</strong> %s</p>
            <p><strong>Serie:</strong> %s</p>
            <p><strong>Court:</strong> %s</p>
            <p><strong>Surface:</strong> %s</p>
            <p><strong>Ronda:</strong> %s</p>
            <p><strong>Best of:</strong> %s</p>
            <p><strong>Jugador 1:</strong> %s</p>
            <p><strong>Jugador 2:</strong> %s</p>
            <p><strong>Ganador:</strong> %s</p>
            <p><strong>Rango Jugador 1:</strong> %s</p>
            <p><strong>Rango Jugador 2:</strong> %s</p>
            <p><strong>Puntos Jugador 1:</strong> %s</p>
            <p><strong>Puntos Jugador 2:</strong> %s</p>
            <p><strong>Odd Jugador 1:</strong> %s</p>
            <p><strong>Odd Jugador 2:</strong> %s</p>
            <p><strong>Resultado:</strong> %s</p>
        </body>
        </html>""" % (i, *x[:17])  # Usar solo los primeros 17 elementos de x

        # Escribir la cadena HTML en un archivo HTML
        nombre_archivo = "datos/{}.html".format(x[9])
        archivo_generado = open(nombre_archivo, "w", encoding="utf-8")  # Especificar la codificación UTF-8 al escribir en el archivo HTML
        archivo_generado.write(cadena)
        archivo_generado.close()
        
        archivos_generados += 1  # Incrementar el contador de archivos generados

        # Imprimir número, torneo y ganador por consola
        print(f"Número: {i}, Torneo: {x[9]}, Ganador: {x[0]}")
    else:
        print(f"La línea {i} no tiene suficientes columnas.")

archivo.close()

print("________________________________________________")

print(f"Se han generado {archivos_generados} archivos HTML con éxito.")

print("________________________________________________")
