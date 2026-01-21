from question_model import Question
from data import question_data
def load_questions():
    questions=[]
    for i in question_data:
        question_object=Question(i['text'],i['answer'])
        questions.append(question_object)
    return questions


