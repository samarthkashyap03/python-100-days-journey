import random
class Guess:
    def __init__(self,attempts):
        self.attempts_left=attempts
        self.random_number=random.randint(1,100)
    def compare(self,user_choice):
        self.attempts_left-=1
        if user_choice>self.random_number:
            return "Too High"
        elif user_choice<self.random_number:
            return "Too Low"
        else:
            return "Correct"
    def is_attempts_left(self):
        return self.attempts_left>0
                
      
