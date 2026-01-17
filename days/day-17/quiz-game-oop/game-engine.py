class Game:
    def __init__(self,questions:list):
        self.questions=questions
        self.score=0
        self.question_number=0
    def next_question(self):
        question=self.questions[self.question_number].question
        return question
    def isContinue(self):
        return self.question_number<len(self.questions)
    def check_answer(self,user_input):
        return user_input==(self.questions[self.question_number].answer).lower()
    def update_question(self):
        self.question_number+=1
    def update_score(self):
        self.score+=1
    
    
    

