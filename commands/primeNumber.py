''' /**
* * Write a program that checks whether a number is prime or not.
* * Once this is done, print the prime numbers between 1 and 100.
*/ '''

from .command import Command

class PrimeNumberCommand(Command):
    def execute(self):
        """
        Main function that executes the PrimeNumber command.
        """
        for i in range(1, 101):
            if self.is_prime(i):
                print(i)

    def is_prime(self, num):
        """
        Function that returns True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    def get_display_name(self):
        return "Prime Number"
    
    