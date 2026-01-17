from turtle import Turtle
class Scoreboard:
    #Constants
    XCOR=345 #X co-ordinate for the scoreboard
    YCOR=280 #Y co-ordinate for the scoreboard
    FONT=("Courier",20,'bold')

    def __init__(self)->None:
        """Class to maintain the score and highscore\n
        Methods:\n
        1.update_score() -> Increments score by 1 and writes it on screen\n
        2.update_highscore() -> Increments highscore by 1 and writes it on screen, also writes it to a local file."""
        self.score=0
        with open('highscore.txt','r') as  f:
            self.highscore=f.read()
        self.score_text=Turtle()
        self.score_text.hideturtle()
        self.score_text.penup()
        self.score_text.goto(-Scoreboard.XCOR,Scoreboard.YCOR)
        self.write_score()
        self.high_score_text=Turtle()
        self.high_score_text.hideturtle()
        self.high_score_text.penup()
        self.high_score_text.goto(Scoreboard.XCOR,Scoreboard.YCOR)
        self.write_highscore()
        
    def write_score(self)->None: 
        self.score_text.clear()
        self.score_text.write(arg=f"Score: {self.score}/ 50",font=Scoreboard.FONT) 
    
    def write_highscore(self)->None:
        self.high_score_text.clear()
        self.high_score_text.write(arg=f"Highscore: {self.highscore}",font=Scoreboard.FONT,align='right')
    
    def update_score(self)->None:
        self.score+=1
        self.write_score()
    
    def update_highscore(self)->None:
        if self.score>int(self.highscore):
           self.highscore=self.score
           with open('highscore.txt','w') as f:
                f.write(str(self.highscore))
        self.write_highscore()
