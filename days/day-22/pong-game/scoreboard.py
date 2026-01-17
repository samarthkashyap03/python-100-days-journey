from turtle import Turtle
class Scoreboard:
    SCOREBOARD_Y=305 #Places the scoreboard at the top of the screen
    def __init__(self,position:int):
        self.score=0
        self.score_object=Turtle()
        self.score_object.penup()
        self.score_object.color('white')
        self.score_object.goto(x=position,y=Scoreboard.SCOREBOARD_Y)
        self.score_object.hideturtle()
        self.display_score()
        
    def display_score(self):
        self.score_object.write(arg=f"{self.score}",align='center',font=("Arial",30,'bold'))

    def update_score(self):
        self.score_object.clear()
        self.score+=1
        self.display_score()