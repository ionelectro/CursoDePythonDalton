#creando diccionarios con dict()
diccionario = dict({"nombre":"Carlos","edad":20,"carrera":"Ingenieria en Sistemas"})
print(diccionario)

#las listas no pueden ser claves de un diccionario y usamos frozenset() para meter conjuntos
diccionario = dict({frozenset([1,2,3]):"Hola"})
print(diccionario)

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","edad","carrera"])
print(diccionario)

#creando diccionarios con fromkeys() y valores por defecto
diccionario = dict.fromkeys(["nombre","edad","carrera"],"valor por defecto")
print(diccionario)

#creando diccionarios con zip()
diccionario = dict(zip(["nombre","edad","carrera"],["Carlos",20,"Ingenieria en Sistemas"]))
print(diccionario)