archivo = open("saludo.txt", "w")
archivo.write("Hola desde Python.\n")
archivo.write("Esto es una segunda linea.")
archivo.close()

archivo = open("saludo.txt", "r")
contenido = archivo.read()
print("Contenido del archivo:")
print(contenido)
archivo.close()
