#Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países
#de la Unión Europea
#( https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true ),
#pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.

def obtener_pib(url, pais="ES"):
    '''
    Función que muestra por pantalla el pib per cápita un país dado de los años disponibles en un fichero dado.
    Parámetros:
        url: Es una cadena con la url del fichero de texto que contiene el pib per cápita.
        country: Es una cadena con el código del país.
    Salida:
        Un diccionario con pares año:pib del país que hay en el fichero con la url dada.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        tabla = request.urlopen(url)
    except URLError:
        return ("La url " + url + " no existe")
    else:
        datos = tabla.read().decode("utf-8").split("\n")
        datos = [i.split("\t") for i in datos]
        datos = [list(map(str.strip, i)) for i in datos]
        for i in datos:
            i[0] = i[0].split(",")[-1]
        datos[0][0] = "años"
        datos = {i[0]: i[1:] for i in datos}
        resultado = {datos["años"][i]: datos[pais][i] for i in range(len(datos["años"]))}
        return resultado


pais = input("Introduzca el código de un país:\n")
print("Producto interior bruto por cápital de", pais)
print("Año", "\t", "PIB")
for anno, pib in obtener_pib(
        "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true").items():
