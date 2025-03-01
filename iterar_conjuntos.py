#iterar sobre un conjunto
conjunto = {1,2,3,4,5}
for elemento in conjunto:
    print(elemento)
    
#iterar sobre un diccionario
diccionario = {
    "nombre": "Juan",
    "apellido": "Perez",    
    "edad": 25,
    "subs": 1000000
}
for clave, valor in diccionario.items(): #items() devuelve una lista con tuplas de clave y valor
    print(clave, valor)
    
#iterar sobre una tupla
tupla = (1,2,3,4,5)
for elemento in tupla:
    print(elemento)
    
#iterar sobre una lista
lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)
    
#iterar con continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
#iterar con break
for i in range(10):
    if i == 5:
        break
    print(i)
    
#iterar una cadena
cadena = "Hola mundo"
for letra in cadena:
    print(letra)
    
#multiplicar los elementos de una lista por 2
numeros = [x*2 for x in range(10)]
print(numeros)
