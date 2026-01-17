from turtle import Turtle
class Snake:
    def __init__(self)->None:
        '''
        This Class allows users to create a snake body, and control it.\n
        Methods:\n
        1.create_snake_body()\n
        2.forward()\n
        3.create_segment()->Internal\n
        4.move_left()\n
        5.move_right()\n
        6.move_up()\n
        7.move_down()\n
        8.extend_snake()
        '''
        self.segments=[]
        self.game_is_on=True
        
    def create_snake_body(self):
        '''
        Creates a snake Body with 3 blocks at positions with same y co-ordinate and differed x co-ordinate.
        
        '''
        initial_positions=((0,0),(-20,0),(-40,0))
        for pos in initial_positions:
            self.create_segment(pos)
    def forward(self):
        """This function keeps the snake moving forward irrespective of heading."""
        self.snake_head=self.segments[0]
        for i in range(len(self.segments)-1,0,-1):
            new_position=self.segments[i-1].position()
            self.segments[i].goto(new_position)
        self.snake_head.forward(20)
    def create_segment(self,position):
        """This is used as a helper function inside this class."""
        segment=Turtle(shape="square")
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    def move_left(self):
        """Moves the snake left, if it is not moving right"""
        if self.snake_head.heading()!=0:
            self.snake_head.setheading(180)
    def move_right(self):
        """Turns the snake right, if not moving left"""
        if self.snake_head.heading()!=180:
            self.snake_head.setheading(0)
    def move_up(self):
        """Turns snake up if not going down"""
        if self.snake_head.heading()!=270:
            self.snake_head.setheading(90)
    def move_down(self):
        """Turns snake down if not moving up"""
        if self.snake_head.heading()!=90:
            self.snake_head.setheading(270)
    def extend_snake(self):
        """Extends the snake body by 1 block"""
        new_position=self.segments[-1].pos()
        self.create_segment(new_position)
    def reset_snake(self):
        for segment in self.segments:
            segment.goto(500,500)
        self.segments=[]
        self.create_snake_body()
        


            
