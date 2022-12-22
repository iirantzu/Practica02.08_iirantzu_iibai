#Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre
#tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

n = int(input("Introduzca un número entero entre 1 y 10:\n"))
nombre_archivo = "Tabla-" + str(n) + ".txt"
tabla = open(nombre_archivo, "w")
for i in range(1, 11):
   tabla.write(str(n) + " x " + str(i) + " = " + str(n * i) + "\n")
tabla.close()
