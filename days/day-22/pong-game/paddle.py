from turtle import Turtle
class Paddle:
    """Creates a paddle on the Screen"""
    SCREEN_SIZE=700
    OFFSET=25 #Used in Move functions
    PADDLE_BOUNDRY=SCREEN_SIZE/2 -75 #offset of 77
    def __init__(self,paddle_position:int):
        """
        Methods:\n
        1.move_up() - It is a function that moves the paddle up by x pixels
        2.move_down() - Moves the paddle in downward directtion
        
        :param paddle_position: The position indicating where we want the paddle to be placed.
        :type paddle_position: int
        """
        self.paddle_object=Turtle(shape='square')
        self.paddle_object.color('white')
        self.paddle_object.shapesize(stretch_len=6,stretch_wid=1)
        self.paddle_object.penup()
        self.paddle_object.setx(paddle_position)
        self.paddle_object.setheading(90)
        
    
    def move_up(self):
        """It is a function that moves the paddle up by x pixels"""
        if self.paddle_object.ycor()<Paddle.PADDLE_BOUNDRY:
            self.paddle_object.sety(self.paddle_object.ycor()+Paddle.OFFSET)
    def move_down(self):
        """It is a function that moves the paddle Down by x pixels"""
        if self.paddle_object.ycor()>-Paddle.PADDLE_BOUNDRY:
            self.paddle_object.sety(self.paddle_object.ycor()-Paddle.OFFSET)
