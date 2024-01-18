import random

def jugar_ruleta(apresupuesto, clear_terminal):
    while True:
        clear_terminal()
        print("¡Bienvenido a la Ruleta!")
        print(f"Tienes ${presupuesto} de crédito.")
        opcion = input("Presiona Enter para jugar o escribe 'exit' para volver al menú principal: ").lower()
        if opcion == "exit":
            break
    clear_terminal()