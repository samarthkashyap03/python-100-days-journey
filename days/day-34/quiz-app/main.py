import download_questions
from generate_question_list import generate_list
from QuizEngine import QuizEngine
download_questions.download_questions()
questions=generate_list()
quizgame=QuizEngine(questions)
while quizgame.question_is_available():
    user_input=input(quizgame.next_question())
    while user_input.lower() not in ['true','false']:
        user_input=input('Enter a valid choice:')
    if quizgame.check_answer(user_input):
        print("You are right!")
        quizgame.update_score()
    print(f"Current Score: {quizgame.current_score()}/{quizgame.number_of_questions}")
    print(f"Correct answer: {quizgame.correct_answer()}")
    quizgame.update_question_number()
print(f"Total Score: {quizgame.current_score()}")

        





    