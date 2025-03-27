#build in
#encontrando el numero mayor de una lista
numeros = [1,2,3,4,5]
mayor = max(numeros)
print(mayor)
menor = min(numeros)
print(menor)


#redondenado a 6 decimmales
numero = 3.14159265358979323846
redondeado = round(numero, 6)
print(redondeado)

#funcion bool
#la funcion bool devuelve True o False dependiendo del valor que se le pase
#si el valor es 0 o una cadena vacia devuelve False
#si el valor es diferente de 0 o una cadena no vacia devuelve True
#ejemplo
#cadena vacia
cadena_vacia = ""
print(bool(cadena_vacia)) #False

#all
#la funcion all devuelve True si todos los elementos de un iterable son True
#ejemplo
#lista de booleanos
lista_booleanos = [True, True, True]
print(all(lista_booleanos)) #True

#sum
#la funcion sum devuelve la suma de los elementos de un iterable
#ejemplo
#lista de numeros
lista_numeros = [1,2,3,4,5]
print(sum(lista_numeros)) #15