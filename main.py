import os
import random
from blackjack import jugar_blackjack
from tragaperras import jugar_tragaperras
from ruleta import jugar_ruleta
from dados import jugar_dados

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_bienvenida():
    print("¡Bienvenido al Casino Virtual!")
    print("Tienes $1000 de presupuesto.")

def ver_presupuesto(presupuesto):
    clear_terminal()
    if presupuesto == 0:
        print("Favor de recargar crédito. Tu presupuesto se ha agotado.")
    else:
        print(f"Tienes ${presupuesto} de presupuesto.")

def main():
    presupuesto = 1000

    mostrar_bienvenida()

    while True:
        ver_presupuesto(presupuesto)
        print("\nMenú:")
        print("1. Juego de Blackjack")
        print("2. Juego de Tragaperras")
        print("3. Juego de Ruleta Americana")
        print("4. Juego de Dados")
        print("5. Ver mi presupuesto")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")
        clear_terminal()

        if opcion == "1":
            presupuesto = jugar_blackjack(presupuesto, clear_terminal)
        elif opcion == "2":
            presupuesto = jugar_tragaperras(presupuesto, clear_terminal)
        elif opcion == "3":
            jugar_ruleta(presupuesto, clear_terminal)
        elif opcion == "4":
            jugar_dados(presupuesto, clear_terminal)
        elif opcion == "5":
            ver_presupuesto(presupuesto, clear_terminal)
        elif opcion == "6":
            print("¡Gracias por jugar, siempre juega responsablemente! Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
