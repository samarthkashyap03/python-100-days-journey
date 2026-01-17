print("Welcome to calculator \n")
print('''
 _____________________
|  _________________  |
| | SP           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
      ''')
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def number():
    num1=float(input("What is the first number:"))
    return num1
num1=number()
operations={
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}
while True:
    num2=float(input("What is the second number:"))
    print(*operations.keys(), sep="\n")
    op=input("Choose an operation:")
    if not op in operations.keys():
        print("Invalid Choice, Try again")
        continue
    result=operations[op](a=num1,b=num2)
    print(f"The result of {num1} {op} {num2} = {result}")
    choice=input('''Press:
                C for continuing with the results:
                N for new calculation
                Q to quit the app:\n''').lower()
    if choice=='q':
        print("Thank you for using calculator")
        break
    elif choice=='c':
        num1=result
        continue
    elif choice=='n':
        num1=number()
        continue
    else:
        print("worng choice, quitting...")
        break