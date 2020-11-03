import math

class Calculator:

    def __init__(self):
        self.state = 0
        self.display_mode = "dec"
        self.memory = 0
        self.degree = "deg"

    def getOneNumbers1(self):
        a = int(input(" Your number? "))
        return a

    def sin(self, val):
        return (round(math.sin(val),10))

    def cos(self, val):
        return (round(math.cos(val),11))

    def tan(self, val):
        return (round(math.tan(val),11))

    def inv_sin(self, val):
        if (val >= -1 and val <= 1):
            return (round(math.asin(val),11))
        else:
            return "Error"

    def inv_cos(self, val):
        if (val >= -1 and val <= 1):
            return (round(math.acos(val),11))
        else:
            return "Error"

    def inv_tan(self, val):
        return (round(math.atan(val),11))

    def SwitchUnitsMode(self,val,mode):
        #unit = input("radian or degree")
        if (mode == "radian"):
            #unit_value = input("Enter the Value :")
            return (round(math.radians(int(val)),7))
        elif mode == "degree":
            #unit_value = input("Enter the Value :")
            return (round(math.degrees(int(val)),7))

    def getOneNumber(self):
        a = int(input("Your number? "))
        return a

    def degree(self):
        unit_value = self.getOneNumbers()
        self.state = math.radians(int(unit_value))

    def SwitchUnitMode(self):
        mode = input("Scientific Operation? ")
        #if (mode != "radian" and mode != "degree"):
        a = self.getOneNumbers1()
        # while True:
        # if mode == 'q':
        # break
        if (mode == "sin"):
            # a = self.getOneNumbers()
            self.state = self.sin(int(a))
        elif (mode == "cos"):
            # a = self.getOneNumbers()
            self.state = self.cos(int(a))
        elif (mode == "tan"):
            # a = self.getOneNumbers()
            self.state = self.tan(int(a))
        elif (mode == "inv_sin"):
            # a = self.getOneNumbers()
            self.state = self.inv_sin(int(a))
        elif (mode == "inv_cos"):
            # a = self.getOneNumbers()
            self.state = self.inv_cos(int(a))
        elif (mode == "inv_tan"):
            # a = self.getOneNumbers()
            self.state = self.inv_tan(int(a))
        elif (mode == "radian" or mode == "degree"):

            self.state = self.SwitchUnitsMode(a,mode)

        else:
            print("Not a valid input.")

    def displayResult(self):
        display_state = self.convertMode()
        print("State:" + display_state)

    # def displayResult

    def add(self, a, b):
        self.state = a + b
        return self.state
    def sub(self, a, b):
        self.state = a - b
        return self.state

# add lots more methods to this calculator class.
    def multiply(self, a, b):
        self.state = a * b
        return self.state

    def divide(self, a, b):
        self.state = a/b
        return self.state

    def square(self, a):
        self.state = a ** 2
        return self.state

    def square_root(self, a):
        self.state = math.sqrt(a)
        return self.state

    def exponentiate(self, a, b):
        self.state = a ** b
        return self.state

    def inverse(self, a):
        self.state = 1/a
        return self.state

    def invert(self, a):
        self.state = -a
        return self.state

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

    def DegreeorRadian(self, mode):
        if mode == '':
            if self.degrees == "deg":
                self.degrees = "rad"
            elif self.radian == "deg":
                self.radian = "rad"
        elif mode in ('deg','rad'):
            self.degrees = mode
        else:
            print("invalid")

    # def SwitchUnitsMode(self):
    #     if self.degree == 'deg':
    #          new_state = math.degree(self.state)
    #     elif self.degree == 'rad':
    #          new_state = math.radians(self.state)
    #     return new_state