# from commands.ejercicio1_command import Ejercicio1Command
# from commands.ejercicio2_command import Ejercicio2Command
from commands.fizzBuzz import FizzBuzzCommand
from menu.menu import Menu

def main():
    """
    Main function that executes the commands in the menu.
    """
    commands = [FizzBuzzCommand()]

    menu = Menu(commands)
    menu.ejecutar_opcion(0) # Ejecuta Ejercicio 1

if __name__ == '__main__':
    main()
