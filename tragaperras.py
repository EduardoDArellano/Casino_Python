import random
import time

def girar_rodillo():
    rodillos = ["cherry", "lemon", "orange", "plum", "bell", "bar", "seven"]
    return random.choice(rodillos)

def mostrar_rodillos(clear_terminal, rodillos):
    num_filas = len(rodillos[0])  # Número de filas en los rodillos

    for i in range(num_filas):
        clear_terminal()
        for j, rodillo in enumerate(rodillos):
            print("|", end="")
            for k, simbolo in enumerate(rodillo):
                if k == i:  # Muestra el símbolo actual del rodillo
                    print(f" {simbolo} |", end="")
                else:  # Muestra un espacio en blanco si no es el símbolo actual
                    print("  |", end="")
            if j < len(rodillos) - 1:
                print("\t", end="")
                time.sleep(1)  # Pausa de 1 segundo entre cada rodillo
        print()
        time.sleep(1)  # Pausa adicional de 1 segundo entre cada fila

def jugar_tragaperras(presupuesto, clear_terminal):
    while True:
        clear_terminal()
        print("¡Bienvenido al juego Tragaperras!")
        print(f"Tienes ${presupuesto} de presupuesto.")
        
        # Verificar el presupuesto mínimo antes de permitir jugar
        if presupuesto < 10:
            print("Lo siento, tu presupuesto es insuficiente para jugar a la Tragaperras.")
            input("Presiona Enter para volver al menú principal...")
            break

        # Preguntar por la apuesta
        while True:
            try:
                apuesta = int(input("Ingresa tu apuesta (mínimo $10): "))
                if 10 <= apuesta <= presupuesto:
                    break
                else:
                    print("Ingresa una apuesta válida dentro del rango permitido.")
            except ValueError:
                print("Ingresa un valor numérico.")

        # Restar la apuesta al presupuesto
        presupuesto -= apuesta

        # Girar los rodillos
        rodillo1 = girar_rodillo()
        rodillo2 = girar_rodillo()
        rodillo3 = girar_rodillo()

        # Mostrar el giro de los rodillos
        mostrar_rodillos(clear_terminal,[[rodillo1], [rodillo2], [rodillo3]])

        # Evaluar el resultado y ajustar el presupuesto
        if rodillo1 == rodillo2 == rodillo3:
            # Premio mayor
            premio = apuesta * 10
            print("¡Felicidades! Has ganado el premio mayor.")
        elif rodillo1 == rodillo2 or rodillo1 == rodillo3 or rodillo2 == rodillo3:
            # Premio por coincidencia en dos rodillos
            premio = apuesta * 5
            print("¡Bien hecho! Has ganado un premio.")
        else:
            # No hubo coincidencias
            premio = 0
            print("Lo siento, no hubo coincidencias. Inténtalo de nuevo.")

        # Actualizar el presupuesto
        presupuesto += premio

        # Mostrar el resultado y el presupuesto actual
        print(f"\n¡Resultado: {rodillo1}, {rodillo2}, {rodillo3}!")
        print(f"\nTu premio: ${premio}")
        print(f"\nPresupuesto actual: ${presupuesto}")

        # Preguntar si quieren jugar de nuevo
        continuar = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if continuar != 's':
            break

    clear_terminal()
    return presupuesto

# Ejemplo de uso:
# presupuesto = jugar_tragaperras(500, clear_terminal)
