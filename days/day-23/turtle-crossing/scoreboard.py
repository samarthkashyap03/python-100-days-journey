from turtle import Turtle
class Scoreboard:
    #CONSTANTS
    X_COORDINATE=-280
    Y_COORDINATE=260

    def __init__(self):
        """
        Used as a scoreboard for games, creating an object already initialises the score and sets it to zero, no need to use display_score()
        Methods:\n
        1. Has a update_score Function, which clears the score, increments with 1 and writes it again\n
        2. game_over()-> Displays game over message at the center of the screen
        """
        self.lives=0
        self.score=Turtle()
        self.score.hideturtle()
        self.score.color('black')
        self.score.penup()
        self.score.goto(x=Scoreboard.X_COORDINATE,y=Scoreboard.Y_COORDINATE)
        self.display_score()
        
    def display_score(self):
        self.score.write(arg=f"Score: {self.lives}",align="left",font=("Arial",20,"normal"))
    def update_score(self):
        """Clears the score text, increments with 1 and writes it again"""
        self.score.clear()
        self.lives+=1
        self.display_score()
    def game_over(self):
        """Displays game over message at the center of the screen"""
        self.score.goto(0,0)
        self.score.write(arg=f"GAME OVER",align="center",font=("Arial",20,"normal"))

