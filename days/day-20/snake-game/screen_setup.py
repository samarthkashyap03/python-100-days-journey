from turtle import Screen
def screen_setup()->object:
    '''
    Initialise the screen, with resolution, and background colour
    '''
    screen=Screen()
    screen.bgcolor('black')
    screen.setup(600,600)
    return screen