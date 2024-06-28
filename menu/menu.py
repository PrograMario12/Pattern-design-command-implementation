class Menu:
    def __init__(self, commands):
        self.commands = commands

    def ejecutar_opcion(self, opcion):
        if 0 <= opcion < len(self.commands):
            self.commands[opcion].execute()
        else:
            print("Opción no válida.")
