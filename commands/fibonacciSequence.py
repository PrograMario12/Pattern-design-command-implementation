'''
Write a program that prints the first 50 numbers of the Fibonacci sequence starting at 0.
The Fibonacci series is composed of a sequence of numbers where the next number is always the sum of the two previous numbers.
0, 1, 1, 2, 3, 5, 8, 13... 
'''
from .command import Command

class FibonacciSequenceCommand(Command):
    def execute(self):
        """
        Main function that executes the FibonacciSequence command.
        """
        a, b = 0, 1
        for _ in range(50):
            print(a)
            a, b = b, a + b
            
    def get_display_name(self):
        return "Fibonacci Sequence"