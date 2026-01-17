class QuizEngine:
    def __init__(self,questions_list:list):
        self.questions=questions_list
        self.number_of_questions=len(self.questions)
        self.current_question_number=0
        self.score=0
    def next_question(self):
        return f"Q({self.current_question_number+1}): {self.questions[self.current_question_number].question} ->(True or False)?"
    def check_answer(self,user_input):
        return user_input.lower()==(self.questions[self.current_question_number].answer).lower()
    def update_score(self):
        self.score+=1
    def correct_answer(self):
        return self.questions[self.current_question_number].answer.lower()
    def update_question_number(self):
        self.current_question_number+=1
    def question_is_available(self):
        return self.current_question_number<self.number_of_questions
    def current_score(self):
        return self.score