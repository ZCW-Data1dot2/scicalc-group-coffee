from calculator import Calculator
from Trig_Functions import Scientfic_calculator

def display_mode():
   while True:
       mode = input("What display mode would you like to work in? Options: Default,\n Bianary, Octal, Decimal, Hexidecimal , Trig_functions? or Enter q to Quit")
       if mode == 'Default':
           calc = Calculator()
           performCalcLoop(calc)
       # if mode == 'Bianary' continue looping through using functions in Bianary mode:
       if ( mode == 'Trig_functions' or mode == "Trig"):
           print("Your basic operations are: sin,cos,tan,inv_sin,inv_cos,inv_tan,radian")
           trig = Scientfic_calculator()
           # x = input("Operation ?")
           trig.SwitchUnitMode()
       if ( mode == "q"):
           break




def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input("Your number? "))
    return a

def displayResult(x: float):
    print(x, "\n")


def performCalcLoop(calc):
    print("Your basic operations are: add, subtract, multiply, divide, " \
    "square, square root, exponentiate, inverse and invert. \n" \
    "If you would like to use the trig functions, type 'Trig'\n" \
    "Type q to quit the program")
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))
        elif choice == 'subtract':
            a, b = getTwoNumbers()
            displayResult(calc.sub(a, b))
        elif choice == 'multiply':
            a, b = getTwoNumbers()
            displayResult(calc.multiply(a, b))
        elif choice == 'divide':
            a, b = getTwoNumbers()
            displayResult(calc.divide(a, b))
        elif choice == 'square':
            a = getOneNumber()
            displayResult(calc.square(a))
        elif choice == 'square root':
            a = getOneNumber()
            displayResult(calc.square_root(a))
        elif choice == 'exponentiate':
            a, b = getTwoNumbers()
            displayResult(calc.exponentiate(a,b))
        elif choice == 'inverse':
            a = getOneNumber()
            displayResult(calc.inverse(a))
        elif choice == 'invert':
            a = getOneNumber()
            displayResult(calc.invert(a))
        elif choice == 'Who deserves 500 points?':
            return "Coffee Group"
        else:
            print("That is not a valid input.")


# main start
def main():
    display_mode()
    # calc = Calculator()
    # performCalcLoop(calc)
    # trig = Trig()
    # performTrigLoop(trig) Hey Suma/Luke I originally put these here but since I added the default /n
    # display_mode function which is called first, you should call the trig function in the desplay mode function. see line 6 and 7
    print("Done Calculating.")

print("Welcome to the Coffee Group Calculator")


if __name__ == '__main__':
    main()



