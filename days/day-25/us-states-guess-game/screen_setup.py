from turtle import Screen,Turtle
map_image='blank_states_img.gif'

def screen_setup()->object:
    """Setup the Screen Window and add the shape of map"""
    screen=Screen()
    screen.addshape(map_image)
    return screen

def display_image()->object:
    """Display the Map image"""
    image=Turtle()
    image.shape(map_image)
    return image