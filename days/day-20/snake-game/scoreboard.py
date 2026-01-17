from turtle import Turtle
class Score:
    def __init__(self):
        '''Creates a Scoreboard to Display Score
           Methods:
           1.refresh_score() 
           2.game_over() 
           '''
        self.current_score=0
        self.scoreboard=Turtle()
        self.scoreboard.penup()
        with open('highscore.txt',mode='r') as f:
            self.high_score=int(f.read())
        self.scoreboard.hideturtle()
        self.scoreboard.color('white')
        self.scoreboard.goto(x=0,y=270)
        self.write_score()
    def refresh_score(self):
        '''
        ->Increase the Score by 1
        
        :param self: Description
        '''
        self.current_score+=1
        self.write_score()
    def write_score(self):
        self.scoreboard.clear()
        self.scoreboard.write(arg=f"Score = {self.current_score}               High Score = {self.high_score}",align='center',font=("Arial",20,"normal"))
    def game_over(self)->None:
        '''
        -> Display 'Game over' message
        '''
        self.scoreboard.home()
        self.scoreboard.write(arg=f"GAME OVER",align='center',font=("Arial",20,"normal"))
    def reset(self):
        if self.current_score>self.high_score:
            with open('highscore.txt',mode='w') as f:
                f.write(str(self.current_score))
                self.high_score=self.current_score
        self.current_score=0
        self.scoreboard.goto(x=0,y=270)
        self.write_score()