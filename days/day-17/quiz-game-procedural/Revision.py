from data import question_data
def display_question(i):
    user_choice=input(f'(Q {i+1}){question_data[i]["text"]} --(True or False):').lower()
    while user_choice.title() not in ['True',"False"]:
        user_choice=input(f'Enter Valid Choice--(True or False):').lower()
    return user_choice.title()
def check_answer(user_answer,i,SCORE):
    if user_answer==question_data[i]["answer"]:
        SCORE+=1
        print(f"Correct answer, it is {user_answer}")
    else:
        print(f"Wrong answer, It was {question_data[i]['answer']}")
    print(f"Score: {SCORE}/{i+1}")
    return SCORE
   
def play():
    score=0
    print("Welcome to Quiz:-")
    for i in range(len(question_data)):
        user_choice=display_question(i)
        score=check_answer(user_answer=user_choice,i=i,SCORE=score)
    print("Thank you for playing!")
play()

    

