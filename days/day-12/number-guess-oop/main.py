from Guess import Guess
import set_difficulty

def play():
    level=input("Enter the difficulty, E for easy and H for Hard:").lower()
    while level not in ['e','h']:
        level=input('Enter a valid Choice:-')
    lives=set_difficulty.set_difficulty(level)
    number_guess=Guess(lives)
    print(f"You will get {lives} attempts:-")
    while number_guess.is_attempts_left():
        user_input=int(input("Enter a number between 1 to 100:"))
        while user_input<1 or user_input>100:
            user_input=int(input("Enter a number between 1 to 100:"))
        result=number_guess.compare(user_input)
        if result=='Correct':
            print(f"You guessed Correctly, the number was {user_input}")
            break
        else:
            print(result)
        print(f"You have {number_guess.attempts_left} lives left!")
    
    print(f"Attempts over, the word was {number_guess.random_number}")

play()
