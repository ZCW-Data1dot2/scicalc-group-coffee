from calculator import Calculator
from Trig_Functions import Scientfic_calculator

def getTwoNumbers():
    a = int(input("first number? "))
    b = int(input("second number? "))
    return a, b

def getOneNumber():
    a = int(input("Your number? "))
    return a


def displayResult(x: float):
    print(x, "\n")


def performCalcLoop(calc):
    print("Your basic operations are: add, subtract, multiply, divide, " \
    "square, square root, exponentiate, inverse and invert. \n" \
    "If you would like to use the trig functions, type 'Trig'\n" \
    "If you would like to switch your current mode, type 'Change Mode''\n" \
    "If you would like to add displayed value to add the current value to memory''\n" \
    "use 'Add to Memory', if you would like to reset memory use 'Reset''\n" \
    "If you would like to recall the current value from memory use 'Recall''\n" \
    "Type q to quit the program")

    while True:
        # Step 1) Ask for input
        choice = input("Core Operation? ")
        # Step 2) Process input
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            calc.add(a, b)
        elif choice == 'subtract':
            a, b = getTwoNumbers()
            calc.sub(a, b)
        elif choice == 'multiply':
            a, b = getTwoNumbers()
            calc.multiply(a, b)
        elif choice == 'divide':
            a, b = getTwoNumbers()
            if b == 0:
                print("Error")
            else:
                calc.divide(a, b)
        elif choice == 'square':
            a = getOneNumber()
            calc.square(a)
        elif choice == 'square root':
            a = getOneNumber()
            calc.square_root(a)
        elif choice == 'exponentiate':
            a, b = getTwoNumbers()
            calc.exponentiate(a,b)
        elif choice == 'inverse':
            a = getOneNumber()
            calc.inverse(a)
        elif choice == 'invert':
            a = getOneNumber()
            calc.invert(a)
        elif choice == 'Who deserves 500 points?':
            return "Coffee Group"
        elif choice == 'Trig_functions' or choice == "Trig":
            print("Your basic operations are: sin,cos,tan,inv_sin,inv_cos,inv_tan,radian")
            trig = Scientfic_calculator()
            # x = input("Operation ?")
            calc.SwitchUnitMode()
        elif choice == "Change Mode":
            mode = input("Choose a display mode (or press enter to cycle): bin, oct, dec, hex\n")
            calc.switchDisplayMode(mode)
        elif choice == "Radian/Degree":
            mode = input("Choose deg or rad")
            calc.DegreeorRadian(mode)
        elif choice == "Add to Memory":
            calc.add_to_memory()
        elif choice == "Reset":
            calc.reset_memory()
        elif choice == "Recall":
            calc.recall_memory()

        else:
            print("That is not a valid input.")

        # Step 3) Display new state
        calc.displayResult()




# main start
def main():
    calc = Calculator()
    print("Your current number is: ", calc.state)
    performCalcLoop(calc)
    print("Done Calculating.")

print("Welcome to the Coffee Group Calculator")


if __name__ == '__main__':
    main()



