import random

def jugar():
    numero_secreto = random.randint(0, 50)
    intentos = 6
    adivinado = False

    print("¡Bienvenido al juego de adivinar el número!")
    print(f"Tienes {intentos} oportunidades para adivinar un número entre 0 y 50.")

    for intento in range(1, intentos + 1):
        try:
            suposicion = int(input(f"Intento {intento}: Ingresa tu suposición: "))

            if suposicion < 0 or suposicion > 50:
                print("Por favor, ingresa un número entre 0 y 50.")
                continue

            if suposicion == numero_secreto:
                print("¡Felicidades! ¡Adivinaste el número!")
                adivinado = True
                break
            elif suposicion < numero_secreto:
                print("El número es mayor.")
            else:
                print("El número es menor.")
        except ValueError as e:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    if not adivinado:
        print(f"Lo siento, has agotado tus intentos. El número era {numero_secreto}.")

    return adivinado

def main():
    while True:
        ganar = jugar()

        if not ganar:
            respuesta = input("¿Quieres intentarlo de nuevo? (s/n): ").lower()
            if respuesta != 's':
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
        else:
            respuesta = input("¡Felicidades! ¿Quieres jugar de nuevo? (s/n): ").lower()
            if respuesta != 's':
                print("Gracias por jugar. ¡Hasta la próxima!")
                break

if __name__ == "__main__":
    main()