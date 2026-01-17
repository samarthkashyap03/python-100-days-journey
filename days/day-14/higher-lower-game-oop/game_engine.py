import random
class HigherLower:
    def __init__(self,data):
        self.data=data
        self.score=0
    def generate_question(self):
        return random.choice(self.data)
    def compare(self,option1:int,option2:int,user_input:str):
        if option1>option2 and user_input=='a':
            self.score+=1
            return 'a'
        elif option2>option1 and user_input=='b':
            self.score+=1
            return 'b'
        return "Incorrect"
    
