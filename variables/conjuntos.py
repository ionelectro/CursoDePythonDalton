#Creando un conjunto con set()

conjunto = set(["Carlos","Aguilar",1000])

print(conjunto) # {'Carlos', 1000, 'Aguilar'}

#Metiendo un conjunto dentro de otro conjunto
conjunto2 =frozenset({"dato1", "dato2", "dato3"})
conjunto3 = ({"Ramon","Asturias",conjunto2})

print(conjunto3) # {'Ramon', 'Asturias', frozenset({'dato1', 'dato2', 'dato3'})}

#Teoria de conjuntos
#Los conjuntos son colecciones de elementos desordenados, sin elementos duplicados.
#Los conjuntos son mutables, lo que significa que pueden cambiar su contenido una vez creados.
#Los conjuntos no tienen un orden, por lo que no se puede acceder a los elementos mediante índices.
#Los elementos de un conjunto deben ser inmutables.
#Los conjuntos no pueden tener elementos duplicados.
#Los conjuntos son iterables.
#Los conjuntos no tienen un método de indexación.

conjunto4 = { 1,3,5,7}
conjunto5 = { 1,3,7}

#Verificar si un conjunto es subconjunto de otro
resultado = conjunto4.issubset(conjunto5)
resultado2 = conjunto5.issubset(conjunto4)
resultado3 = conjunto5<=conjunto4
print(resultado2) # True
print(resultado) # False
print(resultado3) # True

#Verificar si un conjunto es superconjunto de otro
resultado4 = conjunto4.issuperset(conjunto5)
resultado5 = conjunto5.issuperset(conjunto4)
resultado6 = conjunto5<=conjunto4
print(resultado4) # True
print(resultado5) # False
print(resultado6) # True

#Verificar si hay un numero en comun entre dos conjuntos
resultado7 = conjunto4.isdisjoint(conjunto5)
print(resultado7) # False

