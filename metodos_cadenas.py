#metodos cadenas
cadena1 = "hola soy hugo"
cadena2 = "Bienvenidos a mi curso de python"

#dir(cadena1)
resultado = dir(cadena1)

#Upper
cadena2.upper()
print(cadena2.upper())

#Lower
cadena2.lower()
print(cadena2.lower())

#capitalize retorna la cadena con la primera letra en mayuscula
cadena2.capitalize()
print(cadena2.capitalize())

#title retorna la cadena con la primera letra de cada palabra en mayuscula
cadena2.title()
print(cadena2.title())

#find retorna la posicion de la primera ocurrencia de la cadena
cadena2.find("curso")
print(cadena2.find("curso"))

#index retorna la posicion de la primera ocurrencia de la cadena,si no la encuentra retorna un error
cadena2.index("curso")
print(cadena2.index("python"))

#isnumeric retorna true si la cadena es numericamente
cadena2.isnumeric()
print(cadena2.isnumeric())

#isalpha retorna true si la cadena es alfanumerica
cadena2.isalpha()
print(cadena2.isalpha())

#count retorna el numero de veces que se repite una cadena
cadena2.count("curso")
print(cadena2.count("curso"))

#len retorna la longitud de la cadena
len(cadena2)
print(len(cadena2))

#replace remplaza una cadena por otra
cadena2.replace("curso", "clase")
print(cadena2.replace("curso", "clase"))

#endswith retorna true si la cadena termina con la cadena especificada
cadena2.endswith("python")
print(cadena2.endswith("python"))

#startswith retorna true si la cadena empieza con la cadena especificada
cadena2.startswith("Bienvenidos")
print(cadena2.startswith("Bienvenidos"))

#split divide la cadena en subcadenas y retorna una lista
cadena2.split(" ")
print(cadena2.split(" "))

