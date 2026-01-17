from question_loader import load_questions
from Game_Engine import Game
def play():
    game=Game(load_questions())
    while game.isContinue():
        user_input=input(f"(Q {game.question_number+1}) {game.next_question()} --> (True or False?):-").lower()
        while user_input not in ['true','false']:
            user_input=input("Enter a valid choice:")
        if game.check_answer(user_input):
            print("Good")
            game.update_score()
        print(f"The answer was {game.questions[game.question_number].answer},Score = {game.score}/{len(game.questions)}")
        game.update_question()
    print(f"Final Score: {game.score}")
play()