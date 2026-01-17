import turtle
my_turtle=turtle.Turtle()
my_screen=turtle.Screen()
my_screen.listen()

def move_forward():
    my_turtle.forward(25)
def move_backward():
    my_turtle.back(25)
def turn_clockwise():
    my_turtle.right(10)
def turn_anti_clockwise():
    my_turtle.left(10)
def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()
my_screen.onkeypress(move_forward,'w')
my_screen.onkeypress(move_backward,'s')
my_screen.onkeypress(turn_clockwise,'d')
my_screen.onkeypress(turn_anti_clockwise,'a')
my_screen.onkeypress(clear,'c')
my_screen.exitonclick()