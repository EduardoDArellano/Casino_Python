import random

def jugar_blackjack(presupuesto, clear_terminal):
    while True:
        clear_terminal()
        print("¡Bienvenido al Blackjack!")
        print(f"Tienes ${presupuesto} de presupuesto.")
        
        # Verificar el presupuesto mínimo antes de preguntar por la apuesta
        if presupuesto < 100:
            print("Lo siento, tu presupuesto es insuficiente para jugar al Blackjack.")
            input("Presiona Enter para volver al menú principal...")
            break
        
        # Preguntar por el valor de la apuesta
        while True:
            try:
                apuesta = int(input(f"Ingresa tu apuesta (entre 100 y 500): "))
                if 100 <= apuesta <= 500 and apuesta <= presupuesto:
                    break
                else:
                    print("Ingresa una apuesta válida dentro del rango permitido.")
            except ValueError:
                print("Ingresa un valor numérico.")
                
        opcion = input("Presiona Enter para jugar o escribe 'exit' para volver al menú principal: ").lower()
        if opcion == "exit":
            break
        
        # Baraja de cartas
        palos = ['♡', '◇', '♧', '♤']
        numeros = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        cartas = [(numero, palo) for numero in numeros for palo in palos]

        # Mano del jugador y del crupier
        mano_jugador = []
        mano_crupier = []

        # Función para calcular el valor de la mano
        def calcular_valor(mano):
            valor = 0
            ases = 0

            for carta in mano:
                if carta[0].isdigit():
                    valor += int(carta[0])
                elif carta[0] in ['J', 'Q', 'K']:
                    valor += 10
                elif carta[0] == 'A':
                    valor += 11
                    ases += 1

            # Ajustar el valor si hay ases y el valor es mayor a 21
            while ases > 0 and valor > 21:
                valor -= 10
                ases -= 1

            return valor

        # Función para mostrar las cartas
        def mostrar_cartas(mano, ocultar_crupier=False, crupier=False):
            print("==============================")
            if crupier:
                print("Mano crupier:")
            else:
                print("Tu mano:")
            for i, carta in enumerate(mano):
                if i == 0 and ocultar_crupier:
                    print("||???", end="|| ")
                else:
                    print(f"||{carta[0]} de {carta[1]}", end="|| ")

            valor_mano = calcular_valor(mano)
            if ocultar_crupier == False :
                print(f"\n===> {valor_mano}")    
            
        # Función para manejar la jugada del jugador
        def turno_jugador():
            nonlocal presupuesto

            while True:
                if len(mano_jugador) > 2:
                    mostrar_cartas(mano_jugador)
                    mostrar_cartas(mano_crupier, ocultar_crupier=True, crupier=True)
                print("\n==============================")
                print()
                print("¿Qué quieres hacer?")
                print("1. Pedir carta")
                print("2. Plantarte")
                print("3. Salir")

                opcion = input("Selecciona una opción (1-3): ")

                if opcion == "1":
                    carta_nueva = random.choice(cartas)
                    mano_jugador.append(carta_nueva)
                    print()
                    print("==============================")
                    print(f"Has recibido un/a ||{carta_nueva[0]} de {carta_nueva[1]}||")
                    
                    if calcular_valor(mano_jugador) > 21:
                        print("Te has pasado de 21. ¡Perdiste!")
                        presupuesto -= 50  # Puedes ajustar la cantidad según tu lógica de apuestas
                        input("Presiona Enter para continuar...")
                        return
                elif opcion == "2":
                    break
                elif opcion == "3":
                    return

        # Función para manejar el turno del crupier
        def turno_crupier():
            while calcular_valor(mano_crupier) < 17:
                carta_nueva = random.choice(cartas)
                mano_crupier.append(carta_nueva)

        # Inicializar el juego
        mano_jugador = [random.choice(cartas), random.choice(cartas)]
        mano_crupier = [random.choice(cartas), random.choice(cartas)]

        # Mostrar las cartas iniciales
        mostrar_cartas(mano_jugador)
        mostrar_cartas(mano_crupier, ocultar_crupier=True, crupier=True)

        # Turno del jugador
        turno_jugador()

        # Si el jugador no se pasó de 21, turno del crupier
        if calcular_valor(mano_jugador) <= 21:
            turno_crupier()
            clear_terminal()
            mostrar_cartas(mano_jugador)
            mostrar_cartas(mano_crupier, ocultar_crupier=False, crupier=True)

            # Determinar el ganador
            if calcular_valor(mano_crupier) > 21 or calcular_valor(mano_jugador) > calcular_valor(mano_crupier):
                presupuesto += apuesta  # Puedes ajustar la cantidad según tu lógica de apuestas
                print(f"¡Felicidades! Ganaste. Tu nuevo presupuesto es de {presupuesto}")
            elif calcular_valor(mano_jugador) == calcular_valor(mano_crupier):
                print(f"Es un empate. Tu presupuesto actual es de {presupuesto}")
            else:
                presupuesto -= apuesta
                print(f"¡Perdiste!. Tu nuevo presupuesto es de {presupuesto}")

        input("Presiona Enter para continuar...")

        # Preguntar si quieren jugar de nuevo
        clear_terminal()
        if presupuesto == 0:
            print("Lo sentimos, tu presupuesto se ha agotado.")
            break

        continuar = input("¿Quieres jugar otra mano? (s/n): ").lower()
        if continuar != 's':
            break

    clear_terminal()
    return presupuesto
