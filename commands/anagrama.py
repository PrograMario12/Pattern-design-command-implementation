'''
 * Write a function that receives two words (String) and returns
 * true or false (Bool) depending on whether they are anagrams or not.
 * - An anagram consists of forming a word by rearranging ALL
 *   the letters of another initial word.
 * - It is not necessary to check if both words exist.
 * - Two exactly identical words are not anagrams.
 '''

from .command import Command

class AnagramaCommand(Command):
    def execute(self):
        """
        Main function that executes the Anagrama command.
        """
        palabra1 = input("Ingrese la primera palabra: ")
        palabra2 = input("Ingrese la segunda palabra: ")

        if self.is_anagrama(palabra1, palabra2):
            print(f"{palabra1} y {palabra2} son anagramas.")
        else:
            print(f"{palabra1} y {palabra2} no son anagramas.")

    def is_anagrama(self, palabra1, palabra2):
        """
        Function that returns True if the two words are anagrams, False otherwise.
        """
        return sorted(palabra1) == sorted(palabra2)
    
    def get_display_name(self):
        return "Anagrama"