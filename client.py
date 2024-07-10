from commands.fizzBuzz import FizzBuzzCommand
from commands.anagrama import AnagramaCommand
from commands.fibonacciSequence import FibonacciSequenceCommand
from commands.primeNumber import PrimeNumberCommand
from commands.polygonArea import PolygonAreaCommand
from menu.menu import Menu

def main():
    """
    Main function that executes the commands in the menu.
    """
    commands = [FizzBuzzCommand(), AnagramaCommand(), FibonacciSequenceCommand(), PrimeNumberCommand(), PolygonAreaCommand()]

    menu = Menu(commands)

    # Display the options
    menu.showOptions()
    
    # Prompt the user for input
    opcion = int(input("Seleccione una opción: "))
    
    # Execute the selected option
    menu.ejecutar_opcion(opcion)

if __name__ == '__main__':
    main()