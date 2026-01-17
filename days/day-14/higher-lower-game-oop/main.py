import data_loader
import art
from game_engine import HigherLower
questions=data_loader.data()
def play():
    print(art.Welcome_logo)
    game=HigherLower(questions)
    option_a=game.generate_question()
    option_b=game.generate_question()
    while True:
        print(f"COMPARE A: {option_a.name}, a {option_a.description}, from {option_a.country}")
        print(art.VS)
        print(f"COMPARE B: {option_b.name}, a {option_b.description}, from {option_b.country}")
        user_input=input("Enter A or B:-").lower()
        while user_input not in ['a','b']:
            user_input=input("Enter a valid Choice:")
        result=game.compare(option1=option_a.followers,option2=option_b.followers,user_input=user_input)
        if result=='Incorrect':
            print(f"Game Over, Final Score: {game.score}, Correct answer: {option_a.name if option_a.followers>option_b.followers else option_b.name}")
            return
        elif result=='a':
            option_b=game.generate_question()
        else:
            option_a=game.generate_question()
            option_b=game.generate_question()
        print(f"Correct Guess, Score = {game.score}")
play()
