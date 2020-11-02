import math

class Calculator:

    def __init__(self):
        self.state = 0
        self.display_mode = "dec"
        self.memory = 0

    def getOneNumbers(self):
        a = float(input(" Your number? "))
        return a

    def sin(self, val):
        return math.sin(val)

    def cos(self, val):
        return math.cos(val)

    def tan(self, val):
        return math.tan(val)

    def inv_sin(self, val):
        if (val >= -1 and val <= 1):
            return math.asin(val)
        else:
            return "Error"

    def inv_cos(self, val):
        if (val >= -1 and val <= 1):
            return math.acos(val)
        else:
            return "Error"

    def inv_tan(self, val):
        return math.atan(val)

    def SwitchUnitsMode(self):
        unit = input("Radian or Degree")
        if (unit == "Radian"):
            unit_value = input("Enter the Value :")
            return math.radians(int(unit_value))
        elif unit == "Degree":
            unit_value = input("Enter the Value :")
            return math.degrees(int(unit_value))

    def SwitchUnitMode(self):
        mode = input("Scientific Operation? ")
        if (mode != "radian" and mode != "degree"):
            a = self.getOneNumbers()
            # while True:
            # if mode == 'q':
            # break
            if (mode == "sin"):
                # a = self.getOneNumbers()
                print(self.sin(int(a)))
            elif (mode == "cos"):
                # a = self.getOneNumbers()
                print(self.cos(int(a)))
            elif (mode == "tan"):
                # a = self.getOneNumbers()
                print(self.tan(int(a)))
            elif (mode == "inv sin"):
                # a = self.getOneNumbers()
                print(self.inv_sin(int(a)))
            elif (mode == "inv cos"):
                # a = self.getOneNumbers()
                print(self.inv_cos(int(a)))
            elif (mode == "inv tan"):
                # a = self.getOneNumbers()
                print(self.inv_tan(int(a)))
            elif (mode == "radian" or mode == "degree"):
                print(self.SwitchUnitsMode())
            else:
                print("Not a valid input.")

    def displayResult(self):
        display_state = self.convertMode()
        print(display_state)

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
        self.state = -a

    def add_to_memory(self):
        self.memory += self.state

    def reset_memory(self):
        self.memory = 0

    def recall_memory(self):
        print(self.memory)

    def switchDisplayMode(self, mode):
        # Updates the `display_mode` variable
        if mode == '':
            if self.display_mode == "bin":
                self.display_mode = "oct"
            elif self.display_mode == "oct":
                self.display_mode = "dec"
            elif self.display_mode == "dec":
                self.display_mode = "hex"
            elif self.display_mode == "hex":
                self.display_mode = "bin"
        elif mode in ['bin', 'oct', 'dec', 'hex']:
            self.display_mode = mode
        else:
            print("Please choose one of the following display modes: bin, oct, dec, hex")

    def convertMode(self):
        # Convert state from dec into display_mode
        if self.display_mode == "bin":
            new_state = bin(self.state)
        elif self.display_mode == "oct":
            new_state = oct(self.state)
        elif self.display_mode == "dec":
            new_state = str(self.state)
        elif self.display_mode == "hex":
            new_state = hex(self.state)
        return new_state
