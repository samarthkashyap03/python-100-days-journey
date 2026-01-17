import turtle
from Hirst_painting import Hirst_painting
TURTLE_OBJECT=turtle.Turtle()
screen=turtle.Screen()
turtle.colormode(255)
FILE_PATH="image.png"
hirst_painting=Hirst_painting(TURTLE_OBJECT,FILE_PATH)
hirst_painting.create_dot()
screen.exitonclick()
