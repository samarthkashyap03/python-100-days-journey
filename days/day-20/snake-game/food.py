from turtle import Turtle
import random
class Food:
    def __init__(self):
        '''Creates a Food object at a random Location
           Methods: 
           1.render_food()        
        '''
        self.food=Turtle(shape='circle')
        self.food.shapesize(0.5,0.5)
        self.food.color('red')
        self.food.penup()
        self.render_food()
    def render_food(self):
        '''
        Creates food at random x,y 
        :param self: Description
        '''
        self.food.goto(random.randint(-270,270),random.randint(-270,270))
