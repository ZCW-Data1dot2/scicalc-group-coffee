import math

class Calculator:

    def __init__(self):
        self.state = 0
        self.display_mode = "dec"
        self.memory = 0

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

    def add_to_memory(self):
        self.memory += self.state

    def reset_memory(self):
        self.memory = 0

    def recall_memory(self):
        return self.memory

    def switchDisplayMode(self, mode=None):
        if mode is None:
            if self.display_mode == "bin":
                new_display = "oct"
            elif self.display_mode == "oct":
                new_display = "dec"
            elif self.display_mode == "dec":
                new_display = "hex"
            elif self.diaplay_mode == "hex":
                new_display = "bin"

            self.convertMode(new_display)

        elif mode in ['bin', 'oct', 'dec', 'hex']:
            self.convertMode(mode)
        else:
            print("Please choose one of the following display modes: bin, oct, dec, hex")

    def convertMode(self, mode):
        old_mode = self.display_mode
        old_state = self.state
        new_mode = mode

        # Convert from old_mode into dec
        if old_mode == "bin":
            to_dec = int(old_state, 2)
        elif old_mode == "oct":
            to_dec = int(old_state, 8)
        elif old_mode == "dec":
            to_dec = int(old_state, 10)
        elif old_mode == "hex":
            to_dec = int(old_state, 16)

        # Convert from dec into new_mode
        if new_mode == "bin":
            new_state = bin(to_dec)
        elif new_mode == "oct":
            new_state = oct(to_dec)
        elif new_mode == "dec":
            new_state = to_dec
        elif new_mode == "hex":
            new_state = hex(to_dec)

        self.state = new_state
        self.display_mode = new_mode
