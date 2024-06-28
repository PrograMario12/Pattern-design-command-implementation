'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 '''

from .command import Command

def anagrama(command):
    class AnagramaCommand(Command):
        def execute(self):
            word1 = input("Ingrese la primera palabra: ")
            word2 = input("Ingrese la segunda palabra: ")
            print(f"Las palabras {word1} y {word2} son anagramas: {areAnagrams(word1, word2)}")

    def areAnagrams(word1, word2):
        if len(word1) != len(word2):
            return False

        for letter in word1:
            if word1.count(letter) != word2.count(letter):
                return False

        return True

    return AnagramaCommand()