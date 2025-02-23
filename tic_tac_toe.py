def mostrar_tablero(tablero):
    for fila in tablero:
        print("|", end=" ")
        for casilla in fila:
            print(casilla, end=" | ")
        print("\n-------------")

def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True
    
    # Verificar columnas
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    
    return False

def tablero_lleno(tablero):
    return all(casilla != " " for fila in tablero for casilla in fila)

def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    
    print("¡Bienvenido al juego de Cruz y Raya!")
    print("Para jugar, ingresa la posición (fila,columna) del 0 al 2")
    
    while True:
        mostrar_tablero(tablero)
        print(f"Turno del jugador {jugador_actual}")
        
        try:
            fila = int(input("Ingresa la fila (0-2): "))
            columna = int(input("Ingresa la columna (0-2): "))
            
            if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                print("Posición inválida. Debe ser entre 0 y 2.")
                continue
                
            if tablero[fila][columna] != " ":
                print("Esta casilla ya está ocupada. Intenta otra vez.")
                continue
                
            tablero[fila][columna] = jugador_actual
            
            if verificar_ganador(tablero, jugador_actual):
                mostrar_tablero(tablero)
                print(f"¡Felicidades! El jugador {jugador_actual} ha ganado!")
                break
                
            if tablero_lleno(tablero):
                mostrar_tablero(tablero)
                print("¡Empate!")
                break
                
            jugador_actual = "O" if jugador_actual == "X" else "X"
            
        except ValueError:
            print("Por favor, ingresa números válidos.")
        except IndexError:
            print("Posición inválida. Debe ser entre 0 y 2.")

def main():
    while True:
        jugar()
        respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if respuesta != 's':
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()