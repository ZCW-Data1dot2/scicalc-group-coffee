import math

#list = ["Degrees","Radians","Gradian"]
#unit_mode = 1
unit = "Degrees"
unit_value = 20

class Scientfic_calculator:
    def __init__(self):
        pass

    def getOneNumbers(self):
        a = float(input(" One number? "))
        return a
    def sin(self,val):
        return math.sin(val)
    def cos(self,val):
        return math.cos(val)
    def tan(self,val):
        return math.tan(val)
    def inv_sin(self,val):
        if (val >= -1 and val <= 1):
            return math.asin(val)
        else:
            return "Error"
    def inv_cos(self,val):
        if (val >= -1 and val <= 1):
            return math.acos(val)
        else:
            return "Error"
    def inv_tan(self,val):
        return math.atan(val)
    def switchUnitsMode(self):
        global unit_value
        global unit
        if unit == "Degrees":
           unit = "Radians"
           unit_value = math.radians(unit_value)
        elif unit == "Radians":
            unit = "Degrees"
            unit_value = math.degrees(unit_value)

    def SwitchUnitMode(self,mode):
        while True:
            choice = input("Operation? ")
            if choice == 'q':
                break  #
            if (choice== "sin"):

               print(self.sin(int(mode)))
            elif (choice== "cos"):
                print(self.cos(int(mode)))
            elif (choice == "tan"):
                print(self.tan(int(mode)))
            elif (choice == "inv sin"):
                print(self.inv_sin(int(mode)))
            elif (choice == "inv cos"):
                print(self.inv_cos(int(mode)))
            elif (choice == "inv tan"):
                print(self.inv_tan(int(mode)))


trig = Scientfic_calculator()
x = trig.getOneNumbers()
trig.SwitchUnitMode(x)

# switchUnitsMode()
# print(unit_value)

# print ("The Sin value of val is " ,sin(3))
# print ("The Cos value of val is " ,cos(3))
# print ("The Tan value of val is " ,tan(3))
# print ("The Inverse Sin value of val is " ,inv_sin(3))
# print ("The Inverse Sin value of val is " ,inv_sin(1))
# print ("The Inverse Cos value of val is " ,inv_cos(3))
# print ("The Inverse Cos value of val is " ,inv_cos(-1))
# print ("The Inverse Tan value of val is " ,inv_tan(-1))
# print ("The Inverse Tan value of val is " ,inv_tan(60))