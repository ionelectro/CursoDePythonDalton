#pedir un dato al usuario
""" nombre = input("Ingrese su nombre: ")
print(f"Su nombre es {nombre}") """

#pedir un numero al usuario
numero = int(input("Ingrese un numero: "))
print(f"El numero es {numero}")

#pedir otro numero al usuario
numero2 = float(input("Ingrese otro numero: "))
print(f"El numero es {numero2}")

#pedir al usuario si quiere sumar o restar
operacion = input("Desea sumar o restar: ")
print(f"La operacion es {operacion}")

#segun la operacion ingresada por el usuario, se realiza la suma o resta
if operacion == "sumar":
    resultado = numero + numero2
    print(f"El resultado de la suma es {resultado}")
else:
    resultado = numero - numero2
    print(f"El resultado de la resta es {resultado}")
    
