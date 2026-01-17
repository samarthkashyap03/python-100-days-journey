from turtle import Turtle
import random
class Car():
    #----------CONSTANTS-------------
    COLORS=['red','orange','brown','pink','yellow','green','blue','black','violet','cyan']
    CARS=[]
    LEFT_SCREEN_BOUND=-320 #Limit of the left side of screen
    X_COORDINATE=310 # A constant where the car will always be position 
    LOWER_BOUND=-230 #Lower end of screen, i.e Y=-230
    UPPER_BOUND=250 #Upper end of screen, decide from where to where along y cars have to be spawned
    INCREMENT=50 #Step size for random function
    CAR_HEADING=180 #Orientation of car
    MOVE_DISTANCE=10 #Distance the car moves every time the function is called

    def __init__(self):
        """
        Generates a car object
        Methods:\n
        1. move_cars() -> Moves all the cars on the screen
        """
        self.YCOR=random.randrange(Car.LOWER_BOUND,Car.UPPER_BOUND,Car.INCREMENT)
        self.car_body=Turtle(shape='square')
        self.car_body.shapesize(stretch_len=4,stretch_wid=1)
        self.car_body.penup()
        self.car_body.showturtle()
        self.car_body.color(random.choice(Car.COLORS))
        self.car_body.goto(Car.X_COORDINATE,self.YCOR)
        self.car_body.setheading(Car.CAR_HEADING)

    def move_cars(self)->None:
        """
        Moves all the cars on the screen
        """
        for car in Car.CARS:
            if car.car_body.xcor()<Car.LEFT_SCREEN_BOUND:
                Car.CARS.remove(car)
            car.car_body.forward(Car.MOVE_DISTANCE)


