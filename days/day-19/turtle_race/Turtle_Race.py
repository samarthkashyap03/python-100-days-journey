import turtle
import random
class TurtleRace:
    def __init__(self,colors:list):
        self.screen=turtle.Screen()
        self.screen.setup(600,600)
        self.turtles=[]
        self.colours=colors
        self.race_on=True
    def generate_turtles(self):
        for i in self.colours:
            turtle_object=turtle.Turtle(shape='turtle')
            turtle_object.color(i)
            self.turtles.append(turtle_object)
        
    def set_initial_position(self):
        y_count=100
        for turtle in self.turtles:
            turtle.penup()
            turtle.goto(x=-280,y=y_count)
            y_count-=30
        
    def ask_input(self):
        bet=self.screen.textinput(title="Bet on a turtle",prompt=f"Enter the colour of the turtle you want to bet on-{self.colours}")
        while bet not in self.colours:
            bet=self.screen.textinput(title="Bet on a turtle",prompt=f"Enter calid Choice-{self.colours}")
        return bet
    
    def verify_bet(self,bet,winner):
        return bet==winner.pencolor()
    
    def start_race(self):
        while self.race_on:
            for turtle in self.turtles:
                if turtle.xcor()>260:
                    self.race_on=False
                    return turtle
                turtle.forward(random.randint(1,10))
        self.screen.exitonclick()
        
   

