from turtle import Screen,Turtle
def screen_setup():
    """Initialises the screen onbject and returns the same
       Can be used for games, with a net in the center"""
    screen=Screen()
    screen.tracer(0)
    screen.setup(700,700)
    screen.bgcolor('black')
    center_line=Turtle()
    center_line.color('white')
    center_line.penup()
    center_line.sety(350)
    center_line.hideturtle()
    center_line.right(90)
    center_line.width(5)
    while center_line.ycor()>-350:
        center_line.pendown()
        center_line.forward(10)
        center_line.penup()
        center_line.forward(10)
    screen.update()
    return screen
    