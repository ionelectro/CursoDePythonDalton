diccionario ={
    "nombre": "Juan",
    "apellido": "Perez",    
    "edad": 25,
    "subs": 1000000
}

print(diccionario["nombre"])

#keys devuelve una lista con las claves del diccionario
claves = diccionario.keys()
print(claves)


#get devuelve el valor de la clave que se le pase
nombre = diccionario.get("nombre")
print(nombre)

#items devuelve una lista con tuplas de clave y valor
items = diccionario.items()
print(items)

#pop elimina un elemento del diccionario
diccionario.pop("subs")
print(diccionario)

#popitem elimina el ultimo elemento del diccionario
diccionario.popitem()
print(diccionario)

#clear elimina todos los elementos del diccionario
diccionario.clear()
print(diccionario)