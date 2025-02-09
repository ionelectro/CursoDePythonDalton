""" a = 5
b = 10

c = a + b
print(c) """

nombre = "Hugo"
nombre = "Paco"
print(nombre)

numero = 5
numero-= 3
print(numero)


nombre = 8
#concatenacion con f string
bienvenido = f"Bienvenido {nombre}"
print(bienvenido)

#operadores de pertenencia in y not in
print(bienvenido in "Bienvenido 8")
print("pedro" not in bienvenido)

#en python es recomendable snake_case
#para variables

#datos compuestos
lista = [1,2,3,4,5]#lista es mutable
print(lista)
#accceso a uno de los elementos
print(lista[0])
lista[0] = 10
print(lista)

tupla = (1,2,3,4,5)#tupla es inmutable
print(tupla)
#accceso a uno de los elementos
print(tupla[0])

objeto = {1,2,3,4,5}#cada elemento es unico se puede cambiar de lugar
print(objeto)
#accceso a un elemento de objeto
""" for elemento in objeto:
    print(elemento) """

lista_set = list(objeto)
print(lista_set[3])

#diccionarios la estructura es key : value
diccionario = {"clave1": "valor1", "clave2": "valor2"}
print(diccionario["clave1"])

#Operadores Aritmeticos + - * / % // ** 

#suma y resta 
a = 5
b = 10
c = a + b
print(c)

#multiplicacion y division
a = 5
b = 10
c = a * b
print(c)

#modulo y division  %
a = 5
b = 10
c = a % b
print(c)#c = 5

#division 
a = 5
b = 10
c = a / b
print(c)#c = 0

#division entera //
a = 5
b = 10
c = a // b
print(c)#c = 0

#potencia **
a = 5
b = 10
c = a ** b
print(c)

#operadores de comparacion == != > < >= <=

a = 5
b = 10
c = 5

d = "hola"
e = "hola"

print(a == c)
print(a != c)
print(a > c)
print(a < c)
print(a >= c)
print(a <= c)

print(d == e)
print(d != e)
print(d > e)
print(d < e)
print(d >= e)
print(d <= e)

#condicionales if elif else

a = 5
b = 10
c = 5

if a == c:
    print("a y c son iguales")
elif a > c:
    print("a es mayor que c")
    
    
#if elif
ingreso_mensual = 5000

if ingreso_mensual > 10000:
    print("Estas bien economicamente")
elif ingreso_mensual > 1000:
    print("Estas regular economicamente")
else:
    print("Estas mal economicamente")
    
#if anidados
ingreso_mensual = 500000
gastos = 300

if ingreso_mensual > 10000:
    if gastos < 1000:
        print("Estas bien economicamente y ahhorrando")
    else:
        print("Estas regular economicamente")
elif ingreso_mensual > 1000:
    print("Estas regular economicamente")
else:
    print("Estas mal economicamente")


#operadores logicos and or not
#and si todas las condiciones son verdaderas
#or si alguna de las condiciones es verdadera
#not si la condicion es falsa

a = 5
b = 10
c = 5

if a == c and a == b:
    print("a y c son iguales y a y b son iguales")
elif a == c and a == b:
    print("a y c son iguales y a y b son iguales")
else:
    print("a y c no son iguales y a y b no son iguales")
    
if a == c or a == b:
    print("a y c son iguales o a y b son iguales")
elif a == c or a == b:
    print("a y c son iguales o a y b son iguales")
else:
    print("a y c no son iguales o a y b no son iguales")
    
if not a == c:
    print("a y c no son iguales")
elif not a == b:
    print("a y b no son iguales")
else:
    print("a y c son iguales y a y b son iguales")
    
#and & or | not !
g = 46
h = 45
z = 87

if g == 46 & h == 45:
    print("g y h son iguales")
elif g == 46 | h == 45:
    print("g y h son iguales")
else:
    print("g y h no son iguales")
    
if not z == 87:
    print("z no es igual a 87")
else:
    print("z es igual a 87")
    
print("**********")

    
#bucles for y while
#bucle for
for i in range(5):
    print(i)
    
print("**********")
    
for i in range(5,10):
    print(i)

print("**********")
    
for i in range(5,10,2):
    print(i)
    
print("**********")

#bucle while
i = 0
while i < 5:
    print(i)
    i+=1



