import json
from Questions import Questions
def generate_list():
    """Generates a list of question_objects, with attributes question and answer with the help of class Questions."""
    list_of_question=[]
    with open('questions.json','r') as f:
        data=json.load(f)
    for i in data['results']:
        list_of_question.append(Questions(i['question'],i['correct_answer']))
    return list_of_question