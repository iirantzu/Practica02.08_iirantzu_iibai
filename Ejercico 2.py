#Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla
#de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla. Si el
#fichero no existe debe mostrar un mensaje por pantalla informando de ello.

n = int(input("Introduzca un número entero entre 1 y 10:\n"))
nombre_archivo = "Tabla-" + str(n) + ".txt"
try:
   tabla = open(nombre_archivo, 'r')
except FileNotFoundError:
   print("No hay un fichero con la tabla del", n)
else:
   print(tabla.read())