import math

class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

# add lots more methods to this calculator class.
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a/b

    def square(self, a):
        return a ** 2

    def square_root(self, a):
        return math.sqrt(a)

    def exponentiate(self, a, b):
        return a ** b

    def inverse(self, a):
        return 1/a

    def invert(self, a):
        return -a