
archivo = open("Data/atp_tennis.csv", "r")

lineas = archivo.readlines()

lineas = [l.split("|") for l in lineas]

for x in lineas:
    torneo = x[0]
    ganador = x[9]
    
    # Generar la cadena HTML
    cadena = """<b> Torneo: </b> {} <br><br><b> Ganador: </b> {}""".format(torneo, ganador)
    
    print(cadena)  # Imprimir la cadena HTML
    
    # Escribir la cadena HTML en un archivo HTML
    nombre_archivo = "Data/{}.html".format(ganador)
    archivo_generado = open(nombre_archivo, "w")
    archivo_generado.write(cadena)
    archivo_generado.close()

archivo.close()
