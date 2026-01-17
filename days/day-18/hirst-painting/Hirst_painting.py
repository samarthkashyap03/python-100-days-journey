import random
import colorgram
class Hirst_painting():
    def __init__(self,turtle_object:object,image_path:str):
        '''
        Docstring for __init__
        :param self: Description
        :param turtle_object: initialise a turtle object in main.py and pass it here
        :type turtle_object: object
        :param image_path: Specify an image path, to identify and extract the colours from image
        :type image_path: str
        '''
        self.t=turtle_object
        self.image_path=image_path
        self.t.penup()
        self.t.setx(-400)
        self.t.sety(-300)
        self.t.speed(0)

    def generate_colour_tuple(self):
        colours=colorgram.extract(f=self.image_path,number_of_colors=25)
        colour_list=[(colours[i].rgb.r,colours[i].rgb.g,colours[i].rgb.b) for i in range(len(colours))]
        return colour_list
        
    def create_dot(self):
        for i in range(1,101):
            self.t.dot(30,random.choice(self.generate_colour_tuple()))
            self.t.forward(50)
            if i%10==0:
                self.t.left(90)
                self.t.forward(60)
                self.t.setx(-400)
                self.t.right(90)
                continue
        
        
            

       