from turtle import Turtle
import random
class Ball:
    def __init__(self):
        """
        Methods:\n
        1.reset_ball()
        2.move_ball()
        3.react_to_paddle_collisions()
        4.react_to_wall_collisions()
        """
        self.game_is_on=True
        self.ball_object=Turtle(shape='circle')
        self.ball_object.color('white')
        self.ball_object.shapesize(1,1)
        self.ball_object.penup()
        self.reset_ball()
    def reset_ball(self,winner=None)->None:
        """
        Resets the ball position to init.
        
        :param winner: Pass the parameter as 'A' or "B", so that ball is served at the direction of the loser.
        """
        self.ball_object.goto(0,random.randint(-240,240))
        if winner=='A':
            self.heading=random.randint(110,250)
        else:
            self.heading=random.randint(-60,60)
    def move_ball(self):
            """Moves the ball at the defined angle by 15 steps"""
            self.ball_object.setheading(self.heading)
            self.ball_object.forward(5)
    def react_to_paddle_collisions(self):
        """Defines how the ball reacts when it collides with the paddles"""
        current_heading=self.ball_object.heading()
        self.heading=180-current_heading
    def react_to_wall_collisions(self):
        """Defines how ball reacts when it hits top and bottom wall"""
        current_heading=self.ball_object.heading()
        self.heading=360-current_heading
        
        
        
        
         

