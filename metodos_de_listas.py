#list crea una lista a partir de un objeto iterable
lista = list(range(10))
print(lista)
print("***************** list range(10)")

#len retorna la longitud de la lista
print(len(lista))
print("***************** len")

#append agrega un elemento al final de la lista
lista.append(10)
print(lista)
print("***************** append 10")

#insert agrega un elemento en la posicion especificada
lista.insert(0, 0)
print(lista)
print("***************** insert 0")


#extend agrega los elementos de una lista a otra
lista.extend([11, 12, 13])
print(lista)
print("***************** extend 11, 12, 13")

#pop elimina el elemento en la posicion especificada
lista.pop(0)
lista.pop(-1)
print(lista)
print("***************** pop 0")

#remove elimina la primera ocurrencia de un elemento
lista.remove(12)
print(lista)
print("***************** remove 13")

#sort ordena la lista
lista.sort()
print(lista)
print("***************** sort")

#reverse invierte la lista
lista.reverse()
print(lista)
print("***************** reverse")

#clear elimina todos los elementos de la lista
lista.clear()
print(lista)
print("***************** clear")

#dir muestra los metodos de la lista
resultado = dir(lista)
print(resultado)
print("***************** dir")

