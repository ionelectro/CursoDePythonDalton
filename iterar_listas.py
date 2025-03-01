animales = ["perro", "gato", "pez", "loro"]
for animal in animales:
    print(animal)
    
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numero = numero * 2
    print(numero)
    
#iterar sobre dos listas
nombres = ["Carlos","Juan","Maria"]
apellidos = ["Perez","Gomez","Lopez"]
for nombre, apellido in zip(nombres, apellidos): #zip() empareja los elementos de las listas
    print(nombre, apellido)
    
animales2 = ["leon", "tigre", "elefante", "jirafa"]
numeros2 = [1,2,3,4]
# for animal, numero in zip(animales2, numeros2):
#     print(f"El {animal} es el numero {numero}")
    
#iterar sobre una lista y un rango
# for numero, animal in zip(range(1,5), animales2):
#     print(f"El {animal} es el numero {numero}")
    
#forma de iterar con enumerate
# for indice, animal in enumerate(animales2):
#     print(f"{indice+1}. {animal}")
    
# usando el else en un for
for animal in animales2:
    print(animal)
else:
    print("Fin del ciclo for")