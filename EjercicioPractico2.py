import time

#Pedirle al usuario que diga cualquier texto real y: calcular cuanto tardaria en decir esa frase, cuantas palabras dijo.

texto = input("Escribe cualquier texto real: ")
palabras = texto.split()
cantidadDePalabras = len(palabras)
print("Usted ha dicho ", cantidadDePalabras, " palabras")

#si tarda mas de 1 minuto en decirle: "Usted es muy lento"
tiempo = cantidadDePalabras / 2
if tiempo > 60:
    print("Usted es muy lento")
else:
    print("Usted tardaría ", tiempo, " segundos en decir esa frase")
    
#si hablara un 30% mas rapido, cuanto tardaria en decir la misma frase
tiempo = tiempo * 0.7
print("Si hablara un 30% más rápido, tardaría ", tiempo, " segundos en decir la misma frase")


