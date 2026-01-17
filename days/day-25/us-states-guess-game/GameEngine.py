from turtle import Turtle
import pandas as pd
class GameEngine:
    #Constants
    CSV_PATH='50_states.csv'
    OFFSET_FOR_XCOR=15

    def __init__(self)->None:
        """A function to determine the co-ordinates of a state on the map from a csv file, and write the sate name in the respective co-ordinates using turtle.write.\n
        Methods:
        1.determine_coordinates()\n
        2.write_to_coordinates()"""
        self.display_text=Turtle()
        self.display_text.hideturtle()
        self.display_text.penup()
        self.state_data=pd.read_csv(GameEngine.CSV_PATH)
        self.state_list=self.state_data['state'].tolist()
        self.lives=10

    def determine_coordinates(self,user_input)->float:
        self.input=user_input
        xcor=(self.state_data[self.state_data['state']==self.input].x).tolist()[0]-GameEngine.OFFSET_FOR_XCOR
        ycor=(self.state_data[self.state_data['state']==self.input].y).tolist()[0]
        return xcor,ycor
    
    def write_to_coordinates(self,xcor,ycor)->None:
        self.display_text.goto(xcor,ycor)
        self.display_text.write(arg=self.input)


    
