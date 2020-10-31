import math

#list = ["Degrees","Radians","Gradian"]
#unit_mode = 1


class Scientfic_calculator:
    def __init__(self):
        pass

    def getOneNumbers(self):
        a = float(input(" Your number? "))
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
    def SwitchUnitsMode(self):
        unit = input("Radian or Degree")
        if (unit == "Radian"):
            unit_value = input("Enter the Value :")
            return math.radians(int(unit_value))
        elif unit == "Degree":
            unit_value = input("Enter the Value :")
            return math.degrees(int(unit_value))

    def SwitchUnitMode(self):
        mode = input("Operation ?")
        if (mode != "radian" and mode != "degree" ):
            a = self.getOneNumbers()
        while True:
            if mode == 'q':
                break
            if (mode== "sin"):
               # a = self.getOneNumbers()
               print(self.sin(int(a)))
            elif (mode== "cos"):
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
            mode = input("Operation ?")
            if (mode != "radian" and mode != "degree" and mode != "q"):
                a = self.getOneNumbers()

trig = Scientfic_calculator()



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