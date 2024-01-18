import random

def jugar_dados(presupuesto, clear_terminal):
    while True:
        clear_terminal()
        print("¡Bienvenido al juego de Dados!")
        print(f"Tienes ${presupuesto} de crédito.")
        opcion = input("Presiona Enter para jugar o escribe 'exit' para volver al menú principal: ").lower()
        if opcion == "exit":
            break
    clear_terminal()