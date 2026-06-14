# Básico
archivo = open("texto.txt", "w")
archivo.write("Hola")
archivo.close()

# Intermedio
archivo = open("texto.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
