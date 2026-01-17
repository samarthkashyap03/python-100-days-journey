import random
number=0
def pick_number():
    global number
    print("Welcome to the Number Guessing game:")
    print("I am thinking of a number between 1 and 100")
    number=random.randint(1,100)
def choose_difficulty(d):
    if d=='e':
        lives=10
    elif d=='d':
        lives=5
    else:
        print("Incorrect Option")
        lives=False
    return lives
def check_number(number,lives):
    print(f"You have {lives} attempts left!")
    user_input=int(input("Guess the number:"))
    if user_input in range(1,101):
        if user_input<number:
            print("Too Low")
        elif user_input>number:
            print("Too High")
        else:
            print(f"You Guessed the number right!, it is {number}")
            return False
        return True
    else:
        print("Enter the number in the range 1 and 100!")
        return True

def play():
    pick_number()
    lives=choose_difficulty(input("Enter E for Easy mode, D for difficult mode:").lower())
    if lives is False:
        return
    print(number)
    while lives>0:
        if check_number(number=number,lives=lives)==False:
            return
        lives-=1
    if lives==0:
        print(f"You ran out of attempts, the number was {number}")
while input("Do you want to play Number guessing game?, Y or N?:").lower()=='y':
    play()
print("Thanks for playing!!")