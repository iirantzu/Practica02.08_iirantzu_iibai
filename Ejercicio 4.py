#Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla
#el número de palabras que contiene.

def archivo(url):
   '''Función que recibe la url de un fichero de texto y devuelve el númerode palabras que contiene.
   Parámetros:
   url: Es una cadena con la url del fichero de texto.
   Salida:
   El número de palabras que contiene el fichero de texto daro por la url.
   '''
   from urllib import request
   from urllib.error import URLError
   try:
       fila = request.urlopen(url)
   except URLError:
       return("La url " + url + " no existe")
   else:
       content = fila.read()
       return len(content.split())
print(archivo(""))
print(archivo(""))
