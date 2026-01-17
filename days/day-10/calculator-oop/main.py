from calculator import Calculator
from art import calculator_art
def play():
    number_1=float(input("Enter first number:"))
    number_2=float(input("Enter second number:"))
    while True:
        operation=input('''
                        Enter the Operation:
                        +: Addition
                        -: Subtraction
                        *: Multiplication
                        /: Division
                        quit: Close App
                       ''' )
        if operation not in ['+','-','*','/','quit']:
            operation=input("Enter Valid Choice:-")
        if operation=='quit':
            exit(0)
        calculator=Calculator()
        result=calculator.compute(a=number_1,b=number_2,operation=operation)
        print(f"{number_1} {operation} {number_2} = {result}")
        if input("Do you Want to Continuw with the result, Y or N:").lower()=='y':
            number_1=result
            number_2=float(input("Enter a Number: "))
            continue
        else:
            break
while True:        
    play()
    